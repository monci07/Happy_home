import tkinter as tk
from tkinter import ttk

from Screens.windows import client
from Screens.windows import offer
from Screens.windows import clientEdit
from Screens.windows import offerEdit

from Screens import clientSearch
from Screens import offerSearch
from Screens import rentSearch
import DataBase.server as server
from interface import *

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.mainMenu=[]
        self.buscarCMenu=[]
        self.buscarRMenu=[]
        self.buscarOMenu=[]
        self.iconbitmap("home.ico")
        self.bSize = [1, 10]
        self.tSize = [10, 10]
        self.gSize = [0,1]

        self.title("Happy home - Main Menu")
        self.geometry(mainSize)
        self.resizable(False,False)

        self.vcmdInt = (self.register(self.validateNumber),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.vcmdAlpha = (self.register(self.validateAlpha),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.manejador = server.serverCom()

        f1 = tk.Frame(self)
        self.offersAdd= tk.Button(f1, text = "Agregar ofertas", 
                                  font =self.tSize[0], command = self.addOffer, 
                                  height=bHeight, width=15)
        self.clientsAdd= tk.Button(f1, text = "Agregar clientes", 
                                   font =self.tSize[0], command = self.addClient, 
                                   height=bHeight, width=15)
        
        ########################################
        
        f2 = tk.Frame(self)
        self.offersSearch= tk.Button(f2, text = "Buscar ofertas", 
                                     font =self.tSize[0], command = lambda: offerSearch.offerShowMenu(self), 
                                     height=bHeight, width=15)

        self.clientsSearch= tk.Button(f2, text = "Buscar clientes", 
                                      font =self.tSize[0], command = lambda: clientSearch.clientShowMenu(self), 
                                      height=bHeight, width=15)

        self.rentsSearch= tk.Button(f2, text = "Buscar rentas", 
                                    font =self.tSize[0], command = lambda: rentSearch.rentShowMenu(self), 
                                    height=bHeight, width=15)
        
        ########################################
        
        f3 = tk.Frame(self)
        self.editOffer= tk.Button(f3, text = "Editar oferta", 
                                  font =self.tSize[0], command = self.editOffer, 
                                  height=bHeight, width=15)
        self.editClient= tk.Button(f3, text = "Editar cliente",
                                   font =self.tSize[0], command = self.editClient,
                                   height=bHeight, width=15)
        
        self.mainMenu = [f1, f2, f3]

        config_grid(self,[[i, 1] for i in range(0,4)], [[i, 1] for i in range(0, 3)])

        pad = 10
        f1.grid(column=0, row=0, columnspan=3)
        self.offersAdd.grid(column=0, row = 0, padx = pad)
        self.clientsAdd.grid(column=1, row = 0, padx = pad)

        f2.grid(column=0, row=1, columnspan=3)
        self.clientsSearch.grid(column=0, row = 0, padx = pad)
        self.offersSearch.grid(column=1, row = 0, padx = pad)
        self.rentsSearch.grid(column=3, row = 0, padx = pad)
        
        f3.grid(column=0, row=2, columnspan=3)
        self.editOffer.grid(column=0, row = 0, padx = pad)
        self.editClient.grid(column=1, row = 0, padx = pad)

        
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def validateNumber(self, action, index, value_if_allowed,
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
    
    def validateAlpha(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed=='': return True
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return False
            except ValueError:
                return True
        else:
            return False    

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
    
    def editOffer(self):
        self.newWindow = offerEdit.offerEdit(self.manejador)

    def editClient(self):
        self.newWindow = clientEdit.userEdit(self.manejador)

if __name__ == '__main__':
    #creacion de ventana principal
    app=App()
    app.mainloop()