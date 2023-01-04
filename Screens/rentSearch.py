import tkinter as tk
from tkinter import ttk
from interface import *

def rentShowMenu(self):
    global Self
    Self = self
    mainMenuInvisible(self)
    self.geometry(searchSize)
    self.title("Happy home - Rent Search")
    config_grid(self,[[i,0] for i in range(0,7)], [[i,0] for i in range(0,3)])
    
    self.bInquilinoL = tk.Label(self, text = "Inquilino:", font = self.tSize[0])

    self.bInqNameL= tk.Label(self, text = "Nombre:", font = self.tSize[0])
    self.bInqNameE = tk.Entry(self, font = self.tSize[0], width=self.tSize[1]+5, validate = 'key', validatecommand = self.vcmdAlpha)

    ########################################################

    self.bPropietarioL = tk.Label(self, text = "Propietario:", font = self.tSize[0])
    
    self.bPropNameL= tk.Label(self, text = "Nombre:", font = self.tSize[0])
    self.bPropNameE = tk.Entry(self, font = self.tSize[0], width=self.tSize[1]+5, validate = 'key', validatecommand = self.vcmdAlpha)

    ########################################################

    self.rentResult = ttk.Treeview(self, 
                                   columns = ("Propietario", "Inquilino", "Direccion","Fecha de Inicio"),
                                   show = "headings",
                                   height = 33,
                                   selectmode="browse")
    style = ttk.Style()
    style.configure("Treeview", font=self.tSize[0])
    style.configure("Treeview.Heading", font=self.tSize[0])
    tree_handler(self.rentResult, [225, 225, 400, 200])
    self.rentResult.bind('<Button-1>', R_event_handler) 

    for renta in self.manejador.get_renta():
        self.rentResult.insert('', 'end', iid = renta[0], values = renta[1:])

    horzscrlbar = ttk.Scrollbar(self, orient ="horizontal", command = self.rentResult.xview)
    ########################################################

    self.rentaFin = tk.Button(self, text = "Finalizar renta",  width=13, font =self.tSize[0], command = lambda: renta_end(self))
    self.filtro = tk.Button(self, text = "Filtro", width=13, font =self.tSize[0], command = lambda: renta_Filtro(self))
    self.volver = tk.Button(self, text = "Volver",  width=13, font =self.tSize[0], command = lambda: buscarRMenuInvisible(self))

    ########################################################

    self.buscarRMenu = [
        self.bInquilinoL,
        self.bInqNameL, self.bInqNameE,
        self.bPropietarioL,
        self.bPropNameL, self.bPropNameE,
        self.rentResult,
        self.rentaFin, self.filtro, self.volver
    ]

    self.bInquilinoL.grid(column=0, row=0, columnspan=2, sticky="w", pady=4)

    grid_positioning(1,[
        [self.bInqNameL, self.bInqNameE]])

    self.bPropietarioL.grid(column=0, row=2, columnspan=2, sticky="w", pady=4)
    
    grid_positioning(3,[ 
        [self.bPropNameL, self.bPropNameE]])

    self.rentResult.grid(column=2, row=0, rowspan=100, sticky="ns", padx=4)
    self.rentResult.configure(xscrollcommand = horzscrlbar.set)

    self.rentaFin.grid(column = 0, row = 4, sticky="ns", columnspan=2, pady=3)
    self.filtro.grid(column = 0, row = 5, sticky="ns", columnspan=2, pady=3)
    self.volver.grid(column = 0, row = 6, sticky="ns", columnspan=2, pady=3)

def renta_end(self):
    if self.rentResult.selection() == ():
        return
    self.manejador.delete_rent(self.rentResult.selection()[0])
    self.rentResult.delete(self.rentResult.selection()[0])

def renta_Filtro(self):
    inq = self.bInqNameE.get()
    prop = self.bPropNameE.get()
    rentas = [item for item in self.manejador.get_renta()]
    if inq != '' or prop != '':
        for child in self.rentResult.get_children():
            rent = self.rentResult.item(child)["values"]
            if prop == '' and inq not in rent[1]: self.rentResult.delete(child)
            elif prop not in rent[0] and inq == '': self.rentResult.delete(child)
            elif prop not in rent[0] and inq not in rent[1]: self.rentResult.delete(child)
    else:
        items = self.rentResult.get_children()
        for renta in rentas:
            if str(renta[0]) not in items: self.rentResult.insert('', 'end', iid = renta[0], values = renta[1:])
    


def R_event_handler(event):
    if Self.rentResult.identify_region(event.x, event.y) == "separator":
        return "break"