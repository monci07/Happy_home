import tkinter as tk
from tkinter import messagebox
from Screens.windows import offer
from interface import *

class userInsert(tk.Toplevel):
    def __init__(self, server):
        ''' window for addign a client '''
        bSize = [1, 10]
        tSize = [8, 15]
        tk.Toplevel.__init__(self)
        self.title("Happy home - New User")
        self.geometry(newClient)
        self.resizable(False,False)
        self.manejador = server
        self.iconbitmap("home.ico")
        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.nombreL = tk.Label(self, text="Nombre: ", font=tSize[0])
        self.apellidoPL = tk.Label(self, text="Apellido Paterno: ", font=tSize[0])
        self.apellidoML = tk.Label(self, text="Apellido Materno: ", font=tSize[0])
        self.telL = tk.Label(self, text="Telefono: ", font=tSize[0])
        self.emailL = tk.Label(self, text="Email: ", font=tSize[0])

        self.nombreE = tk.Entry(self, font = tSize[0], width=tSize[1])
        self.apellidoPE = tk.Entry(self, font = tSize[0], width=tSize[1])
        self.apellidoME = tk.Entry(self, font = tSize[0], width=tSize[1])
        self.telE = tk.Entry(self,  font = tSize[0], width=tSize[1], validate = 'key', validatecommand = vcmd)
        self.emailE = tk.Entry(self, font = tSize[0], width=tSize[1])

        self.Añadir= tk.Button(self, text = "Añadir", command=self.addCustomer, height=bSize[0], width=bSize[1])
        
        self.Añadir.grid(column=0, row=5, columnspan=2)
        
        grid_positioning(0,
            [[self.nombreL,[self.nombreE],1], 
             [self.apellidoPL,[self.apellidoPE], 1],
             [self.apellidoML,[self.apellidoME], 1],
             [self.telL,[self.telE],1],
             [self.emailL,[self.emailE],1]])
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grab_set()
        self.focus
            

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

    def addCustomer(self):
        nombre=[self.nombreE.get(), self.apellidoPE.get(), self.apellidoME.get()]
        tel = self.telE.get()
        mail=self.emailE.get()
        if ('' not in nombre) or ('' not in tel) or ('' not in mail):
            client = self.manejador.insert_client(nombre, tel, mail)
            if messagebox.askyesno(message='Quiere agregarle alguna propiedad?', icon='question', title='Agregar propiedad') == True:
                self.destroy()
                self.newWindow = offer.offerInsert(str(client), self.manejador)
            else:
                self.destroy()
            

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Quieres salir?"):
            self.destroy()