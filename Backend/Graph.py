from Backend.ATP import ATP
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
        dot += f'\nProducciones:<br align="left"/>'

        items = ''
        for transition in automaton.transitions:
            items += f'\n{transition.origin}, {transition.entrance}, {transition.stackOutput}, {transition.destiny}, {transition.stackInput} <br align="left"/>'
        dot += f'{items}\n>\n];'
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

        os.system('dot -Tpdf Reports/ReportSA.txt -o Reports/ReportSA.pdf')
        webbrowser.open('Reports\ReportSA.pdf')

    def generateTable(self,table : list,name):
        dot = 'digraph structs {\ntitulo [shape=none label = "' + name + '" fontsize=30];\nnode [shape=record];\nstruct [label="'
        dot += '\n{<f0> Iteración|'
        items = ''
        for i in range(len(table)):
            if i < len(table) - 1:
                items += f'<f{i + 1}>{i}|'
            else:
                items += f'<f{i + 1}>{i}'
        dot += items
        dot += '}|'

        dot += '\n{<f0> Pila|'
        items = ''
        for i in range(len(table)):
            if i < len(table) - 1:
                items += f'<f{i + 1}>{table[i][0]}|'
            else:
                items += f'<f{i + 1}>{table[i][0]}'
        dot += items
        dot += '}|'

        dot += '\n{<f0> Entrada|'
        items = ''
        for i in range(len(table)):
            if i < len(table) - 1:
                items += f'<f{i + 1}>{table[i][1]}|'
            else:
                items += f'<f{i + 1}>{table[i][1]}'
        dot += items
        dot += '}|'

        dot += '\n{<f0> Transición|'
        items = ''
        for i in range(len(table)):
            if i < len(table) - 1:
                items += f'<f{i + 1}>{table[i][2]}|'
            else:
                items += f'<f{i + 1}>{table[i][2]}'
        dot += items
        dot += '}'

        dot += '"\n];\ntitulo -> struct [color=none];\n}'

        with open('Reports/ReportPass.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system('dot -Tpdf Reports/ReportPass.txt -o Reports/ReportPass.pdf')
        webbrowser.open('Reports\ReportPass.pdf')