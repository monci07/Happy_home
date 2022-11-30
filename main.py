import tkinter as tk
from tkinter import ttk
import client
import offer
import server
import pyperclip

class App(tk.Tk):
    
    bHeight = 5
    mainSize = "1000x300"
    searchSize = "1325x635"

    def __init__(self):
        super().__init__()
        global bHeight
        global mainMenu
        global mainSize

        self.mainMenu=[]
        self.buscarCMenu=[]
        self.buscarRMenu=[]
        self.buscarOMenu=[]

        self.bSize = [1, 10]
        self.tSize = [10, 20]
        self.gSize = [0,1]

        self.title("Happy home - Main Menu")
        self.geometry(self.mainSize)
        self.resizable(False,False)

        self.vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.manejador = server.serverCom()

        self.offersResult= tk.Button(self, text = "Buscar ofertas", 
                                     font =self.tSize[0], command = self.offerShowMenu, 
                                     height=self.bHeight, width=15)
        self.offersAdd= tk.Button(self, text = "Agregar ofertas", 
                                  font =self.tSize[0], command = self.addOffer, 
                                  height=self.bHeight, width=15)
        self.clientsSearch= tk.Button(self, text = "Buscar clientes", 
                                      font =self.tSize[0], command = self.clientShowMenu, 
                                      height=self.bHeight, width=15)
        self.clientsAdd= tk.Button(self, text = "Agregar clientes", 
                                      font =self.tSize[0], command = self.addClient, 
                                      height=self.bHeight, width=15)
        self.rentsSearch= tk.Button(self, text = "Buscar rentas", 
                                    font =self.tSize[0], command = self.rentShowMenu, 
                                    height=self.bHeight, width=15)
        self.mainMenu = [self.offersResult, self.offersAdd, self.clientsSearch, self.clientsAdd, self.rentsSearch]

        self.config_grid([[i, 1] for i in range(0,2)], [[i, 1] for i in range(0, 5)])

        
        self.offersResult.grid(column=0, row=0)
        self.clientsSearch.grid(column=2, row=0)
        self.rentsSearch.grid(column=4, row=0)
        self.offersAdd.grid(column=1, row=1)
        self.clientsAdd.grid(column=3, row=1)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def config_grid(self, rows: list, columns: list):
        for i in range(len(rows)):
            self.rowconfigure(rows[i][0], weight=rows[i][1])
        for i in range(len(columns)):
            self.columnconfigure(columns[i][0], weight=columns[i][1])
    
    def on_closing(self):
        self.manejador.close_connection()
        self.destroy()

###############################################
#------------------windows--------------------#
###############################################
    def addClient(self):
        self.newWindow = client.userInsert(self.manejador)
    
    def addOffer(self):
        self.newWindow = offer.offerInsert(server = self.manejador)

###############################################
#----------------visibility-------------------#
###############################################
    def mainMenuInvisible(self):
        for item in self.mainMenu:
            item.grid_forget()

    def mainMenuVisible(self):
        global mainSize
        self.geometry(self.mainSize)
        self.title("Happy home - Main Menu")
        self.config_grid([[i, 1] for i in range(0,2)], [[i, 1] for i in range(0, 5)])
        for i in range(len(self.mainMenu)):
            aux = 1 if (i+1)%2 > 0 else 2
            self.mainMenu[i].grid(column=i, row=aux)

    def buscarOMenuInvisible(self):
        for item in self.buscarOMenu:
            item.grid_forget()
        self.mainMenuVisible()
    
    def buscarCMenuInvisible(self):
        for item in self.buscarCMenu:
            item.grid_forget()
        self.mainMenuVisible()

    def buscarRMenuInvisible(self):
        for item in self.buscarRMenu:
            item.grid_forget()
        self.mainMenuVisible()

