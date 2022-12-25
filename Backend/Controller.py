from Backend.GLC import *
from Backend.ATP import *
from Backend.Graph import dotReports

class Controller:
    def __init__(self) -> None:
        self.grammars = []
        self.stackAutomata = []
        self.line = 0

    # Lectura del archivo y creación de objetos
    def popLine(self):
        try:
            return self.inputFile.pop(0)
        except:
            return None

    def viewLine(self):
        try:
            return self.inputFile[0]
        except:
            return None

    def identifyElementsGLC(self):
        if self.line == 0:
            self.grammar = GLC()
            self.grammar.name = self.popLine()
        elif self.line == 1:
            self.grammar.nonTerminals = self.popLine().split(',')
        elif self.line == 2:
            self.grammar.terminals = self.popLine().split(',')
        elif self.line == 3:
            self.grammar.initialNonTerminal = self.popLine()
        elif self.line == 4:
            self.productions = []
            self.isValid = True
            self.isGLC = False
        if self.line >= 4:
            production = self.popLine().split('>')
            destinationInput = production[1].split(' ')
            production[1] = [s for s in destinationInput if s]
            production[0] = production[0].replace(' ','')
            if not production[0] in self.grammar.nonTerminals:
                self.isValid = False
            if len(production[1]) == 1:
                if production[1][0] in self.grammar.nonTerminals:
                    self.productions.append(Production(production[0],destiny=production[1][0]))
                elif production[1][0] in self.grammar.terminals:
                    self.productions.append(Production(production[0],input1=production[1][0]))
                else: self.isValid = False
            elif len(production[1]) == 2:
                if production[1][0] in self.grammar.terminals and production[1][1] in self.grammar.nonTerminals:
                    self.productions.append(Production(production[0],production[1][0],production[1][1]))
                else: self.isValid = False
            elif len(production[1]) == 3:
                if production[1][0] in self.grammar.terminals and production[1][1] in self.grammar.nonTerminals and production[1][2] in self.grammar.terminals:
                    self.productions.append(Production(production[0],production[1][0],production[1][1],production[1][2]))
                    self.isGLC = True
                else: self.isValid = False

        self.line += 1
        if self.viewLine() == '%':
            if self.isValid and self.isGLC:
                self.grammar.productions = self.productions
                self.grammars.append(self.grammar)
            self.popLine()
            self.line = 0
        if self.viewLine():
            self.identifyElementsGLC()

    def grammarRecognition(self):
        self.inputFile = self.inputFile.split('\n')
        self.identifyElementsGLC()

    def readFileGLC(self,route):
        #ruta = '../Gramatica.glc'
        self.inputFile = open(route,encoding='utf-8').read()

    # mostrar objetos
    def showGrammar(self):
        for grammar in self.grammars:
            print('Nombre: ',grammar.name)
            print('No terminales: ',grammar.nonTerminals)
            print('Terminales: ',grammar.terminals)
            print('No terminal inicial',grammar.initialNonTerminal)
            print('Producciones')
            for production in grammar.productions:
                print('-',production.__dict__)
            print()

    # ---------------------------------------------
    # módulo autómata de pila
    def identifyElementsAPL(self):
        if self.line == 0:
            self.automaton = ATP()
            self.automaton.name = self.popLine()
        elif self.line == 1:
            self.automaton.alphabet = self.popLine().split(',')
        elif self.line == 2:
            self.automaton.stackSymbols = self.popLine().split(',')
        elif self.line == 3:
            self.automaton.states = self.popLine().split(',')
        elif self.line == 4:
            self.automaton.initialState = self.popLine()
        elif self.line == 5:
            self.automaton.acceptingStates = self.popLine().split(',')
        elif self.line == 6:
            self.transitions = []
        if self.line >= 6:
            transition = self.popLine().split(';')
            transition[0] = transition[0].split(',')
            transition[1] = transition[1].split(',')
            self.transitions.append(Transition(transition[0][0],transition[0][1],transition[0][2],transition[1][0],transition[1][1]))

        self.line += 1
        if self.viewLine() == '%':
            self.automaton.transitions = self.transitions
            self.stackAutomata.append(self.automaton)
            self.popLine()
            self.line = 0
        if self.viewLine():
            self.identifyElementsAPL()

    def showAutomaton(self):
        for automaton in self.stackAutomata:
            print('Nombre: ',automaton.name)
            print('Alfabeto: ',automaton.alphabet)
            print('Simbolos de pila: ',automaton.stackSymbols)
            print('Estados: ',automaton.states)
            print('Estado inicial: ',automaton.initialState)
            print('Estado de aceptación: ',automaton.acceptingStates)
            print('Transiciones: ')
            for transition in automaton.transitions:
                print('-',transition.__dict__)
            print()

    def automatonRecognition(self):
        self.inputFile = self.inputFile.split('\n')
        self.identifyElementsAPL()

    def readFileAPL(self,route):
        #ruta = '../Automata.apl'
        self.inputFile = open(route,encoding='utf-8').read()