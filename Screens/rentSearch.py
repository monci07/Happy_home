import tkinter as tk
from tkinter import ttk
from interface import *

def rentShowMenu(self):
    mainMenuInvisible(self)
    self.geometry(searchSize)
    
    self.volver = tk.Button(self, text = "Test", font =self.tSize[0], command = lambda: buscarRMenuInvisible(self), height=bHeight, width=30)

    self.buscarRMenu = [self.volver]
    
    for item in self.buscarRMenu:
        item.grid(column=1, row=1)