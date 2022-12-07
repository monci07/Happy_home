import tkinter as tk
from tkinter import ttk
from interface import *

Self = 0

def offerShowMenu(self):
    global Self
    Self = self
    mainMenuInvisible(self)
    self.geometry(searchSize)
    self.title("Happy home - Offers Search")
    config_grid(self,[[i,0] for i in range(0,4)], [[i,0] for i in range(0,3)])

    self.interesado = tk.Label(self, text = "Interesado:", font =self.tSize[0])

    self.cIdL = tk.Label(self, text = "ID", font =self.tSize[0])
    self.cIdE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    self.cIdE.bind("<FocusOut>", check_client)

    self.cNombreL = tk.Label(self, text = "Nombre", font =self.tSize[0])
    self.cNombreE = tk.Entry(self, font =self.tSize[0])
    
    #################################################
    
    self.oferta = tk.Label(self, text = "Oferta:", font =self.tSize[0])
    
    self.oIdL = tk.Label(self, text = "ID:", font =self.tSize[0])
    self.oIdE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1])
    
    self.interesL = tk.Label(self, text = "Interes:", font =self.tSize[0])
    self.interesE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    #################################################
    
    self.filtros = tk.Label(self, text = "Filtros:", font =self.tSize[0])        
    
    self.monedaL = tk.Label(self, text = "Moneda:", font =self.tSize[0])
    self.monedaE = tk.StringVar()
    self.monedaT = tk.OptionMenu(self, self.monedaE, "Dolares", "Pesos")
    self.monedaT.config(font=self.tSize[0])
    menu = self.nametowidget(self.monedaT.menuname)
    menu.config(font=self.tSize[0])
    
    self.rangeL = tk.Label(self, text = "Rango P.:", font =self.tSize[0])
    self.rangeE1 = tk.Entry(self, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    self.rangeE2 = tk.Entry(self, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.estadoL = tk.Label(self, text = "Estado:", font =self.tSize[0])
    self.estadoE = tk.StringVar()
    self.estadoT = tk.OptionMenu(self, self.estadoE, "Venta", "Renta")
    self.estadoT.config(font=self.tSize[0])
    menu = self.nametowidget(self.estadoT.menuname)
    menu.config(font=self.tSize[0])
    
    self.tipoL = tk.Label(self, text = "Tipo:", font =self.tSize[0])
    tiposP = [item[1] for item in self.manejador.get_tipos()]
    self.tipoE = tk.StringVar()
    self.tipo = tk.OptionMenu(self, self.tipoE, *tiposP)
    self.tipo.config(font=self.tSize[0])
    menu = self.nametowidget(self.tipo.menuname)
    menu.config(font=self.tSize[0])
    
    self.amuebladoL = tk.Label(self, text = "Amueblada:", font =self.tSize[0])
    self.amuebladaE = tk.StringVar()
    self.amueblado = tk.OptionMenu(self, self.amuebladaE, "Si", "No", "Semi")
    self.amueblado.config(font=self.tSize[0])
    menu = self.nametowidget(self.amueblado.menuname)
    menu.config(font=self.tSize[0])        
    
    self.numRecamarasL = tk.Label(self, text = "Num. Recamaras:", font =self.tSize[0])
    self.numRecamarasE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.numBañosL = tk.Label(self, text = "Num. Baños:", font =self.tSize[0])
    self.numBañosE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.numNivelesL = tk.Label(self, text = "Num. Niveles:", font =self.tSize[0])
    self.numNivelesE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    
    self.mascotasL = tk.Label(self, text = "Mascotas:", font =self.tSize[0])
    self.mascotasE = tk.IntVar(value = 2)
    self.mascotasEO1= tk.Radiobutton(self,
            text="Si",
            variable=self.mascotasE,
            value=1,
            font = self.tSize[0])
    self.mascotasEO2= tk.Radiobutton(self,
            text="No",
            variable=self.mascotasE,
            value=0,
            font = self.tSize[0])        
    
    self.posesionL = tk.Label(self, text = "Posesion:", font =self.tSize[0])
    self.posesionE = tk.StringVar(self)
    self.posesionT = tk.OptionMenu(self, self.posesionE, "Regular", "Irregular")
    self.posesionT.config(font=self.tSize[0])
    menu = self.nametowidget(self.posesionT.menuname)
    menu.config(font=self.tSize[0])
    
    self.adjL = tk.Label(self, text = "Adjudicada:", font =self.tSize[0])
    self.adjE = tk.IntVar(value = 2)
    self.adjEO1= tk.Radiobutton(self,
            text="Si",
            variable=self.adjE,
            value=1,
            font = self.tSize[0])
    self.adjEO2= tk.Radiobutton(self,
            text="No",
            variable=self.adjE,
            value=0,
            font = self.tSize[0])
    
    #################################################

    self.offersResult = ttk.Treeview(self, 
                                        columns = ("ID", "Propietario", "Direccion", "Tipo", "Estado", "Moneda", "Precio", "S. Terreno(m2)", "S. Constr.(m2)","Amueblado", "Recamaras", "Baños", "Niveles", "Mascotas", "Posesion", "Adjudicada"), 
                                        show = "headings",
                                        height = 30,
                                        selectmode="browse")                            
    style = ttk.Style()
    style.configure("Treeview", font=self.tSize[0])
    style.configure("Treeview.Heading", font=self.tSize[0])
    tree_handler(self.offersResult,[50, #"ID"
                                    220, #"Propietario"
                                    400, #"Direccion"
                                    150, #"Tipo"
                                    100, #"Estado"
                                    150, #"Moneda"
                                    150, #"Precio"
                                    150, #"S. Terreno(m2)"
                                    150, #"S. Constr.(m2)"
                                    105, #"Amueblado"
                                    105, #"Recamaras"
                                    90, #"Baños"
                                    90, #"Niveles"
                                    100, #"Mascotas"
                                    110, #"Posesion"
                                    110]) #"Adjudicada"        
    
    verscrlbar = ttk.Scrollbar(self, orient ="vertical", command = self.offersResult.yview)
    horzscrlbar = ttk.Scrollbar(self, orient ="horizontal", command = self.offersResult.xview)
    self.offersResult.bind('<Button-1>', O_event_handler)        
    

    f1 = tk.Frame(self)
    self.filroO = tk.Button(f1, text = "Filtrar", font =self.tSize[0], command = lambda: offerSearch(self), width=10)
    self.cerrarTrato = tk.Button(f1, text = "Cerrar Trato", font =self.tSize[0], command = lambda: cerrarTrato_handler(self), width=10)
    self.volver = tk.Button(f1, text = "Volver", font =self.tSize[0], command = lambda:buscarOMenuInvisible(self), width=10)
    
    self.buscarOMenu = [self.interesado,
                        self.cIdL, self.cIdE,
                        self.cNombreL, self.cNombreE,
                        self.oferta,
                        self.oIdL, self.oIdE,
                        self.interesL, self.interesE,
                        self.filtros,
                        self.monedaL, self.monedaT,
                        self.rangeL, self.rangeE1, self.rangeE2,
                        self.tipoL, self.tipo,
                        self.estadoL, self.estadoT,
                        self.amuebladoL, self.amueblado,
                        self.numRecamarasL, self.numRecamarasE,
                        self.numBañosL, self.numBañosE,
                        self.numNivelesL, self.numNivelesE,
                        self.mascotasL, self.mascotasEO1, self.mascotasEO2,
                        self.posesionL, self.posesionT,
                        self.adjL, self.adjEO1, self.adjEO2,
                        self.offersResult, verscrlbar, horzscrlbar,
                        f1, self.cerrarTrato, self.filroO , self.volver]        
    
    self.interesado.grid(column=0, row=0, sticky=tk.W)
    
    grid_positioning(1,
                        [[self.cIdL, [self.cIdE], 3],
                        [self.cNombreL, [self.cNombreE], 3]])
    
    self.oferta.grid(column=0, row=3, sticky=tk.W)
    
    grid_positioning(4,
                        [[self.oIdL, [self.oIdE], 3],
                        [self.interesL, [self.interesE], 3]])
    
    self.filtros.grid(column=0, row=7, sticky=tk.W)
    
    grid_positioning(8,
                        [[self.monedaL, [self.monedaT], 3],
                        [self.rangeL, [self.rangeE1, self.rangeE2], 1],
                        [self.tipoL, [self.tipo], 3],
                        [self.estadoL, [self.estadoT], 3],
                        [self.amuebladoL, [self.amueblado], 1],
                        [self.numRecamarasL, [self.numRecamarasE], 3],
                        [self.numBañosL, [self.numBañosE], 3],
                        [self.numNivelesL, [self.numNivelesE], 3],
                        [self.mascotasL, [self.mascotasEO1, self.mascotasEO2], 1],
                        [self.posesionL, [self.posesionT], 3],
                        [self.adjL, [self.adjEO1, self.adjEO2], 1]])        
    
    self.offersResult.grid(column=3, row=0, rowspan=100)        
    verscrlbar.grid(column=3, row=0, rowspan=100, sticky='nse')
    self.offersResult.configure(yscrollcommand = verscrlbar.set)
    horzscrlbar.grid(column=3, row=99, columnspan=100, sticky='ews')
    self.offersResult.configure(xscrollcommand = horzscrlbar.set)
    
    for offer in self.manejador.get_ofertas():
        if offer[0] != 0:
            data = fix_data(offer)
            self.offersResult.insert("", tk.END, iid=data[0], values = data)            
    
    f1.grid(column=0, row=19, columnspan=3)
    self.volver.grid(row=0,column=0)
    self.cerrarTrato.grid(row=0,column=1, padx=10)
    self.filroO.grid(row=0,column=2)
    #self.volver.grid(column=0, row=19, sticky='ns')
    #self.cerrarTrato.grid(column=1, row=19, sticky='ns')
    #self.filroO.grid(column=2, row=19, sticky='ns')

def check_client(event):
    id = Self.cIdE.get()
    cliente = Self.manejador.get_clients(id)
    if cliente == None:
        Self.cIdE.config(fg="red")
        Self.cIdE.delete(0, tk.END)
        tk.messagebox.showerror(title="Error", message="No se encontro cliente.")
    else:
        Self.cIdE.config(fg="black")
        Self.cNombreE.delete(0, tk.END)
        Self.cNombreE.insert(0, cliente[1]+' '+cliente[2]+" "+cliente[3])

def fix_data(result):
    result = list(result)
    result[14]='Si' if result[13]==1 else 'No' #Mascotas
    result[16]='Si' if result[15]==1 else 'No' #Adjudicada
    result.pop(0)
    return tuple(result)

def val(interesado, propietario):
    if interesado!='':
        if interesado == propietario:
            tk.messagebox.showerror(title="Error", message="El interesado no puede ser el propietario.")
            return False
        else:
            return True

def cerrarTrato_handler(self):
    id = self.oIdE.get()
    interesado = self.cNombreE.get()
    propietario = self.offersResult.item(id)['values'][1]
    if id != '' and val(interesado, propietario) and self.interesE.get() != '':
        self.manejador.consultar('UPDATE oferta SET disponibilidad = 0 WHERE idOferta = '+id+';')
        if(self.offersResult.item(id)['values'][4]=='Renta'):check_renta(self,id,self.cIdE.get())
        self.offersResult.delete(id)
      
def check_renta(self, idOferta, idCliente):
    print(self.manejador.consultar('INSERT INTO rentas (idOferta, idCliente, fechaInicio) VALUES ('+idOferta+', '+idCliente+', CURDATE());'))

def offerSearch(self):
    try:
        offers= filterOffers()
        for i in self.offersResult.get_children():
            self.offersResult.delete(i)
        for offer in offers:
            offer = fix_data(offer)
            self.offersResult.insert('', 'end', iid=offer[0], values = offer)
    except Exception as e:
        print(e)

def filterOffers():
    offer=[]
    offer.append('SELECT o.disponibilidad, o.idOferta, CONCAT(c.nombre, \" \", c.apellidoP, \" \", c.apellidoM), p.direccion, t.tipo, o.estado, o.moneda, o.precio, p.superficieT, p.superficieC, p.amueblada, p.numRecamaras, p.numBaños, p.numNiveles, p.mascotas, p.posesion, p.adjudicion FROM cliente as c INNER JOIN propiedad as p ON c.idCliente = p.propietario INNER JOIN tipospropiedad as t ON p.idTipo = t.idTipo INNER JOIN oferta as o ON o.idOferta = p.idPropiedad')
    if Self.monedaE.get() != '':
        offer.append(' o.moneda = \"'+Self.monedaE.get()+'\"')
    if Self.rangeE1.get() != '':
        offer.append(' o.precio >= ' + str(Self.rangeE1.get()))
    if Self.rangeE2.get() != '':
        offer.append(' o.precio <= ' + str(Self.rangeE2.get()))
    if Self.tipoE.get() != '':
        offer.append(' t.tipo = \"'+Self.tipoE.get()+'\"')
    if Self.estadoE.get() != '':
        offer.append(' o.estado = \"'+Self.estadoE.get()+'\"')
    if Self.amuebladaE.get() != '':
        offer.append(' p.amueblada = \"'+Self.amuebladaE.get()+'\"')
    if Self.numRecamarasE.get() != '':
        offer.append(' p.numRecamaras = '+(Self.numRecamarasE.get()))
    if Self.numBañosE.get() != '':
        offer.append(' p.numBaños = '+(Self.numBañosE.get()))
    if Self.numNivelesE.get() != '':
        offer.append(' p.numNiveles = '+(Self.numNivelesE.get()))
    if Self.mascotasE.get() != 2:
        offer.append(' p.mascotas = '+str(Self.mascotasE.get()))
    if Self.posesionE.get() != '':
        offer.append(' p.posesion = \"'+Self.posesionE.get()+'\"')
    if Self.adjE.get() != 2:
        offer.append(' p.adjudicion = '+str(Self.adjE.get()))
    query = offer[0]
    if len(offer) < 2:
        query += ';'
        return Self.manejador.consultar(query)
    else:
        query += ' WHERE'
        for f in range(1,len(offer)):
            query += offer[f]
            if f < len(offer)-1: query += ' AND'
        query += ';'
        return Self.manejador.consultar(query)

def lookup(filters, name, entrie):
    try:
        filters[name]=int(entrie)
        return filters
    except ValueError:
        return filters

def O_event_handler(event):
    if Self.offersResult.identify_region(event.x, event.y) == "separator":
        return "break"
    elif Self.offersResult.identify_region(event.x, event.y) == "cell":
        Self.oIdE.delete(0,tk.END)
        Self.oIdE.insert(0,Self.offersResult.focus())