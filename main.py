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

        self.vcmdInt = (self.register(self.validateNumber),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.vcmdAlpha = (self.register(self.validateAlpha),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        try:
            
            self.title("Happy home - Main Menu")
            self.geometry(mainSize)
            self.manejador = server.serverCom()

            self.frameMainMenu = tk.Frame(self)

            f1 = tk.Frame(self.frameMainMenu)
            self.offersAdd= tk.Button(f1, text = "Agregar ofertas", 
                                    font =self.tSize[0], command = self.addOffer, 
                                    height=bHeight, width=15)
            self.clientsAdd= tk.Button(f1, text = "Agregar clientes", 
                                    font =self.tSize[0], command = self.addClient, 
                                    height=bHeight, width=15)
        
            ########################################
        
            f2 = tk.Frame(self.frameMainMenu)
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
        
            f3 = tk.Frame(self.frameMainMenu)
            self.editOffer= tk.Button(f3, text = "Editar oferta", 
                                    font =self.tSize[0], command = self.editOffer, 
                                    height=bHeight, width=15)
            self.editClient= tk.Button(f3, text = "Editar cliente",
                                    font =self.tSize[0], command = self.editClient,
                                    height=bHeight, width=15)
        
            self.mainMenu = [self.frameMainMenu, f2, f3]

            config_grid(self.frameMainMenu,[[i, 1] for i in range(0,3)], [[i, 1] for i in range(0, 1)])

            padx = 10
            pady = 5
            self.frameMainMenu.grid(column=0, row=0)
            f1.grid(column=0, row=0)
            self.offersAdd.grid(column=0, row = 0, padx = padx, pady = pady)
            self.clientsAdd.grid(column=1, row = 0, padx = padx, pady = pady)

            f2.grid(column=0, row=1)
            self.clientsSearch.grid(column=0, row = 0, padx = padx, pady = pady)
            self.offersSearch.grid(column=1, row = 0, padx = padx, pady = pady)
            self.rentsSearch.grid(column=3, row = 0, padx = padx, pady = pady)
        
            f3.grid(column=0, row=2)
            self.editOffer.grid(column=0, row = 0, padx = padx, pady = pady)
            self.editClient.grid(column=1, row = 0, padx = padx, pady = pady)

            self.protocol("WM_DELETE_WINDOW", self.on_closing)

        except:
            
            self.title("Happy home - Conection error")
            tk.Label(self, text = "No se pudo conectar con el servidor,\n favor de cerrar el programa y prender XAMPP.", font = self.tSize[0]).pack(expand=True, fill='both')
        

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
        client.userInsert(self.manejador)
    
    def addOffer(self):
        offer.offerInsert(server = self.manejador)
    
    def editOffer(self):
        offerEdit.offerEdit(self.manejador)

    def editClient(self):
        clientEdit.userEdit(self.manejador)

if __name__ == '__main__':
    #creacion de ventana principal
    app=App()
    app.mainloop()