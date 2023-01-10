import tkinter as tk
from tkinter import messagebox
from Screens.windows import offer
from interface import *
from tkinter import ttk

class info(tk.Toplevel):
    Self = None
    def __init__(self, data):
        self.tSize = [10, 10]
        ''' holi '''
        global Self
        Self = self
        super().__init__()
        self.geometry(offerInfo)
        self.resizable(False,False)
        self.title("Happy home - Offer Info")

        self.infoTable = ttk.Treeview(self,
                                      columns = ("1", "2"),
                                      selectmode="browse",
                                      show= "tree",
                                      height=16)
        self.infoTable.bind('<Button-1>', self.O_event_handler)
        style = ttk.Style()
        style.configure("Treeview", font=self.tSize[0])
        tree_handler(self.infoTable, [150, 400])
        self.infoTable.column('#0', width=0, stretch='no')

        data_names = ["Id", "Propietario", "Direccion", "Tipo", "Estado", "Moneda", "Precio", "S. Terreno(m2)", "S. Constr.(m2)", "Amueblado", "Recamaras", "Baños", "Niveles", "Mascotas", "Posesion", "Adjudicada"]

        for i in range(len(data_names)):
            self.infoTable.insert("", tk.END, values=(data_names[i],data[i]))

        self.infoTable.pack()        
    
    def O_event_handler(self,event):
        if Self.infoTable.identify_region(event.x, event.y) == "separator":
            return "break"