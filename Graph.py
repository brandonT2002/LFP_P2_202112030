from ATP import ATP
import os
import webbrowser

class dotReports:
    def generateSAReport(self,automaton : ATP):
        dot = 'digraph G {\ngraph [labelloc=t];\nnode [shape=circle];\nfontsize=30;\nlabel = "' + automaton.name + '";NodeLabel [shape=none fontsize=18 label = \n<'

        dot += f'\nAlfabeto: {", ".join(automaton.alphabet)}<br align="left"/>'
        dot += f'\nAlfabeto de pila: {", ".join(automaton.stackSymbols)}<br align="left"/>'
        dot += f'\nEstados: {", ".join(automaton.states)}<br align="left"/>'
        dot += f'\nEstado inicial: {automaton.initialState}<br align="left"/>'
        dot += f'\nEstados de aceptación: {",".join(automaton.acceptingStates)}<br align="left"/>'

        items = ''
        dot += f'\n>\n];'
        dot += '\nrankdir=LR;\n'

        items = ''
        for state in automaton.states:
            items += f'{state};'
        dot += items

        items = ''
        for accepted in automaton.acceptingStates:
            items += f'\n{accepted} [peripheries=2];'
        dot += items

        dot += f'\nNodeLabel -> {automaton.initialState} [color=none];'

        items = ''
        for transition in automaton.transitions:
            items += f'\n{transition.origin} -> {transition.destiny} [label="{transition.entrance},{transition.stackOutput};{transition.stackInput}"];'
        dot += items
        dot += '\n}'

        with open('Reports/ReportSA.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system('dot -Tpdf Reports/ReportSA.txt -o ReportSA.pdf')
        webbrowser.open('ReportSA.pdf')