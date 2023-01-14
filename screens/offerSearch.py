import tkinter as tk
from tkinter import ttk
from interface import *
from Screens.windows import offer
from Screens.windows import offerInfo

Self = 0

def offerShowMenu(self):
    global Self
    Self = self
    mainMenuInvisible(self)
    self.geometry(searchSize)
    self.title("Happy home - Offers Search")

    self.frameOfferSearch = tk.Frame(self)
    config_grid(self.frameOfferSearch,[[i,0] for i in range(0,19)], [[i,0] for i in range(0,3)])

    self.interesado = tk.Label(self.frameOfferSearch, text = "Interesado:", font =self.tSize[0])

    self.cIdL = tk.Label(self.frameOfferSearch, text = "ID", font =self.tSize[0])
    self.cIdE = tk.Entry(self.frameOfferSearch, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    self.cIdE.bind("<FocusOut>", check_client)
    self.cIdE.bind("<Return>", check_client)
    
    self.cNombreL = tk.Label(self.frameOfferSearch, text = "Nombre", font =self.tSize[0])
    self.cNombreE = tk.Entry(self.frameOfferSearch, font =self.tSize[0])
    
    #################################################
    
    self.oferta = tk.Label(self.frameOfferSearch, text = "Oferta:", font =self.tSize[0])
    
    self.oIdL = tk.Label(self.frameOfferSearch, text = "ID:", font =self.tSize[0])
    self.oIdE = tk.Entry(self.frameOfferSearch, font =self.tSize[0], width=self.tSize[1])
    
    self.interesL = tk.Label(self.frameOfferSearch, text = "Interes:", font =self.tSize[0])
    self.interesE = tk.Entry(self.frameOfferSearch, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    #################################################
    
    self.filtros = tk.Label(self.frameOfferSearch, text = "Filtros:", font =self.tSize[0])        
    
    self.monedaL = tk.Label(self.frameOfferSearch, text = "Moneda:", font =self.tSize[0])
    self.monedaE = tk.StringVar()
    self.monedaT = tk.OptionMenu(self.frameOfferSearch, self.monedaE, "Dolares", "Pesos")
    self.monedaT.config(font=self.tSize[0])
    menu = self.nametowidget(self.monedaT.menuname)
    menu.config(font=self.tSize[0])
    
    self.rangeL = tk.Label(self.frameOfferSearch, text = "Rango P.:", font =self.tSize[0])
    f4 = tk.Frame(self.frameOfferSearch)
    self.rangeE1 = tk.Entry(f4, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    self.rangeE2 = tk.Entry(f4, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    self.rangeE1.grid(row = 0, column=0)
    self.rangeE2.grid(row = 0, column=1)

    self.estadoL = tk.Label(self.frameOfferSearch, text = "Estado:", font =self.tSize[0])
    self.estadoE = tk.StringVar()
    self.estadoT = tk.OptionMenu(self.frameOfferSearch, self.estadoE, "Venta", "Renta")
    self.estadoT.config(font=self.tSize[0])
    menu = self.nametowidget(self.estadoT.menuname)
    menu.config(font=self.tSize[0])
    
    self.tipoL = tk.Label(self.frameOfferSearch, text = "Tipo:", font =self.tSize[0])
    tiposP = [item[1] for item in self.manejador.get_tipos()]
    self.tipoE = tk.StringVar()
    self.tipo = tk.OptionMenu(self.frameOfferSearch, self.tipoE, *tiposP)
    self.tipo.config(font=self.tSize[0])
    menu = self.nametowidget(self.tipo.menuname)
    menu.config(font=self.tSize[0])
    
    self.amuebladoL = tk.Label(self.frameOfferSearch, text = "Amueblada:", font =self.tSize[0])
    self.amuebladaE = tk.StringVar()
    self.amueblado = tk.OptionMenu(self.frameOfferSearch, self.amuebladaE, "Si", "No", "Semi")
    self.amueblado.config(font=self.tSize[0])
    menu = self.nametowidget(self.amueblado.menuname)
    menu.config(font=self.tSize[0])        
    
    self.numRecamarasL = tk.Label(self.frameOfferSearch, text = "Num. Recamaras:", font =self.tSize[0])
    self.numRecamarasE = tk.Entry(self.frameOfferSearch, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.numBañosL = tk.Label(self.frameOfferSearch, text = "Num. Baños:", font =self.tSize[0])
    self.numBañosE = tk.Entry(self.frameOfferSearch, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.numNivelesL = tk.Label(self.frameOfferSearch, text = "Num. Niveles:", font =self.tSize[0])
    self.numNivelesE = tk.Entry(self.frameOfferSearch, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.mascotasL = tk.Label(self.frameOfferSearch, text = "Mascotas:", font =self.tSize[0])
    f2 = tk.Frame(self.frameOfferSearch)
    self.mascotasE = tk.IntVar(value = 1)
    self.mascotasEO1= tk.Radiobutton(f2,
            text="Si",
            variable=self.mascotasE,
            value=1,
            font = self.tSize[0])
    self.mascotasEO2= tk.Radiobutton(f2,
            text="No",
            variable=self.mascotasE,
            value=0,
            font = self.tSize[0])

    self.mascotasEO1.grid(row=0, sticky = tk.W)
    self.mascotasEO2.grid(row=1, sticky = tk.W)
    
    self.posesionL = tk.Label(self.frameOfferSearch, text = "Posesion:", font =self.tSize[0])
    self.posesionE = tk.StringVar(self.frameOfferSearch)
    self.posesionT = tk.OptionMenu(self.frameOfferSearch, self.posesionE, "Regular", "Irregular")
    self.posesionT.config(font=self.tSize[0])
    menu = self.nametowidget(self.posesionT.menuname)
    menu.config(font=self.tSize[0])
    
    self.adjL = tk.Label(self.frameOfferSearch, text = "Adjudicada:", font =self.tSize[0])
    f3 = tk.Frame(self.frameOfferSearch)
    self.adjE = tk.IntVar(value = 1)
    self.adjEO1= tk.Radiobutton(f3,
            text="Si",
            variable=self.adjE,
            value=1,
            font = self.tSize[0])
    self.adjEO2= tk.Radiobutton(f3,
            text="No",
            variable=self.adjE,
            value=0,
            font = self.tSize[0])
    self.adjEO1.grid(row=0, sticky = tk.W)
    self.adjEO2.grid(row=1, sticky = tk.W)
    
    #################################################

    f5 = tk.Frame(self.frameOfferSearch, width = 5)
    
    self.offersResult = ttk.Treeview(f5,
                                     columns=("ID", "Direccion", "Tipo", "Estado", "Moneda", "Precio"),
                                     show = "headings",
                                     height = 33,
                                     selectmode="browse")
    style = ttk.Style()
    style.configure("Treeview", font=self.tSize[0])
    style.configure("Treeview.Heading", font=self.tSize[0])
    
    tree_handler(self.offersResult,[50, #"ID"
                                    375, #"Direccion"
                                    135, #"Tipo"
                                    90, #"Estado"
                                    110, #"Moneda"
                                    150]) #"Precio"

    self.offersResult.grid(column=0, row=0, columnspan=100)

    verscrlbar = tk.Scrollbar(f5, orient ="vertical")
    
    verscrlbar.grid(column=101, row=0, rowspan=100, sticky='nse')
    self.offersResult.configure(yscrollcommand=verscrlbar.set)
    verscrlbar.configure(command = self.offersResult.yview)    


    self.offersResult.bind('<Button-1>', O_event_handler)        
    

    frameButtonsOS = tk.Frame(self.frameOfferSearch)
    self.filroO = tk.Button(frameButtonsOS, text = "Filtrar", font =self.tSize[0], command = lambda: offerSearch(self), width=10)
    self.cerrarTrato = tk.Button(frameButtonsOS, text = "Cerrar Trato", font =self.tSize[0], command = lambda: cerrarTrato_handler(self), width=10)
    self.volver = tk.Button(frameButtonsOS, text = "Volver", font =self.tSize[0], command = lambda:buscarOMenuInvisible(self), width=10)
    
    self.frameOfferSearch.grid(column=0, row=0, sticky=tk.W)       
    
    self.interesado.grid(column=0, row=0, sticky=tk.W)
    
    grid_positioning(1,
                        [[self.cIdL, self.cIdE],
                        [self.cNombreL, self.cNombreE]])
    
    self.oferta.grid(column=0, row=3, sticky=tk.W)
    
    grid_positioning(4,
                        [[self.oIdL, self.oIdE],
                        [self.interesL, self.interesE]])
    
    self.filtros.grid(column=0, row=7, sticky=tk.W)
    
    grid_positioning(8,
                        [[self.monedaL, self.monedaT],
                        [self.rangeL, f4],
                        [self.tipoL, self.tipo],
                        [self.estadoL, self.estadoT],
                        [self.amuebladoL, self.amueblado],
                        [self.numRecamarasL, self.numRecamarasE],
                        [self.numBañosL, self.numBañosE],
                        [self.numNivelesL, self.numNivelesE],
                        [self.mascotasL, f2],
                        [self.posesionL, self.posesionT],
                        [self.adjL, f3]])    
    
    f5.grid(column=3, row=0, rowspan=20)        

    self.data = {}
    self.index = [0, 2, 3, 4, 5, 6]
    for offer in self.manejador.get_ofertas():
        if offer[0] != 0:
            data = fix_data(offer)
            self.data[data[0]] = data
            self.offersResult.insert("", tk.END, iid=data[0], values = tuple([data[i] for i in self.index]))
    frameButtonsOS.grid(column=0, row=19, columnspan=3)
    self.volver.grid(row=0,column=0) 
    self.cerrarTrato.grid(row=0,column=1, padx=10)
    self.filroO.grid(row=0,column=2)

def check_client(event):
    '''This method is used to check if the client exists or not'''
    #Gets the client's id
    id = Self.cIdE.get()
    #Gets the client using the id
    cliente = Self.manejador.get_clients(id)
    #If the client doesn't exist, an error message is shown
    if cliente == None:
        Self.cIdE.config(fg="red")
        Self.cIdE.delete(0, tk.END)
        tk.messagebox.showerror(title="Error", message="No se encontro cliente.")
    #If the client exists, the client's id is set to black color
    else:
        Self.cIdE.config(fg="black")
        Self.cNombreE.delete(0, tk.END)
        Self.cNombreE.insert(0, cliente[1]+' '+cliente[2]+" "+cliente[3])

def fix_data(result):
    result = list(result) # Convert tuple to list
    result[14]='Si' if result[13]==1 else 'No' #Mascotas
    result[16]='Si' if result[15]==1 else 'No' #Adjudicada
    result.pop(0) # Remove the first element
    return tuple(result)

def val(interesado, propietario):
    '''This method is used to check thet the interested client is not owner of the offer'''
    if interesado!='':
        if interesado == propietario:
            tk.messagebox.showerror(title="Error", message="El interesado no puede ser el propietario.")
            return False
        else:
            return True

def cerrarTrato_handler(self):
    '''This method is used to close a deal'''
    #get values from the UI
    id = self.oIdE.get()
    interesado = self.cNombreE.get()
    propietario = self.offersResult.item(id)['values'][1]
    #validate values
    if id != '' and val(interesado, propietario) and self.interesE.get() != '':
        #update oferta table
        self.manejador.consultar('UPDATE oferta SET disponibilidad = 0 WHERE idOferta = '+id+';')
        #if the offer is rent, insert the rent
        if(self.offersResult.item(id)['values'][4]=='Renta'):self.manejador.consultar('INSERT INTO rentas (idOferta, idCliente, fechaInicio) VALUES ('+id+', '+self.cIdE.get()+', CURDATE());')
        #delete the offer from the table
        self.offersResult.delete(id)
      
def offerSearch(self):
    """Search for offers in the database and display the result on the GUI."""
    try:
        # Search for offers in the database.
        offers= filterOffers(self)
        # Remove all previous search results from the GUI.
        for i in self.offersResult.get_children():
            self.offersResult.delete(i)
        # Add the found offers to the GUI.
        for offer in offers:
            # Convert the offer to a format that can be displayed on the GUI.
            offer = fix_data(offer)
            # Store the offer in the dictionary for later use.
            self.data[offer[0]] = offer
            # Add the offer to the GUI.
            self.offersResult.insert("", tk.END, iid=offer[0], values = tuple([offer[i] for i in self.index]))
    except Exception as e:
        print(e)

def filterOffers(self):
    #Get the values from the entries
    prop = {"t.tipo": self.tipoE.get(),"p.amueblada":self.amuebladaE.get(), "p.numRecamaras":str(self.numRecamarasE.get()), "p.numNiveles":str(self.numNivelesE.get()), 
            "p.numBaños":str(self.numBañosE.get()), "p.mascotas":str(self.mascotasE.get()), "p.posesion":self.posesionE.get(), "p.adjudicion":str(self.adjE.get())}
    oferta = {"o.estado":self.estadoE.get(),  "o.moneda":self.monedaE.get(),  "precioL":self.rangeE1.get(), "precioH":self.rangeE2.get()}
    #Set the tables and the keys
    tables = (['oferta', oferta], ['propiedad', prop])
    strings = ["t.tipo", "p.amueblada", "p.posesion", "o.estado", "o.moneda"]
    #Create the query
    query = 'SELECT o.disponibilidad, o.idOferta, CONCAT(c.nombre, \" \", c.apellidoP, \" \", c.apellidoM), p.direccion, t.tipo, o.estado, o.moneda, o.precio, p.superficieT, p.superficieC, p.amueblada, p.numRecamaras, p.numBaños, p.numNiveles, p.mascotas, p.posesion, p.adjudicion FROM cliente as c INNER JOIN propiedad as p ON c.idCliente = p.propietario INNER JOIN tipospropiedad as t ON p.idTipo = t.idTipo INNER JOIN oferta as o ON o.idOferta = p.idPropiedad WHERE '
    #Add the conditions to the query
    for table in tables:
        for key in table[1].keys():
            if str(table[1][key]) != "":
                if (key == "precioL" and table[1][key] != ""): query += 'o.precio >= '+table[1][key]
                elif (key == "precioH" and table[1][key] != ""): query += 'o.precio <= '+table[1][key]
                elif key not in strings: query += key+' = '+table[1][key]
                else: query += key+' = "'+table[1][key]+'"'
                query += ' AND '
    query = query[:-5]+';'
    #Return the result of the query
    return self.manejador.consultar(query)

def lookup(filters, name, entrie):
    """Add a filter to the filter dictionary, if entrie is an integer"""
    try:
        filters[name]=int(entrie)
        return filters
    except ValueError:
        return filters

# This code is called when the user clicks on the offersResult widget
def O_event_handler(event):
    # Check if the mouse click is on the separator line between the columns
    if Self.offersResult.identify_region(event.x, event.y) == "separator":
        # If so, return "break" to stop the event from being passed to other widgets
        return "break"
    # Check if the mouse click is on a cell in the offersResult widget
    if Self.offersResult.identify_region(event.x, event.y) == "cell":
        # If so, clear the contents of the oIdE entry widget
        Self.oIdE.delete(0,tk.END)
        # Then insert the id of the offer clicked on in the offersResult widget into the oIdE entry widget
        Self.oIdE.insert(0,Self.offersResult.focus())
        # Try to display the info of the offer clicked on in the offersResult widget
        try:
            offerInfo.info(data = Self.data[int(Self.offersResult.focus())])
        except:
            pass # If there is an error, ignore it