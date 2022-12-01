import tkinter as tk
from tkinter import ttk
from screens.windows import client
from screens.windows import offer
from screens import clientSearch
from screens import offerSearch
import DataBase.server as server
from interface import *

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        global bHeight
        global mainMenu

        self.mainMenu=[]
        self.buscarCMenu=[]
        self.buscarRMenu=[]
        self.buscarOMenu=[]

        self.bSize = [1, 10]
        self.tSize = [10, 20]
        self.gSize = [0,1]

        self.title("Happy home - Main Menu")
        self.geometry(mainSize)
        self.resizable(False,False)

        self.vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.manejador = server.serverCom()

        self.offersResult= tk.Button(self, text = "Buscar ofertas", 
                                     font =self.tSize[0], command = lambda: offerSearch.offerShowMenu(self), 
                                     height=bHeight, width=15)
        self.offersAdd= tk.Button(self, text = "Agregar ofertas", 
                                  font =self.tSize[0], command = self.addOffer, 
                                  height=bHeight, width=15)
        self.clientsSearch= tk.Button(self, text = "Buscar clientes", 
                                      font =self.tSize[0], command = lambda: clientSearch.clientShowMenu(self), 
                                      height=bHeight, width=15)
        self.clientsAdd= tk.Button(self, text = "Agregar clientes", 
                                      font =self.tSize[0], command = self.addClient, 
                                      height=bHeight, width=15)
        self.rentsSearch= tk.Button(self, text = "Buscar rentas", 
                                    font =self.tSize[0], command = self.rentShowMenu, 
                                    height=bHeight, width=15)
        self.mainMenu = [self.offersResult, self.offersAdd, self.clientsSearch, self.clientsAdd, self.rentsSearch]

        config_grid(self,[[i, 1] for i in range(0,2)], [[i, 1] for i in range(0, 5)])

        
        self.offersResult.grid(column=0, row=0)
        self.clientsSearch.grid(column=2, row=0)
        self.rentsSearch.grid(column=4, row=0)
        self.offersAdd.grid(column=1, row=1)
        self.clientsAdd.grid(column=3, row=1)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

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
#------------------menus----------------------#
###############################################
            
        #################################################
        #---------------------Offers--------------------#
        #################################################
    
            
            #self.offersResult.delete(*self.offersResult.get_children())
        #################################################
        #---------------------Client--------------------#
        #################################################

    


            #################################################
            #----------------------rent---------------------#
            #################################################
    def rentShowMenu(self):
        global bHeight
        global searchSize
        mainMenuInvisible(self)
        self.geometry(searchSize)
        
        self.volver = tk.Button(self, text = "Test", font =self.tSize[0], command = lambda: buscarRMenuInvisible(self), height=bHeight, width=30)

        self.buscarRMenu = [self.volver]

        for item in self.buscarRMenu:
            item.grid(column=1, row=1)

if __name__ == '__main__':
    #creacion de ventana principal
    app=App()
    app.mainloop()