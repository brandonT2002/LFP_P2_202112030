from Backend.Controller import Controller
from Backend.Graph import dotReports
ctrl = Controller()
ctrl.readFileGLC('Gramatica.glc')
ctrl.grammarRecognition()
print('---GRAMATICAS LIBRES DE CONTEXTO---')
#ctrl.showGrammar()

ctrl.readFileAPL('Automata.apl')
ctrl.automatonRecognition()
print('---AUTOMATAS DE PILA---')
#ctrl.showAutomaton()

#print(ctrl.stackAutomata[0])
gr = dotReports()
gr.generateSAReport(ctrl.stackAutomata[0])