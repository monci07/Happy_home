import tkinter as tk
from tkinter import messagebox
from interface import *


class offerInsert(tk.Toplevel):
    
    def __init__(self, client = None, server = None):
        ''' window for adding a offer '''
        global Self
        bSize = [1, 10]
        tSize = [8, 25]
        tk.Toplevel.__init__(self)
        self.title("Happy home - New Offer")
        self.geometry(newOffer)
        self.resizable(False,False)
        self.iconbitmap("home.ico")
        self.manejador = server
        aux = self.manejador.get_clients(client) if client != None else None

        config_grid(self,[[i,1] for i in range(0,21)], [[i,1] for i in range(0,4)])

        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        #############################################################
        ##--------------------Datos del cliente--------------------##
        #############################################################

        self.cliente = tk.Label(self, text = "Cliente: ", font = tSize[0], pady = 3)
        self.idClienteL = tk.Label(self, text = "ID Cliente: ", font = tSize[0])
        self.nombreL = tk.Label(self, text="Nombre: ", font= tSize[0])
        self.apellidosL = tk.Label(self, text="Apellido(s): ", font= tSize[0])

        self.idClienteE = tk.Entry(self, font = tSize[0], width=tSize[1]-20, validate = 'key', validatecommand = vcmd)
        self.idClienteE.bind("<FocusOut>", self.check_client)
        self.nombreE = tk.Entry(self, font = tSize[0], width=tSize[1]) #, state = "disabled"
        self.apellidosE = tk.Entry(self, font = tSize[0], width=tSize[1])
        
        if aux!= None:
            self.idClienteE.insert(0, aux[0])
            self.nombreE.insert(0, aux[1])
            self.apellidosE.insert(0, aux[2]+" "+aux[3])
        
        self.cliente.grid(column=0, row=0, sticky=tk.W)

        grid_positioning(1,
                         [[self.idClienteL, [self.idClienteE],3], 
                          [self.nombreL, [self.nombreE],3], 
                          [self.apellidosL, [self.apellidosE],3]])

        #############################################################
        ##------------------Datos de la propiedad------------------##
        #############################################################
        
        self.propiedad = tk.Label(self, text = "Propiedad: ", font = tSize[0], pady = 3)
        self.tipoL = tk.Label(self, text="Tipo: ", font= tSize[0])
        self.direccionL = tk.Label(self, text="Direccion: ", font= tSize[0])
        self.superficieTL = tk.Label(self, text="Superficie terreno(m2): ", font= tSize[0])
        self.superficieCL = tk.Label(self, text="Superficie construccion(m2): ", font= tSize[0])
        self.amuebladaL = tk.Label(self, text="Amueblada: ", font= tSize[0])
        self.numRecamarasL = tk.Label(self, text="Numero de recamaras: ", font= tSize[0])
        self.numBañosL = tk.Label(self, text="Numero de baños: ", font= tSize[0])
        self.numNivelesL = tk.Label(self, text="Numero de niveles: ", font= tSize[0])
        self.mascotasL = tk.Label(self, text="Mascotas: ", font= tSize[0])
        self.posesionL = tk.Label(self, text="Posesion: ", font=tSize[0])
        self.adjudL= tk.Label(self, text="¿Adjudicada?: ", font= tSize[0])

        tiposP = [item for item in self.manejador.get_tipos()]
        self.tipoE = tk.StringVar(self)
        self.tipo = tk.OptionMenu(self, self.tipoE, *tiposP)
        self.tipo.config(font=tSize[0])
        menu = self.nametowidget(self.tipo.menuname)
        menu.config(font=tSize[0])
        
        self.direccionE = tk.Entry(self, font = tSize[0], width=tSize[1])
        self.superficieTE = tk.Entry(self, font = tSize[0], width=tSize[1]-15, validate = 'key', validatecommand = vcmd)
        self.superficieCE = tk.Entry(self, font = tSize[0], width=tSize[1]-15, validate = 'key', validatecommand = vcmd)

        self.amuebladaE = tk.StringVar(value="Si")
        self.amuebladaEO1= tk.Radiobutton(self, 
               text="Si",
               variable=self.amuebladaE, 
               value="Si",
               font = tSize[0])
        self.amuebladaEO2= tk.Radiobutton(self,
                text="No",
                variable=self.amuebladaE,
                value="No",
                font = tSize[0])
        self.amuebladaEO3= tk.Radiobutton(self,
                text="Semi",
                variable=self.amuebladaE, 
                value="Semi",
                font = tSize[0])

        self.numRecamarasE = tk.Scale(self, from_=1, to=20, orient=tk.HORIZONTAL, font = tSize[0], width=tSize[1])
        self.numBañosE = tk.Scale(self, from_=1, to=20, orient=tk.HORIZONTAL, font = tSize[0], width=tSize[1])
        self.numNivelesE = tk.Scale(self, from_=1, to=10, orient=tk.HORIZONTAL, font = tSize[0], width=tSize[1])
        self.mascotasE = tk.IntVar()
        self.mascotasEO1= tk.Radiobutton(self,
                text="Si",
                variable=self.mascotasE,
                value=1,
                font = tSize[0])
        self.mascotasEO2= tk.Radiobutton(self,
                text="No",
                variable=self.mascotasE,
                value=0,
                font = tSize[0])

        self.posesionE = tk.StringVar()
        self.posesionT = tk.OptionMenu(self, self.posesionE, "Regular", "Irregular")
        self.posesionT.config(font=tSize[0])
        menu = self.nametowidget(self.posesionT.menuname)
        menu.config(font=tSize[0])

        self.adjE = tk.IntVar()
        self.adjEO1= tk.Radiobutton(self,
                text="Si",
                variable=self.adjE,
                value=1,
                font = tSize[0])
        self.adjEO2= tk.Radiobutton(self,
                text="No",
                variable=self.adjE,
                value=0,
                font = tSize[0])


        self.propiedad.grid(column=0, row=4, sticky=tk.W)

        grid_positioning(5,
            [[self.tipoL, [self.tipo], 3],
            [self.direccionL, [self.direccionE], 3],
            [self.superficieTL, [self.superficieTE], 3],
            [self.superficieCL, [self.superficieCE], 3],
            [self.amuebladaL, [self.amuebladaEO1, self.amuebladaEO2, self.amuebladaEO3], 1],
            [self.numRecamarasL, [self.numRecamarasE], 3],
            [self.numBañosL, [self.numBañosE], 3],
            [self.numNivelesL, [self.numNivelesE], 3],
            [self.mascotasL, [self.mascotasEO1, self.mascotasEO2], 1],
            [self.posesionL, [self.posesionT], 3],
            [self.adjudL, [self.adjEO1, self.adjEO2], 1]])


        ##############################################################
        ##--------------------Datos de la oferta--------------------##
        ##############################################################
        self.oferta = tk.Label(self, text="Oferta: ", font = tSize[0], pady = 3)
        self.estadoL = tk.Label(self, text="Estado: ", font= tSize[0])
        self.monedaL = tk.Label(self, text="Moneda: ", font= tSize[0])
        self.precioL = tk.Label(self, text="Precio: ", font= tSize[0])

        self.estadoE = tk.StringVar(self)
        self.estado = tk.OptionMenu(self, self.estadoE, "Renta", "Venta")
        self.estado.config(font = tSize[0])
        menu = self.nametowidget(self.estado.menuname)
        menu.config(font=tSize[0])

        self.monedaE = tk.StringVar(self)
        self.moneda = tk.OptionMenu(self, self.monedaE, "Dolares", "Pesos")
        self.moneda.config(font = tSize[0])
        menu = self.nametowidget(self.moneda.menuname)
        menu.config(font=tSize[0])

        self.precioE = tk.Entry(self, font = tSize[0], width=tSize[1]-15, validate = 'key', validatecommand = vcmd)

        self.oferta.grid(column=0, row=17, sticky=tk.W)

        grid_positioning(18,
            [[self.estadoL, [self.estado], 3],
            [self.monedaL, [self.moneda], 3],
            [self.precioL, [self.precioE], 3]])

        self.addOfferB= tk.Button(self, text = "Añadir", command=self.addOffer, height=bSize[0], width=bSize[1])
        self.addOfferB.grid(column=0, row=21, columnspan=4, pady = 10)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grab_set()
        self.focus

    ##############################################################
    ##---------------------Funciones de la GUI------------------##
    ##############################################################
            

    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed=='': return True
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    ##############################################################
    ##---------------Funciones de funcionamiento----------------##
    ##############################################################
    def check_client(self, event):
        id = self.idClienteE.get()
        try:cliente = self.manejador.get_clients(id)
        except:cliente = None
        if cliente == None:
            self.idClienteE.config(fg="red")
            self.idClienteE.delete(0, tk.END)
            tk.messagebox.showerror(title="Error", message="No se encontro cliente.")

        elif self.nombreE.get() == '' and self.apellidosE.get() == '':
            self.idClienteE.config(fg="black")
            self.nombreE.insert(0, cliente[1])
            self.apellidosE.insert(0, cliente[2]+" "+cliente[3])

    def addOffer(self):
        try:
            cliente = (self.idClienteE.get())
            propiedad = {"tipo":list(self.tipoE.get())[1], "direccion":self.direccionE.get(), "superficieT":(self.superficieTE.get()), "superficieC":(self.superficieCE.get()), 
                         "amueblada":self.amuebladaE.get(), "numRecamaras":str(self.numRecamarasE.get()), "numNiveles":str(self.numNivelesE.get()), "numBaños":str(self.numBañosE.get()), 
                         "mascotas":str(self.mascotasE.get()), "posesion":self.posesionE.get(), "adjunto":str(self.adjE.get())}
            oferta = {"estado":self.estadoE.get(), 
                      "moneda":self.monedaE.get(), 
                      "precio":self.precioE.get()}
            print(self.manejador.insert_offer(cliente, propiedad, oferta))
            self.destroy()
        except Exception as e:
            tk.messagebox.showerror(title="Error", message="Faltaron campos por llenar.")
            print(e)
            

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Quieres salir?"):
            self.destroy()
    
    def check_widget(self, lists):
        for item in lists.values():
            if item == "": return False
            elif item == 0: return False
        return True