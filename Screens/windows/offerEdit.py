import tkinter as tk
from tkinter import messagebox
from interface import *


class offerEdit(tk.Toplevel):
    
    def __init__(self, server = None):
        ''' window for adding a offer '''
        global Self
        bSize = [1, 10]
        tSize = [8, 25]
        super().__init__()
        self.title("Happy home - Offer Edit")
        self.geometry(editOffer)
        self.resizable(False,False)
        self.iconbitmap("home.ico")
        self.manejador = server
        #aux = self.manejador.get_clients(client) if client != None else None

        config_grid(self,[[i,1] for i in range(0,21)], [[i,1] for i in range(0,3)])

        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.idOfertaL = tk.Label(self, text="ID Oferta: ", font= tSize[0])
        self.idOfertaE = tk.Entry(self, font = tSize[0], width=tSize[1]-20, validate = 'key', validatecommand = vcmd)
        self.idOfertaE.bind("<Return>", self.check_offer)

        self.idOfertaL.grid(column=0, row=0, sticky=tk.E)
        self.idOfertaE.grid(column=1, row=0, sticky=tk.W)
        #############################################################
        ##--------------------Datos del cliente--------------------##
        #############################################################

        self.cliente = tk.Label(self, text = "Cliente: ", font = tSize[0], pady = 3)
        self.idClienteL = tk.Label(self, text = "ID Cliente: ", font = tSize[0])
        self.nombreL = tk.Label(self, text="Nombre: ", font= tSize[0])
        self.apellidosL = tk.Label(self, text="Apellido(s): ", font= tSize[0])

        self.idClienteE = tk.Entry(self, font = tSize[0], width=tSize[1]-20, validate = 'key', validatecommand = vcmd)
        self.idClienteE.bind("<Return>", self.check_client)
        self.nombreE = tk.Entry(self, font = tSize[0], width=tSize[1], state = "disabled") #, state = "disabled"
        self.apellidosE = tk.Entry(self, font = tSize[0], width=tSize[1], state = "disabled")
        
        self.cliente.grid(column=0, row=1, sticky=tk.W)

        grid_positioning(2,
                         [[self.idClienteL, self.idClienteE], 
                          [self.nombreL, self.nombreE], 
                          [self.apellidosL, self.apellidosE]])

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

        self.tiposP = [item for item in self.manejador.get_tipos()]
        self.tipoE = tk.StringVar(self, value=self.tiposP[0])
        self.tipo = tk.OptionMenu(self, self.tipoE, *self.tiposP)
        self.tipo.config(font=tSize[0])
        menu = self.nametowidget(self.tipo.menuname)
        menu.config(font=tSize[0])
        
        self.direccionE = tk.Entry(self, font = tSize[0], width=tSize[1])
        self.superficieTE = tk.Entry(self, font = tSize[0], width=tSize[1]-15, validate = 'key', validatecommand = vcmd)
        self.superficieCE = tk.Entry(self, font = tSize[0], width=tSize[1]-15, validate = 'key', validatecommand = vcmd)

        frameEditO1 = tk.Frame(self)
        self.amuebladaE = tk.StringVar(value="Si")
        self.amuebladaEO1= tk.Radiobutton(frameEditO1, 
               text="Si",
               variable=self.amuebladaE, 
               value="Si",
               font = tSize[0])
        self.amuebladaEO2= tk.Radiobutton(frameEditO1,
                text="No",
                variable=self.amuebladaE,
                value="No",
                font = tSize[0])
        self.amuebladaEO3= tk.Radiobutton(frameEditO1,
                text="Semi",
                variable=self.amuebladaE, 
                value="Semi",
                font = tSize[0])
        self.amuebladaEO1.grid(row=0, sticky=tk.W)
        self.amuebladaEO2.grid(row=1, sticky=tk.W)
        self.amuebladaEO3.grid(row=2, sticky=tk.W)

        self.numRecamarasE = tk.Scale(self, from_=1, to=20, orient=tk.HORIZONTAL, font = tSize[0], width=tSize[1])
        self.numBañosE = tk.Scale(self, from_=1, to=20, orient=tk.HORIZONTAL, font = tSize[0], width=tSize[1])
        self.numNivelesE = tk.Scale(self, from_=1, to=10, orient=tk.HORIZONTAL, font = tSize[0], width=tSize[1])
        
        f2= tk.Frame(self)
        self.mascotasE = tk.IntVar(value = 1)
        self.mascotasEO1= tk.Radiobutton(f2,
                text="Si",
                variable=self.mascotasE,
                value=1,
                font = tSize[0])
        self.mascotasEO2= tk.Radiobutton(f2,
                text="No",
                variable=self.mascotasE,
                value=0,
                font = tSize[0])
        self.mascotasEO1.grid(row=0, sticky=tk.W)
        self.mascotasEO2.grid(row=1, sticky=tk.W)

        self.posesionE = tk.StringVar(value = "Regular")
        self.posesionT = tk.OptionMenu(self, self.posesionE, "Regular", "Irregular")
        self.posesionT.config(font=tSize[0])
        menu = self.nametowidget(self.posesionT.menuname)
        menu.config(font=tSize[0])

        f3 = tk.Frame(self)
        self.adjE = tk.IntVar(value = 1)
        self.adjEO1= tk.Radiobutton(f3,
                text="Si",
                variable=self.adjE,
                value=1,
                font = tSize[0])
        self.adjEO2= tk.Radiobutton(f3,
                text="No",
                variable=self.adjE,
                value=0,
                font = tSize[0])
        self.adjEO1.grid(row=0, sticky=tk.W)
        self.adjEO2.grid(row=1, sticky=tk.W)

        self.propiedad.grid(column=0, row=5, sticky=tk.W)

        grid_positioning(6,
            [[self.tipoL, self.tipo],
            [self.direccionL, self.direccionE],
            [self.superficieTL, self.superficieTE],
            [self.superficieCL, self.superficieCE],
            [self.amuebladaL, frameEditO1],
            [self.numRecamarasL, self.numRecamarasE],
            [self.numBañosL, self.numBañosE],
            [self.numNivelesL, self.numNivelesE],
            [self.mascotasL, f2],
            [self.posesionL, self.posesionT],
            [self.adjudL, f3]])


        ##############################################################
        ##--------------------Datos de la oferta--------------------##
        ##############################################################
        self.oferta = tk.Label(self, text="Oferta: ", font = tSize[0], pady = 3)
        self.estadoL = tk.Label(self, text="Estado: ", font= tSize[0])
        self.monedaL = tk.Label(self, text="Moneda: ", font= tSize[0])
        self.precioL = tk.Label(self, text="Precio: ", font= tSize[0])

        self.estadoE = tk.StringVar(self, value = "Renta")
        self.estado = tk.OptionMenu(self, self.estadoE, "Renta", "Venta")
        self.estado.config(font = tSize[0])
        menu = self.nametowidget(self.estado.menuname)
        menu.config(font=tSize[0])

        self.monedaE = tk.StringVar(self, value = "Dolares")
        self.moneda = tk.OptionMenu(self, self.monedaE, "Dolares", "Pesos")
        self.moneda.config(font = tSize[0])
        menu = self.nametowidget(self.moneda.menuname)
        menu.config(font=tSize[0])

        self.precioE = tk.Entry(self, font = tSize[0], width=tSize[1]-15, validate = 'key', validatecommand = vcmd)

        self.oferta.grid(column=0, row=18, sticky=tk.W)

        grid_positioning(19,
            [[self.estadoL, self.estado],
            [self.monedaL, self.moneda],
            [self.precioL, self.precioE]])

        self.addOfferB= tk.Button(self, text = "ACtualizar", command=self.updateOffer, height=bSize[0], width=bSize[1])
        self.addOfferB.grid(column=0, row=22, columnspan=4, pady = 10)

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
                try:
                    float(value_if_allowed)
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
        if cliente == None and event == '<Return>':
            self.idClienteE.config(fg="red")
            self.idClienteE.delete(0, tk.END)
            tk.messagebox.showerror(title="Error", message="No se encontro cliente.")
        else:
            self.idClienteE.config(fg="black")
            self.nombreE.config(state='normal')
            self.apellidosE.config(state='normal')
            self.nombreE.delete(0, tk.END)
            self.apellidosE.delete(0, tk.END)
            self.nombreE.insert(0, cliente[1])
            self.apellidosE.insert(0, cliente[2]+" "+cliente[3])
            self.nombreE.config(state='disabled')
            self.apellidosE.config(state='disabled')

    def check_offer(self, event):
        id = self.idOfertaE.get()
        names = ['idCliente', 'idTipo', 'direccion', 'superficieT', 'superficieC', 'amueblada', 'numRecamaras', 'numBaños', 'numNiveles', 'mascotas', 'posesion', 'adjunto', 'estado', 'moneda', 'precio']
        try:offer = self.manejador.get_specific_offer(id)
        except:offer = None        
        if offer == None:
            self.idOfertaE.config(fg="red")
            self.idOfertaE.delete(0, tk.END)
        else:
            self.idOfertaE.config(fg="black")
            self.data = {
                'idOferta': id
            }
            for i in range(len(names)):
                self.data[names[i]] = offer[0][i]
            self.fill_data()
    
    def fill_data(self):
        self.idClienteE.delete(0, tk.END)
        self.idClienteE.insert(0, self.data['idCliente'])
        for tipo in self.tiposP:
            if tipo[1] == self.data['idTipo']:
                self.tipoE.set(tipo)
                self.data['idTipo'] = tipo[0]
                break
        self.direccionE.delete(0, tk.END)
        self.direccionE.insert(0, self.data['direccion'])
        self.superficieTE.delete(0, tk.END)
        self.superficieTE.insert(0, self.data['superficieT'])
        self.superficieCE.delete(0, tk.END)
        self.superficieCE.insert(0, self.data['superficieC'])
        self.amuebladaE.set(self.data['amueblada'])
        self.numRecamarasE.set(self.data['numRecamaras'])
        self.numNivelesE.set(self.data['numNiveles'])
        self.numBañosE.set(self.data['numBaños'])
        self.mascotasE.set(self.data['mascotas'])
        self.posesionE.set(self.data['posesion'])
        self.adjE.set(self.data['adjunto'])
        self.estadoE.set(self.data['estado'])
        self.monedaE.set(self.data['moneda'])
        self.precioE.delete(0, tk.END)
        self.precioE.insert(0, self.data['precio'])


    def updateOffer(self):
        try:
            prop = {'idCliente': self.idClienteE.get(), 'idTipo':list(self.tipoE.get())[1], "direccion":self.direccionE.get(), "superficieT":(self.superficieTE.get()), 
                    "superficieC":(self.superficieCE.get()), "amueblada":self.amuebladaE.get(), "numRecamaras":str(self.numRecamarasE.get()), "numNiveles":str(self.numNivelesE.get()), 
                    "numBaños":str(self.numBañosE.get()), "mascotas":str(self.mascotasE.get()), "posesion":self.posesionE.get(), "adjunto":str(self.adjE.get())}
            oferta = {"estado":self.estadoE.get(), 
                      "moneda":self.monedaE.get(), 
                      "precio":self.precioE.get()}
            tables = (['oferta', oferta], ['propiedad', prop])
            strings = ["direccion", "amueblada", "posesion", "estado", "moneda"]
            for table in tables:
                query = 'UPDATE '+table[0]+' SET '
                for key in table[1].keys():
                    if table[1][key] != str(self.data[key]):
                        if key not in strings: query += key+' = '+table[1][key]+', '
                        else: query += key+' = "'+table[1][key]+'", '
                if table[0] == 'oferta': query = query[:-2]+' WHERE idOferta = '+self.data['idOferta']+';'
                else: query = query[:-2]+' WHERE idPropiedad = '+self.data['idOferta']+';'
                if 'SE ' not in query: self.manejador.update(query)
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