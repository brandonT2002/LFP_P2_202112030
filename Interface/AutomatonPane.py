import tkinter as tk
from tkinter import *
from tkinter import ttk

class AutomatonPane(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root)
        self.configure(bg='#2A2D2E')
        self.grid(row=0,column=1,pady=20,padx=20,sticky='nswe')

        self.components()

    def components(self):
        self.rowconfigure((0,1,2,3,4,5),weight=1)
        self.rowconfigure(6,weight=10)
        self.columnconfigure((0,1,2,3),weight=1)
        self.columnconfigure(4,weight=0)

        title1 = Label(master=self,text='Autómata de Pila',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        title1.grid(row=0,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nw')

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox',fieldbackground= "#343638", background= "#fff", selectforeground='white',activebackground='#343638',activeforeground='black',foreground='white')

        self.cbAutomaton = ttk.Combobox(master=self,values=['value1','value2','value3'],font=('Roboto Medium',16))
        self.cbAutomaton.grid(row=1,column=0,columnspan=2,pady=0,padx=(20,10),sticky='nwe')
        self.cbAutomaton.set('Seleccione un Autómata')

        self.information = Button(master=self,text='Información General',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.information.grid(row=1,column=2,columnspan=2,pady=0,padx=(10,20),sticky='nwe')

        self.validateString = Button(master=self,text='Validar Cadena',font=('Roboto Medium',11),bg='gray40',activebackground='gray40',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.validateString.grid(row=2,column=0,pady=0,padx=(20,10),sticky='nwe')

        self.validationPath = Button(master=self,text='Ruta de Validación',font=('Roboto Medium',11),bg='gray40',activebackground='gray40',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.validationPath.grid(row=2,column=1,pady=0,padx=(10,10),sticky='nwe')

        self.stepByStep = Button(master=self,text='Paso a Paso',font=('Roboto Medium',11),bg='gray40',activebackground='gray40',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.stepByStep.grid(row=2,column=2,pady=0,padx=(10,10),sticky='nwe')

        self.onePass = Button(master=self,text='Una Pasada',font=('Roboto Medium',11),bg='gray40',activebackground='gray40',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.onePass.grid(row=2,column=3,pady=0,padx=(10,20),sticky='nwe')

        self.validateStringPane()

    def validateStringPane(self):
        self.stringPane = Frame(master=self)
        self.stringPane.grid(row=3,column=0,columnspan=4,rowspan=5,padx=20,pady=(0,20),sticky="nswe")
        self.stringPane.configure(bg='#2A2D2E')
        self.stringPane.rowconfigure(0, weight=1)
        self.stringPane.columnconfigure(0, weight=1)

        self.string = Entry(master=self.stringPane,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.string.configure(disabledbackground='#343638',disabledforeground='white')
        self.string.grid(row=0,column=0,padx=(0,20),sticky='nw')

        self.validateS = Button(master=self.stringPane,text='Validar',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.validateS.grid(row=0,column=1,sticky='nwe')