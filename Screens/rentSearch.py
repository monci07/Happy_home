import tkinter as tk
from tkinter import ttk
from interface import *

def rentShowMenu(self):
    global Self
    Self = self
    mainMenuInvisible(self)
    self.geometry(searchSize)
    self.title("Happy home - Rent Search")
    
    self.frameRentSearch = tk.Frame(self)

    
    config_grid(self.frameRentSearch,[[i,0] for i in range(0,7)], [[i,0] for i in range(0,3)])
    
    self.bInquilinoL = tk.Label(self.frameRentSearch, text = "Inquilino:", font = self.tSize[0])

    self.bInqNameL= tk.Label(self.frameRentSearch, text = "Nombre:", font = self.tSize[0])
    self.bInqNameE = tk.Entry(self.frameRentSearch, font = self.tSize[0], width=self.tSize[1]+5, validate = 'key', validatecommand = self.vcmdAlpha)

    ########################################################

    self.bPropietarioL = tk.Label(self.frameRentSearch, text = "Propietario:", font = self.tSize[0])
    
    self.bPropNameL= tk.Label(self.frameRentSearch, text = "Nombre:", font = self.tSize[0])
    self.bPropNameE = tk.Entry(self.frameRentSearch, font = self.tSize[0], width=self.tSize[1]+5, validate = 'key', validatecommand = self.vcmdAlpha)

    ########################################################

    self.rentResult = ttk.Treeview(self.frameRentSearch, 
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

    horzscrlbar = ttk.Scrollbar(self.frameRentSearch, orient ="horizontal", command = self.rentResult.xview)
    ########################################################

    self.rentaFin = tk.Button(self.frameRentSearch, text = "Finalizar renta",  width=13, font =self.tSize[0], command = lambda: renta_end(self))
    self.filtro = tk.Button(self.frameRentSearch, text = "Filtro", width=13, font =self.tSize[0], command = lambda: renta_Filtro(self))
    self.volver = tk.Button(self.frameRentSearch, text = "Volver",  width=13, font =self.tSize[0], command = lambda: buscarRMenuInvisible(self))

    ########################################################

    self.frameRentSearch.grid(column=0, row=0, sticky="nsew")

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
    # Check if the user has selected a rental to end
    if self.rentResult.selection() == ():
        return
    # Delete the selected rental
    self.manejador.delete_rent(self.rentResult.selection()[0])
    # Delete the selected rental from the list
    self.rentResult.delete(self.rentResult.selection()[0])

def renta_Filtro(self):
    # Get the values of the two entries
    inq = self.bInqNameE.get()
    prop = self.bPropNameE.get()
    # Get all the renta values
    rentas = [item for item in self.manejador.get_renta()]
    # If the entries are not empty, check if they are in the renta values
    if inq != '' or prop != '':
        # Loop through each child of the rentResult treeview
        for child in self.rentResult.get_children():
            # Get the values of the current child
            rent = self.rentResult.item(child)["values"]
            # If the prop entry is empty, and the inq entry does not match the current child, delete the child
            if prop == '' and inq not in rent[1]: self.rentResult.delete(child)
            # If the inq entry is empty, and the prop entry does not match the current child, delete the child
            elif prop not in rent[0] and inq == '': self.rentResult.delete(child)
            # If both entries do not match the current child, delete the child
            elif prop not in rent[0] and inq not in rent[1]: self.rentResult.delete(child)
    # If both entries are empty, loop through each renta value
    else:
        items = self.rentResult.get_children()
        for renta in rentas:
            # If the current renta value is not in the rentResult treeview, insert it
            if str(renta[0]) not in items: self.rentResult.insert('', 'end', iid = renta[0], values = renta[1:])
    


def R_event_handler(event):
    # Check if the mouse event occurred within the separator
    if Self.rentResult.identify_region(event.x, event.y) == "separator":
        # If it did, don't allow the mouse event to continue
        return "break"