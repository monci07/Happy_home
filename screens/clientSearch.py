import tkinter as tk
from tkinter import ttk
from interface import *

Self = 0

def clientShowMenu(self):
    global Self
    Self = self
    mainMenuInvisible(self)
    self.geometry(searchSize)
    self.title("Happy home - Client search")

    self.frameClientSearch = tk.Frame(self)
    config_grid(self.frameClientSearch,[[i,0] for i in range(0,4)], [[i,0] for i in range(0,3)])
    
    self.cIdL = tk.Label(self.frameClientSearch, text = "ID", font =self.tSize[0])
    self.cIdE = tk.Entry(self.frameClientSearch, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.cNombreL = tk.Label(self.frameClientSearch, text = "Nombre", font =self.tSize[0])
    self.cNombreE = tk.Entry(self.frameClientSearch, font =self.tSize[0], validate = 'key', validatecommand = self.vcmdAlpha)
    
    self.cApellidoL = tk.Label(self.frameClientSearch, text = "Apellido", font =self.tSize[0])
    self.cApellidoE = tk.Entry(self.frameClientSearch, font =self.tSize[0], validate = 'key', validatecommand = self.vcmdAlpha)
    
    self.filtro = tk.Button(self.frameClientSearch, text = "Filtrar", font =self.tSize[0], command = lambda: filterClient(self), height=bHeight-15, width=15)
    self.volver = tk.Button(self.frameClientSearch, text = "Volver", font =self.tSize[0], command = lambda: buscarCMenuInvisible(self), height=bHeight-15, width=15)
    
    self.clientsResult = ttk.Treeview(self.frameClientSearch, 
                                        columns = ("ID", "Nombre", "Apellido P.", "Apellido M.", "Fecha R.", "Telefono", "Correo"), 
                                        show = "headings",
                                        height = 33)
    
    style = ttk.Style()
    style.configure("Treeview", font=self.tSize[0])
    style.configure("Treeview.Heading", font=self.tSize[0])
    tree_handler(self.clientsResult, [80, 125, 125, 125, 125, 125, 300])        
    for client in self.manejador.get_clients():
        self.clientsResult.insert('', 'end', iid=client[0], values = client)
    self.clientsResult.bind('<Button-1>', C_event_handler)
    
    grid_positioning(0,
                        [[self.cIdL, self.cIdE],
                        [self.cNombreL, self.cNombreE],
                        [self.cApellidoL, self.cApellidoE]])
    
    self.filtro.grid(column=0, row=3, columnspan=2)
    self.volver.grid(column=0, row=4, columnspan=2)
    self.clientsResult.grid(column=2, row=0, rowspan=1000)
    verscrlbar = ttk.Scrollbar(self.frameClientSearch, orient ="vertical", command = self.clientsResult.yview)
    verscrlbar.grid(column=3, row=0, rowspan=1000, sticky='ns')
    self.clientsResult.configure(yscrollcommand = verscrlbar.set)
    
    self.buscarCMenu = [self.cIdL,self.cIdE,
                        self.cNombreL,self.cNombreE,
                        self.cApellidoL,self.cApellidoE,
                        self.filtro, self.volver,
                        self.clientsResult, verscrlbar]   
    
    self.frameClientSearch.grid(column=0, row=0, sticky='nsew')

def filterClient(self):
    # create a list of all client objects
    clients = clientSearch(self)

    # delete all children from the treeview
    for i in self.clientsResult.get_children():
        self.clientsResult.delete(i)

    # if the list of clients is not empty
    if clients != []:
        # add all clients in the list to the treeview
        for client in clients:
            self.clientsResult.insert('', 'end', iid=client[0], values = client)
    # if the list of clients is empty
    else:
        # add all clients from the database to the treeview
        for client in self.manejador.get_clients():
            self.clientsResult.insert('', 'end', iid=client[0], values = client)

def clientSearch(self):
    # Get the id of the client from the entry
    id = self.cIdE.get()
    # If the id is empty, give it the value 0
    id = id if id != '' else 0
    # Create the query
    query = 'select * from cliente where '
    # If the id is 0, the user is searching by name
    if id == 0:
        # Get the name of the client from the entry
        nombre = self.cNombreE.get()
        # Get the last name of the client from the entry
        apellidos = self.cApellidoE.get()
        # If the name is empty, the user is searching by last name
        if nombre == '':
            # Split the last name in two parts
            apellidos = (apellidos + (' ')).split(" ")
            # If the second part of the last name is empty, search by the first part
            if apellidos[1]=='': query+= 'apellidoP LIKE \"%'+apellidos[0]+'%\"'
            # If the second part of the last name is not empty, search by both parts
            else: query += 'apellidoP LIKE \"%'+apellidos[0]+'%\" OR apellidoM LIKE \"%'+apellidos[1]+'%\"'
        # If the last name is empty, the user is searching by name
        elif apellidos == '':
            # Search by the first name
            query += 'nombre LIKE \"%'+nombre+'%\";'
        # If both the name and the last name are not empty, the user is searching by both
        else:
            # Search by both
            query += 'nombre LIKE \"%'+nombre+'%\" OR apellidoP LIKE \"%'+apellidos[0]+'%\" OR apellidoM LIKE \"%'+apellidos[1]+'%\"'
    # If the id is not 0, the user is searching by id
    else:
        # Search by the id
        query += 'idCliente = '+id
    query += ';'
    # Execute the query and return the results
    return self.manejador.consultar(query)

def C_event_handler(event):
    if Self.clientsResult.identify_region(event.x, event.y) == "separator":  #Checks if the cursor is over a separator
        return "break"
    elif Self.clientsResult.identify_region(event.x, event.y) == "cell":  #Checks if the cursor is over a cell
        curItem = Self.clientsResult.focus()  #Gets the current item (row) of the focused cell
        pyperclip.copy(curItem)  #Copies the value of the focused cell to the clipboard