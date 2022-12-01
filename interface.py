import tkinter as tk
from tkinter import ttk
import pyperclip

mainSize = "1000x300"
searchSize = "1325x635"
newOffer = "550x750"
newClient = "400x200"
bHeight = 5

def grid_positioning(init=int, list=list):
    ''' test '''
    for i in range(len(list)):
        list[i][0].grid(column=0, row=i+init, sticky=tk.E)
        for j in range(len(list[i][1])):
            list[i][1][j].grid(column=j+1, row=i+init, sticky=tk.W, columnspan=list[i][2])

def validate(action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        ''' test '''
        if value_if_allowed=='': return True
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

def config_grid(self, rows: list, columns: list):
    for i in range(len(rows)):
        self.rowconfigure(rows[i][0], weight=rows[i][1])
    for i in range(len(columns)):
        self.columnconfigure(columns[i][0], weight=columns[i][1])

def mainMenuInvisible(self):
    for item in self.mainMenu:
        item.grid_forget()

def mainMenuVisible(self):
    self.geometry(mainSize)
    self.title("Happy home - Main Menu")
    config_grid(self,[[i, 1] for i in range(0,4)], [[i, 1] for i in range(0, 3)])
    for i in range(len(self.mainMenu)):
        aux = 1 if (i+1)%2 > 0 else 2
        self.mainMenu[i].grid(column=i, row=aux)

def buscarOMenuInvisible(self):
    for item in self.buscarOMenu:
        item.grid_forget()
    mainMenuVisible(self)
    
def buscarCMenuInvisible(self):
    for item in self.buscarCMenu:
        item.grid_forget()
    mainMenuVisible(self)

def buscarRMenuInvisible(self):
    for item in self.buscarRMenu:
        item.grid_forget()
    mainMenuVisible(self)

def tree_handler(tree=ttk.Treeview, lWith=list):
    for i in range(len(tree['columns'])):
        tree.column(tree['columns'][i],anchor=tk.CENTER, width=lWith[i])
        tree.heading(tree['columns'][i], text=tree['columns'][i])