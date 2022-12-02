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

    config_grid(self,[[i,0] for i in range(0,4)], [[i,0] for i in range(0,3)])
    
    self.cIdL = tk.Label(self, text = "ID", font =self.tSize[0])
    self.cIdE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)
    
    self.cNombreL = tk.Label(self, text = "Nombre", font =self.tSize[0])
    #TODO: hacerlo alphabetico
    self.cNombreE = tk.Entry(self, font =self.tSize[0])
    
    self.cApellidoL = tk.Label(self, text = "Apellido", font =self.tSize[0])
    #TODO: hacerlo alphabetico
    self.cApellidoE = tk.Entry(self, font =self.tSize[0])
    
    self.filtro = tk.Button(self, text = "Filtrar", font =self.tSize[0], command = lambda: filterClient(self), height=bHeight-15, width=15)
    self.volver = tk.Button(self, text = "Volver", font =self.tSize[0], command = lambda: buscarCMenuInvisible(self), height=bHeight-15, width=15)
    
    self.clientsResult = ttk.Treeview(self, 
                                        columns = ("ID", "Nombre", "Apellido P.", "Apellido M.", "Fecha R.", "Telefono", "Correo"), 
                                        show = "headings",
                                        height = 30)
    
    style = ttk.Style()
    style.configure("Treeview", font=self.tSize[0])
    style.configure("Treeview.Heading", font=self.tSize[0])
    tree_handler(self.clientsResult, [80, 125, 125, 125, 125, 125, 300])        
    for client in self.manejador.get_clients():
        self.clientsResult.insert('', 'end', iid=client[0], values = client)
    self.clientsResult.bind('<Button-1>', C_event_handler)
    
    grid_positioning(0,
                        [[self.cIdL, [self.cIdE], 1],
                        [self.cNombreL, [self.cNombreE], 1],
                        [self.cApellidoL, [self.cApellidoE], 1]])        
    
    self.filtro.grid(column=0, row=3, columnspan=2)
    self.volver.grid(column=0, row=4, columnspan=2)
    self.clientsResult.grid(column=2, row=0, rowspan=1000)
    verscrlbar = ttk.Scrollbar(self, orient ="vertical", command = self.clientsResult.yview)
    verscrlbar.grid(column=3, row=0, rowspan=1000, sticky='ns')
    self.clientsResult.configure(yscrollcommand = verscrlbar.set)
    
    self.buscarCMenu = [self.cIdL,self.cIdE,
                        self.cNombreL,self.cNombreE,
                        self.cApellidoL,self.cApellidoE,
                        self.filtro, self.volver,
                        self.clientsResult, verscrlbar]   

def filterClient(self):
    clients = clientSearch(self)
    for i in self.clientsResult.get_children():
            self.clientsResult.delete(i)
    if clients != []:
        for client in clients:
            self.clientsResult.insert('', 'end', iid=client[0], values = client)
    else:
        for client in self.manejador.get_clients():
            self.clientsResult.insert('', 'end', iid=client[0], values = client)

def clientSearch(self):
    id = self.cIdE.get()
    id = id if id != '' else 0
    clients=[]
    query = 'select * from cliente where '
    if id == 0:
        nombre = self.cNombreE.get()
        apellidos = self.cApellidoE.get()
        if nombre == '':
            apellidos = (apellidos + (' ')).split(" ")
            if apellidos[1]=='': query+= 'apellidoP LIKE \"%'+apellidos[0]+'%\"'
            else: query += 'apellidoP LIKE \"%'+apellidos[0]+'%\" OR apellidoM LIKE \"%'+apellidos[1]+'%\"'
        elif apellidos == '':
            query += 'nombre LIKE \"%'+nombre+'%\";'
        else:
            query += 'nombre LIKE \"%'+nombre+'%\" OR apellidoP LIKE \"%'+apellidos[0]+'%\" OR apellidoM LIKE \"%'+apellidos[1]+'%\"'
    else:
        query += 'idCliente = '+id
    query += ';'
    clients = self.manejador.consultar(query)
    return clients

def C_event_handler(event):
    if Self.clientsResult.identify_region(event.x, event.y) == "separator":
        return "break"
    elif Self.clientsResult.identify_region(event.x, event.y) == "cell":
        curItem = Self.clientsResult.focus()
        pyperclip.copy(curItem)