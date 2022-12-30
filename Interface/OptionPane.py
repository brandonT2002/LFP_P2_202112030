import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from Backend.Controller import Controller
from Interface.AutomatonPane import AutomatonPane
from Interface.GrammarPane import GrammarPane
from Interface.SplashScreen import SplashScreen

class OptionPane(tk.Frame):
    def __init__(self,root,grammar : GrammarPane,automaton : AutomatonPane):
        super().__init__(master=root,width=200)
        self.configure(bg='#2A2D2E')
        self.grid(row=0,column=0,sticky='nswe')

        self.ctrl = Controller()
        self.grammar = grammar
        self.automaton = automaton
        self.components()

    def components(self):
        self.grid_rowconfigure(0,minsize=10)
        self.grid_rowconfigure(7,weight=1)
        self.grid_rowconfigure(8,minsize=20)
        self.grid_rowconfigure(11,minsize=10)

        opciones = Label(master=self,text='Opciones',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        opciones.grid(row=1,column=0,pady=10,padx=10)

        self.upload = Button(master=self,text='Cargar Archivo',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.chooseFile)
        self.upload.grid(row=2,column=0,pady=10,padx=20)

        self.grammarMod = Button(master=self,text='Modulo Gramática',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.option1)
        self.grammarMod.grid(row=3,column=0,pady=10,padx=20)

        self.automatonMod = Button(master=self,text='Modulo Autómata',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=self.option2)
        self.automatonMod.grid(row=4,column=0,pady=10,padx=20)

        self.exit = Button(master=self,text='Salir',font=('Roboto Medium',11),bg='#D35B58',activebackground='#D35B58',foreground='white',activeforeground='white',width=15,height=1,cursor='hand2',command=quit)
        self.exit.grid(row=9,column=0,pady=10,padx=20)

    def chooseFile(self):
        try:
            formatos = (
                ("form files","*.glc"),
                ("form files","*.ap"),
            )
            archivo = askopenfilename(
                title='Abrir Archivo',
                initialdir='',
                filetypes = formatos)
            if not archivo == '':
                extension = archivo.split('.')
                if extension[1] == 'glc':
                    self.ctrl.readFileGLC(archivo)
                    self.ctrl.grammarRecognition()
                    self.ctrl.showGrammar()
                    self.nameGrammar = []
                    for i in range(len(self.ctrl.grammars)):
                        self.nameGrammar.append(f'{i + 1} - {self.ctrl.grammars[i].name}')
                    self.grammar.cbGrammar.configure(values=self.nameGrammar)
                elif extension[1] == 'ap':
                    self.ctrl.readFileAPL(archivo)
                    self.ctrl.automatonRecognition()
                    #self.ctrl.showAutomaton()
                    #self.ctrl.stackAutomata
                    self.nameAutomata = []
                    for i in range(len(self.ctrl.stackAutomata)):
                        self.nameAutomata.append(f'{i + 1} - {self.ctrl.stackAutomata[i].name}')
                    self.automaton.cbAutomaton.configure(values=self.nameAutomata)
                self.automaton.ctrl = self.ctrl
                self.grammar.ctrl = self.ctrl
        except: pass

    def option1(self):
        self.automaton.grid_remove()
        self.grammar.grid()

    def option2(self):
        self.grammar.grid_remove()
        self.automaton.grid()