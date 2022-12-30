from Backend.GLC import *
from Backend.ATP import *
from Backend.Stack import Stack
from Backend.Graph import dotReports
import os

class Controller:
    def __init__(self) -> None:
        self.grammars = []
        self.stackAutomata = []
        self.line = 0
        self.count = 0

    # validaciones de lectura
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

    # ---------------------------------------------
    # módulo gramática libre de contexto
    def getPathGLC(self):
        path = self.grammar.path
        for i in self.grammar.productions:
            path[i.origin]['exp' + str(len(path[i.origin]))] = {'input1':i.input1,'destiny':i.destiny,'input2':i.input2}
        return path

    def identifyElementsGLC(self):
        if self.line == 0:
            self.grammar = GLC()
            self.grammar.name = self.popLine()
        elif self.line == 1:
            self.grammar.nonTerminals = self.popLine().split(',')
            for nonTerminal in self.grammar.nonTerminals:
                self.grammar.path[nonTerminal] = {}
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
                self.grammar.path = self.getPathGLC()
                self.grammars.append(self.grammar)
            self.popLine()
            self.count = 0
            self.line = 0
        if self.viewLine():
            self.identifyElementsGLC()

    def generatedReportG(self,index):
        dotReports().generateGReport(self.grammars[index])

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
            print(grammar.path)
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
            for state in self.automaton.states:
                self.automaton.path[state] = {}
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
            try:
                dictionary = {}
                dictionary['destiny'] = transition[1][0]
                dictionary['pop'] = transition[0][2]
                dictionary['add'] = transition[1][1]
                self.automaton.path[transition[0][0]][transition[0][1]] = dictionary
            except: pass

        self.line += 1
        if self.viewLine() == '%':
            self.automaton.transitions = self.transitions
            self.stackAutomata.append(self.automaton)
            self.popLine()
            self.line = 0
        if self.viewLine():
            self.identifyElementsAPL()

    def getKeys(self,transitions):
        keys = []
        for k in transitions:
            keys.append(k)
        return keys

    def rewritePast(self,pass_,accumulated):
        for i in range(len(pass_) - 1,0,-1):
            pass_[i][0] = pass_[i - 1][0]
        pass_[0][0] = ''
        pass_.append(['',accumulated.replace('$',''),''])
        return pass_

    def evaluateStack(self,path,state,transitions,entry,acceptance,string,stack : Stack,acumulated,route,pass_):
        transition = transitions[entry]
        if stack.checkPop(transition['pop']):
            stack.popStack(transition['pop'])
            stack.addStack(transition['add'])
            t = '{}, {}, {}; {}, {}'.format(state,entry,transition['pop'],transition['destiny'],transition['add'])
            route.append(t)
            acumulated += entry
            pass_.append([''.join(stack),acumulated.replace('$',''),t])
            return self.evaluateCharacters(path,transition['destiny'],acceptance,string,stack,acumulated,route,pass_ )

    def evaluateCharacters(self,path,state,acceptance,string,stack : Stack,acumulated,route,pass_):
        transitions = path[state]
        keys = self.getKeys(transitions)
        if len(string) == 0:
            if len(stack) == 0 and state in acceptance:
                return True, route, self.rewritePast(pass_,acumulated)
            if '$' in keys:
                return self.evaluateStack(path,state,transitions,'$',acceptance,'',stack,acumulated,route,pass_)
        if len(string) > 0:
            if string[0] in keys:
                return self.evaluateStack(path,state,transitions,string[0],acceptance,''.join(string[1:]),stack,acumulated,route,pass_)
            if '$' in keys:
                return self.evaluateStack(path,state,transitions,'$',acceptance,string,stack,acumulated,route,pass_)
        return False

    # generando reportes
    def generatedReport(self,index):
        dotReports().generateSAReport(self.stackAutomata[index])

    # enviando valores al frontend
    def validateString(self,index,string):
        path = self.stackAutomata[index].path
        initial = self.stackAutomata[index].initialState
        accepting = self.stackAutomata[index].acceptingStates

        isValid = self.evaluateCharacters(path,initial,accepting,string,Stack(),'',[],[])
        if isValid:
            return 'Cadena Válida'
        else:
            return 'Cadena Invalida'

    def returnRoute(self,index,string):
        path = self.stackAutomata[index].path
        initial = self.stackAutomata[index].initialState
        accepting = self.stackAutomata[index].acceptingStates

        isValid = self.evaluateCharacters(path,initial,accepting,string,Stack(),'',[],[])
        if isValid:
            return '\n'.join(isValid[1])
        else:
            return 'Verifique la Cadena'

    def generateStep(self,index,string):
        path = self.stackAutomata[index].path
        initial = self.stackAutomata[index].initialState
        accepting = self.stackAutomata[index].acceptingStates

        isValid = self.evaluateCharacters(path,initial,accepting,string,Stack(),'',[],[])
        if isValid:
            self.steps = 0
            directory = 'Image/Steps'
            for f in os.listdir(directory):
                os.remove(os.path.join(directory,f))
            for i in range(len(isValid[2])):
                route = isValid[2][i][2].replace(' ','')
                route = route.split(';')
                if len(route) > 1:
                    route[0] = route[0].split(',')
                    route[1] = route[1].split(',')
                    dotReports().generateStepByStep(self.stackAutomata[index],isValid[2][i][0],isValid[2][i][1],route[0][0],route[1][0],i)
                elif len(route) < 2:
                    dotReports().generateStepByStep(self.stackAutomata[index],isValid[2][i][0],isValid[2][i][1],'','',i)
                self.steps += 1
            #print('steps ',self.steps)
        else:
            return 'Verifique la Cadena'

    def generateTable(self,index,string):
        path = self.stackAutomata[index].path
        initial = self.stackAutomata[index].initialState
        accepting = self.stackAutomata[index].acceptingStates

        isValid = self.evaluateCharacters(path,initial,accepting,string,Stack(),'',[],[])
        if isValid:
            dotReports().generateTable(isValid[2],self.stackAutomata[index].name)
        else:
            return 'Verifique la Cadena'

    def getAlphabet(self,index):
        return ', '.join(self.stackAutomata[index].alphabet)

    def showAutomaton(self):
        for automaton in self.stackAutomata:
            print('Nombre: ',automaton.name)
            print('Alfabeto: ',automaton.alphabet)
            print('Simbolos de pila: ',automaton.stackSymbols)
            print('Estados: ',automaton.states)
            print('Estado inicial: ',automaton.initialState)
            print('Estado de aceptación: ',automaton.acceptingStates)
            print(automaton.path)
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