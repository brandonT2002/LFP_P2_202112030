from GLC import *

class ControllerGLC:
    def __init__(self) -> None:
        self.grammars = []
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

    def identifyElements(self):
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
        if self.line >= 5:
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
            self.identifyElements()

    def grammarRecognition(self):
        self.inputFile = self.inputFile.split('\n')
        self.identifyElements()

    def readFile(self):
        ruta = 'Gramatica.glc'
        self.inputFile = open(ruta,encoding='utf-8').read()

    # mostrar objetos
    def showGrammar(self):
        for grammar in self.grammars:
            print('Nombre: ',grammar.name)
            print('No terminales: ',grammar.nonTerminals)
            print('Terminales: ',grammar.terminals)
            print('No terminal inicial',grammar.initialNonTerminal)
            print('Producciones')
            for production in grammar.productions:
                print(production.__dict__)
            print()

ctrl = ControllerGLC()
ctrl.readFile()
ctrl.grammarRecognition()
ctrl.showGrammar()