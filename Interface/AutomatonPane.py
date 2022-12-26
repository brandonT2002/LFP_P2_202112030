import tkinter as tk
from tkinter import *

class AutomatonPane(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root)
        self.configure(bg='#2A2D2E')
        self.grid(row=0,column=1,pady=20,padx=20,sticky='nswe')