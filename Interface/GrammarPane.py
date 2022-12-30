import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from Backend.Controller import Controller

class GrammarPane(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root)
        self.configure(bg='#2A2D2E')
        self.grid(row=0,column=1,pady=20,padx=20,sticky='nswe')
        self.ctrl : Controller = None
        self.components()

    def components(self):
        self.rowconfigure((0,1,2,3,4,5),weight=1)
        self.rowconfigure(6,weight=10)
        self.columnconfigure((0,1,2,3),weight=1)
        self.columnconfigure(4,weight=0)

        title1 = Label(master=self,text='Gramática Libre de Contexto',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        title1.grid(row=0,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nw')

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#343638", background= "#fff", selectforeground='white',activebackground='#343638',activeforeground='black',foreground='white')

        self.cbGrammar = ttk.Combobox(master=self,font=('Roboto Medium',16))
        self.cbGrammar.grid(row=1,column=0,columnspan=2,pady=0,padx=(20,10),sticky='nwe')
        self.cbGrammar.set('Seleccione una Gramática')

        self.information = Button(master=self,text='Información General',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.getReport)
        self.information.grid(row=1,column=2,pady=0,padx=(10,10),sticky='nwe')

        self.branchTree = Button(master=self,text='Árbol de Derivación',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.branchTree.grid(row=1,column=3,pady=0,padx=(10,20),sticky='nwe')

        self.delete = Button(master=self,text='Limpiar',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.delete.grid(row=5,column=3,pady=(0,0),padx=(10,20),sticky='swe')
        self.delete.grid_remove()

    def getReport(self):
        if self.cbGrammar.get() == 'Seleccione una Gramática':
            messagebox.showinfo('Información','No se ha seleccionado una gramática')
        else:
            index = int(self.cbGrammar.get().split(' - ')[0]) - 1
            self.ctrl.generatedReportG(index)
            image = Image.open('Reports/ReportG.png')
            #image = image.resize((700,450),Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)

            label = Label(self,image=image,background='#2A2D2E')
            label.img = image
            label.grid(row=2,column=0,rowspan=3,columnspan=4,pady=20,padx=20,sticky='nswe')

            self.delete.grid()