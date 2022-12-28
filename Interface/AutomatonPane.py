import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from Backend.Controller import Controller
class AutomatonPane(tk.Frame):
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

        title1 = Label(master=self,text='Autómata de Pila',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        title1.grid(row=0,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nw')

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox',fieldbackground= "#343638", background= "#fff", selectforeground='white',activebackground='#343638',activeforeground='black',foreground='white')

        self.cbAutomaton = ttk.Combobox(master=self,font=('Roboto Medium',16))
        self.cbAutomaton.bind('<<ComboboxSelected>>',self.viewAutomaton)
        self.cbAutomaton.grid(row=1,column=0,columnspan=2,pady=0,padx=(20,10),sticky='nwe')
        self.cbAutomaton.set('Seleccione un Autómata')

        self.information = Button(master=self,text='Información General',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.generatePDF)
        self.information.grid(row=1,column=2,columnspan=2,pady=0,padx=(10,20),sticky='nwe')

        self.alphabet = Label(master=self,text='Alfabeto: ',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        self.alphabet.grid(row=2,column=2,columnspan=2,pady=(10,10),padx=20,sticky='nw')

        self.string1 = Entry(master=self,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.string1.configure(disabledbackground='#343638',disabledforeground='white')
        self.string1.grid(row=2,column=0,pady=(10,10),padx=20,columnspan=2,sticky='nwe')

        self.validateString = Button(master=self,text='Validar Cadena',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.getString)
        self.validateString.grid(row=3,column=0,pady=(10,10),padx=(20,10),sticky='nwe')

        self.validationPath = Button(master=self,text='Ruta de Validación',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.option1)
        self.validationPath.grid(row=3,column=1,pady=(10,10),padx=(10,10),sticky='nwe')

        self.stepByStep = Button(master=self,text='Paso a Paso',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.option2)
        self.stepByStep.grid(row=3,column=2,pady=(10,10),padx=(10,10),sticky='nwe')

        self.onePass = Button(master=self,text='Una Pasada',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.onePass.grid(row=3,column=3,pady=(10,10),padx=(10,20),sticky='nwe')

        self.pathPane()
        self.stepPane()
        self.Panel1.grid_remove()
        self.Panel2.grid_remove()

    def pathPane(self):
        self.Panel1 = Frame(master=self)
        self.Panel1.grid(row=4,column=0,columnspan=4,rowspan=5,padx=20,pady=(0,20),sticky="nswe")
        self.Panel1.configure(bg='#2A2D2E')
        self.Panel1.rowconfigure(0,weight=1)
        self.Panel1.columnconfigure((0,1,2,3),weight=1)
        self.Panel1.columnconfigure(4,weight=0)

        self.route = Label(master=self.Panel1,text='Ruta: ',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        self.route.grid(row=0,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nwe')

    def stepPane(self):
        self.Panel2 = Frame(master=self)
        self.Panel2.grid(row=4,column=0,columnspan=4,rowspan=5,padx=20,pady=(0,20),sticky="nswe")
        self.Panel2.configure(bg='#2A2D2E')
        self.Panel2.rowconfigure(0,weight=1)
        self.Panel2.columnconfigure((0,1,2,3),weight=1)
        self.Panel2.columnconfigure(4,weight=0)

        self.previous = Button(master=self.Panel2,text='Anterior ←',font=('Roboto Medium',11),bg='#107C41',activebackground='#107C41',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.previous.grid(row=0,column=1,columnspan=1,padx=(20,10),sticky='new')

        self.next = Button(master=self.Panel2,text='Siguiente →',font=('Roboto Medium',11),bg='#107C41',activebackground='#107C41',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2')
        self.next.grid(row=0,column=2,columnspan=1,padx=(10,20),sticky='new')

        image = Image.open('Image/gr.png')
        image = image.resize((600,375),Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        label = Label(self.Panel2,image=image,background='#2A2D2E')
        label.img = image
        label.grid(row=1,column=0,rowspan=3,columnspan=4,pady=(0,20),sticky='nswe')

    def generatePDF(self):
        if self.cbAutomaton.get() == 'Seleccione un Autómata':
            messagebox.showinfo('Información','No se ha seleccionado un autómata')
        else:
            index = int(self.cbAutomaton.get().split(' - ')[0]) - 1
            self.ctrl.generatedReport(index)

    def getString(self):
        if self.string1.get().replace(' ','') == '':
            messagebox.showinfo('Información','Ingrese una cadena para validar')
        elif self.cbAutomaton.get() == 'Seleccione un Autómata':
            messagebox.showinfo('Información','No se ha seleccionado un autómata')
        else:
            index = int(self.cbAutomaton.get().split(' - ')[0]) - 1
            messagebox.showinfo('Información',self.ctrl.validateString(index,self.string1.get()))

    def getRoute(self):
        if self.string1.get().replace(' ','') == '':
            messagebox.showinfo('Información','Ingrese una cadena para validar')
        elif self.cbAutomaton.get() == 'Seleccione un Autómata':
            messagebox.showinfo('Información','No se ha seleccionado un autómata')
        else:
            index = int(self.cbAutomaton.get().split(' - ')[0]) - 1
            if self.ctrl.validateString(index,self.string1.get()) == 'Cadena Válida':
                self.route.configure(text=f'Ruta: \n{self.ctrl.returnRoute(index,self.string1.get())}')
            else:
                messagebox.showinfo('Información',self.ctrl.returnRoute(index,self.string1.get()))
                self.route.configure(text=f'Ruta: ')

    def viewAutomaton(self,event):
        index = int(self.cbAutomaton.get().split(' - ')[0]) - 1
        self.alphabet.configure(text=f'Alfabeto: {self.ctrl.getAlphabet(index)}')

    def option1(self):
        self.Panel2.grid_remove()
        self.Panel1.grid()
        self.getRoute()

    def option2(self):
        self.Panel1.grid_remove()
        self.Panel2.grid()