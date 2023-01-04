import tkinter as tk
from tkinter import messagebox
from Screens.windows import offer
from interface import *

class userEdit(tk.Toplevel):
    def __init__(self, server):
        
        ''' window for addign a client '''

        bSize = [1, 10]
        tSize = [8, 15]
        tk.Toplevel.__init__(self)
        self.title("Happy home - User Edit")
        self.geometry(editClient)
        self.resizable(False,False)
        self.manejador = server
        self.iconbitmap("home.ico")
        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.client = []

        self.idClienteL = tk.Label(self, text="ID Cliente: ", font=tSize[0])
        self.nombreL = tk.Label(self, text="Nombre: ", font=tSize[0])
        self.apellidoPL = tk.Label(self, text="Apellido Paterno: ", font=tSize[0])
        self.apellidoML = tk.Label(self, text="Apellido Materno: ", font=tSize[0])
        self.telL = tk.Label(self, text="Telefono: ", font=tSize[0])
        self.emailL = tk.Label(self, text="Email: ", font=tSize[0])

        self.idClienteE = tk.Entry(self, font = tSize[0], width=tSize[1])
        self.idClienteE.bind("<FocusOut>", self.searchCustomer)
        self.idClienteE.bind("<Return>", self.searchCustomer)
        self.nombreE = tk.Entry(self, font = tSize[0], width=tSize[1], state='disabled')
        self.apellidoPE = tk.Entry(self, font = tSize[0], width=tSize[1], state='disabled')
        self.apellidoME = tk.Entry(self, font = tSize[0], width=tSize[1], state='disabled')
        self.telE = tk.Entry(self,  font = tSize[0], width=tSize[1], validate = 'key', validatecommand = vcmd, state='disabled')
        self.emailE = tk.Entry(self, font = tSize[0], width=tSize[1], state='disabled')

        self.Añadir= tk.Button(self, text = "Actualizar", command=self.updateCustomer, height=bSize[0], width=bSize[1], font= tSize[0])
        
        grid_positioning(0,
            [[self.idClienteL,self.idClienteE],
             [self.nombreL,self.nombreE], 
             [self.apellidoPL,self.apellidoPE],
             [self.apellidoML,self.apellidoME],
             [self.telL,self.telE],
             [self.emailL,self.emailE]])
        
        self.Añadir.grid(column=0, row=6, columnspan=2)

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

    def updateCustomer(self):
        nombre=[self.nombreE.get(), self.apellidoPE.get(), self.apellidoME.get()]
        tel = self.telE.get()
        mail=self.emailE.get()
        self.manejador.consultar('UPDATE cliente SET nombre = \"' + nombre[0] + '\", apellidoP = \"' + nombre[1] + '\", apellidoM = \"' + nombre[2] + '\", tel = \"' + tel + '\", correo = \"' + mail + '\" WHERE idCliente = ' + self.idClienteE.get() + ';')
        self.destroy()
       
    def searchCustomer(self, event):
        aux = self.manejador.consultar('SELECT nombre, apellidoP, apellidoM, tel, correo FROM cliente WHERE idCliente = ' + self.idClienteE.get() + ';')
        entrys = [self.nombreE, self.apellidoPE, self.apellidoME, self.telE, self.emailE]
        for i in range(len(aux[0])):
            entrys[i].config(state='normal')
            entrys[i].delete(0, tk.END)
            entrys[i].insert(0, aux[0][i])
            self.client.append(aux[0][i])


    def on_closing(self):
        if messagebox.askokcancel("Quit", "Quieres salir?"):
            self.destroy()