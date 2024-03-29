import tkinter as tk
from tkinter import ttk
import pyperclip

mainSize = "580x425"
searchSize = "1325x723"
newOffer = "550x750"
newClient = "400x200"
editOffer = "550x850"
editClient = "400x225"
offerInfo = "560x325"
bHeight = 5

def grid_positioning(init=int, list=list):
    ''' 
        Puts widgets in a grid with a given initial position and a list of widgets
        Parameters:
            init (int): Initial position
            list (list): List of widgets
    '''
    for i in range(len(list)):
        list[i][0].grid(column=0, row=i+init, sticky=tk.E)
        list[i][1].grid(column=1, row=i+init, sticky=tk.W)

def config_grid(self, rows: list, columns: list):
    '''
        Configures the grid of the window
        Parameters:
            rows (list): List of lists with the row number[0] and the weight[1]
            columns (list): List of lists with the column number[0] and the weight[1]
    '''
    for i in range(len(rows)):
        self.rowconfigure(rows[i][0], weight=rows[i][1])
    for i in range(len(columns)):
        self.columnconfigure(columns[i][0], weight=columns[i][1])

def mainMenuInvisible(self):
    '''
        Hides the main menu
        Parameters:
            self (tk.Tk): Main window
    '''
    self.frameMainMenu.grid_forget()

def mainMenuVisible(self):
    '''
        Shows the main menu
        Parameters:
            self (tk.Tk): Main window
    '''
    self.geometry(mainSize)
    self.title("Happy home - Main Menu")
    self.frameMainMenu.grid(column=0, row=0)

def buscarOMenuInvisible(self):
    '''
        Hides the buscarO menu
        Parameters:
            self (tk.Tk): Main window
    '''
    self.frameOfferSearch.grid_forget()
    mainMenuVisible(self)
    
def buscarCMenuInvisible(self):
    '''
        Hides the buscarC menu
        Parameters:
            self (tk.Tk): Main window
    '''
    self.frameClientSearch.grid_forget()
    mainMenuVisible(self)

def buscarRMenuInvisible(self):
    '''
        Hides the buscarR menu
        Parameters:
            self (tk.Tk): Main window
    '''
    self.frameRentSearch.grid_forget()
    mainMenuVisible(self)

def tree_handler(tree:ttk.Treeview, lWith: list):
    '''
        Handles the treeview widget
        Parameters:
            tree (ttk.Treeview): Treeview widget
            lWith (list): List of widths for each column
    '''
    for i in range(len(tree['columns'])):
        tree.column(tree['columns'][i], anchor=tk.CENTER, width=lWith[i], stretch=False)
        tree.heading(tree['columns'][i], text=tree['columns'][i])