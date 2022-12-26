import tkinter as tk
from tkinter import *

class OptionPane(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root,width=200)
        self.configure(bg='#2A2D2E')
        self.grid(row=0,column=0,sticky='nswe')

        self.components()

    def components(self):
        self.grid_rowconfigure(0,minsize=10)
        self.grid_rowconfigure(7,weight=1)
        self.grid_rowconfigure(8,minsize=20)
        self.grid_rowconfigure(11,minsize=10)

        opciones = Label(master=self,text='Opciones',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        opciones.grid(row=1,column=0,pady=10,padx=10)

        self.upload = Button(master=self,text='Cargar Archivo',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.upload.grid(row=2,column=0,pady=10,padx=20)

        self.grammarMod = Button(master=self,text='Modulo Gramática',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.grammarMod.grid(row=3,column=0,pady=10,padx=20)

        self.automatonMod = Button(master=self,text='Modulo Autómata',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.automatonMod.grid(row=4,column=0,pady=10,padx=20)

        self.exit = Button(master=self,text='Salir',font=('Roboto Medium',11),bg='#D35B58',activebackground='#D35B58',foreground='white',activeforeground='white',width=15,height=1,command=quit)
        self.exit.grid(row=9,column=0,pady=10,padx=20)