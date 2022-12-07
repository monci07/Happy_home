import tkinter as tk
from tkinter import ttk
from interface import *

def rentShowMenu(self):
    global Self
    Self = self
    mainMenuInvisible(self)
    self.geometry(searchSize)
    self.title("Happy home - Rent Search")
    config_grid(self,[[i,0] for i in range(0,4)], [[i,0] for i in range(0,3)])
    
    self.bInquilinoL = tk.Label(self, text = "Inquilino:", font = self.tSize[0])

    self.bInqIdL= tk.Label(self, text = "ID:", font = self.tSize[0])
    self.bInqIdE = tk.Entry(self, font = self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    self.bInqNameL= tk.Label(self, text = "Nombre:", font = self.tSize[0])
    self.bInqNameE = tk.Entry(self, font = self.tSize[0], validate = 'key', validatecommand = self.vcmdInt)

    ########################################################

    self.bPropietarioL = tk.Label(self, text = "Propietario:", font = self.tSize[0])
    
    self.bPropIdL= tk.Label(self, text = "ID:", font = self.tSize[0])
    self.bPropIdE = tk.Entry(self, font = self.tSize[0], width=self.tSize[1], validate = 'key', validatecommand = self.vcmdInt)
    self.bPropNameL= tk.Label(self, text = "Nombre:", font = self.tSize[0])
    self.bPropNameE = tk.Entry(self, font = self.tSize[0], validate = 'key', validatecommand = self.vcmdInt)

    ########################################################

    self.rentResult = ttk.Treeview(self, 
                                   columns = ("Propietario", "Inquilino", "Direccion","Fecha de Inicio"),
                                   show = "headings",
                                   height = 30,
                                   selectmode="browse")
    style = ttk.Style()
    style.configure("Treeview", font=self.tSize[0])
    style.configure("Treeview.Heading", font=self.tSize[0])
    tree_handler(self.rentResult, [225, 225, 400, 200])
    self.rentResult.bind('<Button-1>', R_event_handler) 

    for renta in self.manejador.get_renta():
        self.rentResult.insert('', 'end', values = renta)

    horzscrlbar = ttk.Scrollbar(self, orient ="horizontal", command = self.rentResult.xview)
    ########################################################

    self.rentaFin = tk.Button(self, text = "Finalizar renta",  width=13, font =self.tSize[0], command = lambda: rentaFin(self))
    self.filtro = tk.Button(self, text = "Filtro", width=13, font =self.tSize[0], command = lambda: rentaFiltro(self))
    self.volver = tk.Button(self, text = "Volver",  width=13, font =self.tSize[0], command = lambda: buscarRMenuInvisible(self))

    ########################################################

    self.buscarRMenu = [
        self.bInquilinoL,
        self.bInqIdL, self.bInqIdE,
        self.bInqNameL, self.bInqNameE,
        self.bPropietarioL,
        self.bPropIdL, self.bPropIdE,
        self.bPropNameL, self.bPropNameE,
        self.rentResult,
        self.rentaFin, self.filtro, self.volver
    ]

    self.bInquilinoL.grid(column=0, row=0, columnspan=2, sticky="w")

    grid_positioning(1,[
        [self.bInqIdL, [self.bInqIdE],1],
        [self.bInqNameL, [self.bInqNameE],1]])

    self.bPropietarioL.grid(column=0, row=3, columnspan=2, sticky="w", pady=5)
    
    grid_positioning(4,[ 
        [self.bPropIdL, [self.bPropIdE],1],
        [self.bPropNameL, [self.bPropNameE],1]])

    self.rentResult.grid(column=2, row=0, rowspan=100, sticky="w")
    self.rentResult.configure(xscrollcommand = horzscrlbar.set)

    self.rentaFin.grid(column = 0, row = 6, sticky="ns", columnspan=2, pady=3)
    self.filtro.grid(column = 0, row = 7, sticky="ns", columnspan=2, pady=3)
    self.volver.grid(column = 0, row = 8, sticky="ns", columnspan=2, pady=3)

def R_event_handler(event):
    if Self.rentResult.identify_region(event.x, event.y) == "separator":
        return "break"
    elif Self.rentResult.identify_region(event.x, event.y) == "cell":
        Self.oIdE.delete(0,tk.END)
        Self.oIdE.insert(0,Self.offersResult.focus())