###############################################
#------------------menus----------------------#
###############################################
        
    def grid_positioning(self, init=int, list=list):
        for i in range(len(list)):
            list[i][0].grid(column=0, row=i+init, sticky=tk.E)
            for j in range(len(list[i][1])):
                list[i][1][j].grid(column=j+1, row=i+init, sticky=tk.W, columnspan=list[i][2])

    def tree_handler(self, tree=ttk.Treeview, lWith=list):
        for i in range(len(tree['columns'])):
            tree.column(tree['columns'][i],anchor=tk.CENTER, width=lWith[i])
            tree.heading(tree['columns'][i], text=tree['columns'][i])

    def C_event_handler(self,event):
        if self.clientsResult.identify_region(event.x, event.y) == "separator":
            return "break"
        elif self.clientsResult.identify_region(event.x, event.y) == "cell":
            curItem = self.clientsResult.focus()
            pyperclip.copy(curItem)

    def O_event_handler(self,event):
        if self.offersResult.identify_region(event.x, event.y) == "separator":
            return "break"
        elif self.offersResult.identify_region(event.x, event.y) == "cell":
            self.oIdE.delete(0,tk.END)
            self.oIdE.insert(0,self.offersResult.focus())
            
        #################################################
        #---------------------Offers--------------------#
        #################################################
    def offerShowMenu(self):
        global bHeight
        global searchSize
        self.mainMenuInvisible()
        self.geometry(self.searchSize)
        self.title("Happy home - Offers Search")
        self.config_grid([[i,0] for i in range(0,4)], [[i,0] for i in range(0,3)])


        self.interesado = tk.Label(self, text = "Interesado:", font =self.tSize[0])

        self.cIdL = tk.Label(self, text = "ID", font =self.tSize[0])
        self.cIdE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)
        self.cIdE.bind("<FocusOut>", self.check_client)

        self.cNombreL = tk.Label(self, text = "Nombre", font =self.tSize[0])
        self.cNombreE = tk.Entry(self, font =self.tSize[0])

        #################################################

        self.oferta = tk.Label(self, text = "Oferta:", font =self.tSize[0])

        self.oIdL = tk.Label(self, text = "ID:", font =self.tSize[0])
        self.oIdE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10)
        self.interesL = tk.Label(self, text = "Interes:", font =self.tSize[0])
        self.interesE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)

        #################################################

        self.filtros = tk.Label(self, text = "Filtros:", font =self.tSize[0])
        
        self.rangeL = tk.Label(self, text = "Rango P.:", font =self.tSize[0])
        self.rangeE1 = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)
        self.rangeE2 = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)

        self.estadoL = tk.Label(self, text = "Estado:", font =self.tSize[0])
        self.estadoE = tk.StringVar(self)
        self.estadoT = tk.OptionMenu(self, self.estadoE, "Venta", "Renta")
        self.estadoT.config(font=self.tSize[0])
        menu = self.nametowidget(self.estadoT.menuname)
        menu.config(font=self.tSize[0])

        self.tipoL = tk.Label(self, text = "Tipo:", font =self.tSize[0])
        tiposP = [item for item in self.manejador.get_tipos()]
        self.tipoE = tk.StringVar(self)
        self.tipo = tk.OptionMenu(self, self.tipoE, *tiposP)
        self.tipo.config(font=self.tSize[0])
        menu = self.nametowidget(self.tipo.menuname)
        menu.config(font=self.tSize[0])

        self.amuebladoL = tk.Label(self, text = "Amueblada:", font =self.tSize[0])
        self.amuebladaE = tk.StringVar(self)
        self.amueblado = tk.OptionMenu(self, self.amuebladaE, "Si", "No", "Semi")
        self.amueblado.config(font=self.tSize[0])
        menu = self.nametowidget(self.amueblado.menuname)
        menu.config(font=self.tSize[0])
        
        self.numRecamarasL = tk.Label(self, text = "Num. Recamaras:", font =self.tSize[0])
        self.numRecamarasE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)

        self.numBañosL = tk.Label(self, text = "Num. Baños:", font =self.tSize[0])
        self.numBañosE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)

        self.numNivelesL = tk.Label(self, text = "Num. Niveles:", font =self.tSize[0])
        self.numNivelesE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)

        self.mascotasL = tk.Label(self, text = "Mascotas:", font =self.tSize[0])
        self.mascotasE = tk.IntVar()
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
        self.adjE = tk.IntVar()
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



        self.offersResult = ttk.Treeview(self, 
                                         columns = ("ID", "Propietario", "Direccion", "Tipo", "Estado", "Moneda", "Precio", "S. Terreno(m2)", "S. Constr.(m2)","Amueblado", "Recamaras", "Baños", "Niveles", "Mascotas", "Posesion", "Adjudicada"), 
                                         show = "headings",
                                         height = 30,
                                         selectmode="browse")
                            
        style = ttk.Style()
        style.configure("Treeview", font=self.tSize[0])
        style.configure("Treeview.Heading", font=self.tSize[0])

        self.tree_handler(self.offersResult,[50, #"ID"
                                             220, #"Propietario"
                                             350, #"Direccion"
                                             100, #"Tipo"
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

        self.offersResult.bind('<Button-1>', self.O_event_handler)
        
        self.testButton = tk.Button(self, text = "Test", font =self.tSize[0], command = self.buscarOMenuInvisible, height=self.bHeight-5, width=10)

        self.buscarOMenu = [self.interesado,
                            self.cIdL, self.cIdE,
                            self.cNombreL, self.cNombreE,
                            self.oferta,
                            self.oIdL, self.oIdE,
                            self.interesL, self.interesE,
                            self.filtros,
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
                            self.testButton]
        
        self.interesado.grid(column=0, row=0, sticky=tk.W)
        self.grid_positioning(1,
                              [[self.cIdL, [self.cIdE], 3],
                               [self.cNombreL, [self.cNombreE], 3]])
        self.oferta.grid(column=0, row=3, sticky=tk.W)
        self.grid_positioning(4,
                             [[self.oIdL, [self.oIdE], 3],
                              [self.interesL, [self.interesE], 3]])
        self.filtros.grid(column=0, row=7, sticky=tk.W)
        self.grid_positioning(8,
                             [[self.rangeL, [self.rangeE1, self.rangeE2], 1],
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
            data = self.fix_data(offer)
            self.offersResult.insert("", tk.END, iid=data[0], values = data)
            


        self.testButton.grid(column=0, row=19, sticky=tk.W)

    def check_client(self,event):
        id = self.cIdE.get()
        cliente = self.manejador.get_clients(id)
        if cliente == None:
            self.cIdE.config(fg="red")
            self.cIdE.delete(0, tk.END)
            tk.messagebox.showerror(title="Error", message="No se encontro cliente.")

        elif self.cNombreE.get() == '':
            self.cIdE.config(fg="black")
            self.cNombreE.insert(0, cliente[1]+' '+cliente[2]+" "+cliente[3])

    def fix_data(self, result):
        r = ()
        if result[16]!= 0: #Disponible
            r+=(result[18],) #ID oferta
            r+=(result[0] + ' ' + result[1] + ' ' + result[2],) #Nombre cliente
            r+=(result[6],) #Direccion
            r+=(result[17],) #Tipo
            r+=(result[20],) #Estado
            r+=(result[21],) #Moneda
            r+=(result[22],) #Precio
            r+=(result[7],) #S. Terreno(m2)
            r+=(result[8],) #S. Constr.(m2)
            r+=(result[9],) #Amueblado
            r+=(result[10],) #Recamaras
            r+=(result[12],) #Baños
            r+=(result[11],) #Niveles
            r+=('Si' if result[13]==1 else 'No',) #Mascotas
            r+=(result[14],) #Posesion
            r+=('Si' if result[15]==1 else 'No',) #Adjudicada
        return r

        #################################################
        #---------------------Client--------------------#
        #################################################

    def clientShowMenu(self):
        global bHeight
        global searchSize
        self.mainMenuInvisible()
        self.geometry(self.searchSize)
        self.title("Happy home - Client search")
        self.config_grid([[i,0] for i in range(0,4)], [[i,0] for i in range(0,3)])



        self.cIdL = tk.Label(self, text = "ID", font =self.tSize[0])
        self.cIdE = tk.Entry(self, font =self.tSize[0], width=self.tSize[1]-10, validate = 'key', validatecommand = self.vcmd)

        self.cNombreL = tk.Label(self, text = "Nombre", font =self.tSize[0])
        #TODO: hacerlo alphabetico
        self.cNombreE = tk.Entry(self, font =self.tSize[0])

        self.cApellidoL = tk.Label(self, text = "Apellido", font =self.tSize[0])
        #TODO: hacerlo alphabetico
        self.cApellidoE = tk.Entry(self, font =self.tSize[0])

        self.filtro = tk.Button(self, text = "Filtrar", font =self.tSize[0], command = self.filterClient, height=self.bHeight-15, width=15)
        self.testButton = tk.Button(self, text = "Volver", font =self.tSize[0], command = self.buscarCMenuInvisible, height=self.bHeight-15, width=15)

        self.clientsResult = ttk.Treeview(self, 
                                          columns = ("ID", "Nombre", "Apellido P.", "Apellido M.", "Fecha R.", "Telefono", "Correo"), 
                                          show = "headings",
                                          height = 30)
        style = ttk.Style()
        style.configure("Treeview", font=self.tSize[0])
        style.configure("Treeview.Heading", font=self.tSize[0])
        self.tree_handler(self.clientsResult, [80, 125, 125, 125, 125, 125, 300])
        
        for client in self.manejador.get_clients():
            self.clientsResult.insert('', 'end', iid=client[0], values = client)

        self.clientsResult.bind('<Button-1>', self.C_event_handler)


        self.grid_positioning(0,
                             [[self.cIdL, [self.cIdE], 1],
                              [self.cNombreL, [self.cNombreE], 1],
                              [self.cApellidoL, [self.cApellidoE], 1]])
        
        self.filtro.grid(column=0, row=3, columnspan=2)
        self.testButton.grid(column=0, row=4, columnspan=2)

        self.clientsResult.grid(column=2, row=0, rowspan=1000)
        verscrlbar = ttk.Scrollbar(self, orient ="vertical", command = self.clientsResult.yview)
        verscrlbar.grid(column=3, row=0, rowspan=1000, sticky='ns')
        self.clientsResult.configure(yscrollcommand = verscrlbar.set)


        self.buscarCMenu = [self.cIdL,self.cIdE,
                            self.cNombreL,self.cNombreE,
                            self.cApellidoL,self.cApellidoE,
                            self.filtro, self.testButton,
                            self.clientsResult]
    
    def clientSearch(self):
        id = self.cIdE.get()
        id = id if id != '' else 0
        clients=[]
        query = ''
        if id == 0:
            nombre = self.cNombreE.get()
            apellidos = self.cApellidoE.get()
            if nombre == '':
                apellidos = (apellidos + (' ')).split(" ")
                if apellidos[1]=='': query= 'select * from cliente where apellidoP LIKE \"%'+apellidos[0]+'%\";'
                else: query= 'select * from cliente where apellidoP LIKE \"%'+apellidos[0]+'%\" OR apellidoM LIKE \"%'+apellidos[1]+'%\";'
            elif apellidos == '':
                query = 'select * from cliente where nombre LIKE \"%'+nombre+'%\";'
            else:
                query = 'select * from cliente where nombre LIKE \"%'+nombre+'%\" OR apellidoP LIKE \"%'+apellidos[0]+'%\" OR apellidoM LIKE \"%'+apellidos[1]+'%\";'
        else:
            query = 'select * from cliente where idCliente = '+id+';'
        clients = self.manejador.consultar(query)
        return clients

    def filterClient(self):
        clients = self.clientSearch()
        for i in self.clientsResult.get_children():
                self.clientsResult.delete(i)
        if clients != []:
            for client in clients:
                self.clientsResult.insert('', 'end', iid=client[0], values = client)
        else:
            for client in self.manejador.get_clients():
                self.clientsResult.insert('', 'end', iid=client[0], values = client)


            #################################################
            #----------------------rent---------------------#
            #################################################
    def rentShowMenu(self):
        global bHeight
        global searchSize
        self.mainMenuInvisible()
        self.geometry(self.searchSize)
        
        self.testButton = tk.Button(self, text = "Test", font =self.tSize[0], command = self.buscarRMenuInvisible, height=self.bHeight, width=30)

        self.buscarRMenu = [self.testButton]

        for item in self.buscarRMenu:
            item.grid(column=1, row=1)

if __name__ == '__main__':
    #creacion de ventana principal
    app=App()
    app.mainloop()