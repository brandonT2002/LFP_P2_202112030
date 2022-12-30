from Backend.ATP import ATP
from Backend.GLC import GLC
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
        dot += f'\nTransiciones:<br align="left"/>'

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

    def generateStepByStep(self,automaton : ATP,stack,entry,origin,destiny,i):
        dot = 'digraph G {\ngraph [labelloc=t];\nnode [shape=circle style=filled fillcolor="#ffffff"];\nfontsize=30;\nlabel = "' + automaton.name +'";\nrankdir=LR;'

        items = ''
        for state in automaton.states:
            items += f'{state};'
        dot += items

        if origin != '':
            dot += f'{origin} [fillcolor="#83BD75"]'
        else:
            items = ''
            for accepted in automaton.acceptingStates:
                items += f'\n{accepted} [fillcolor="#83BD75"];'
            dot += items

        items = ''
        for accepted in automaton.acceptingStates:
            items += f'\n{accepted} [peripheries=2];'
        dot += items

        items = ''
        for transition in automaton.transitions:
            if origin == transition.origin and destiny == transition.destiny:
                    items += f'\n{transition.origin} -> {transition.destiny} [label="{transition.entrance},{transition.stackOutput};{transition.stackInput}" fontcolor="#FF1E1E"];'
            else:
                items += f'\n{transition.origin} -> {transition.destiny} [label="{transition.entrance},{transition.stackOutput};{transition.stackInput}"];'
        dot += items

        dot += '\nnode [shape=record];\nstack [label="\n{<f0> Pila}|\n{<f0> ' + stack + '}"\n];\nentry [label="\n{<f0> entrada}|\n{<f0> ' + entry + '}"\n];'

        dot += '\n}'

        with open(f'Image/Steps/Step{i}.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system(f'dot -Tpng Image/Steps/Step{i}.txt -o Image/Steps/Step{i}.png')

    def generateGReport(self,grammar : GLC):
        dot = 'digraph G {\nNode[shape=none];\nlabelloc=t;\nfontsize=30;\nlabel = "' + grammar.name +'";\nL[label=<'

        dot += f'\nNo terminales: {", ".join(grammar.nonTerminals)}<br align="left"/>'
        dot += f'\nTerminales: {", ".join(grammar.terminals)}<br align="left"/>'
        dot += f'\nNo terminal inicial: {", ".join(grammar.initialNonTerminal)}<br align="left"/>'
        dot += f'\nProducciones:<br align="left"/>'

        path = grammar.path
        for k,v in path.items():
            dot += f'\n{k} &#62;'
            for k1,v1 in v.items():
                if k1 == 'exp0':
                    if v1['input1']:
                        dot += ' ' + v1['input1']
                    if v1['destiny']:
                        dot += ' ' + v1['destiny']
                    if v1['input2']:
                        dot += ' ' + v1['input2']
                    dot += '<br align="left"/>'
                else:
                    dot += '\n      |'
                    if v1['input1']:
                        dot += ' ' + v1['input1']
                    if v1['destiny']:
                        dot += ' ' + v1['destiny']
                    if v1['input2']:
                        dot += ' ' + v1['input2']
                    dot += '<br align="left"/>'
        dot += '>]\n}'

        with open('Reports/ReportG.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system('dot -Tpng Reports/ReportG.txt -o Reports/ReportG.png')

    def nodes(self,productions,i):
        node = ''
        if i < len(productions):
            production = productions[i]
            node += f'\n{i} [label = "{production.origin}" group="0"];'
            if production.input1:
                node += f'\n{i}1 [label = "{production.input1}" group="1"];'
            if production.input2:
                node += f'\n{i}2 [label = "{production.input2}" group="2"];'
            node += self.nodes(productions,i + 1)
        return node

    def subgraphs(self,productions,i):
        subgraph = ''
        if i < len(productions):
            production = productions[i]
            if i < len(productions) - 1:
                if production.input1 or production.input2:
                    subgraph += '\nsubgraph {\nrank = same;\n'
                    subgraph += f'{i}1'
                    if production.input1:
                        subgraph += f' -> {i + 1}'
                    if production.input2:
                        subgraph += f' -> {i}2'
                    subgraph += '[color=none];\n}'
            subgraph += self.subgraphs(productions,i + 1)
        return subgraph

    def links(self,productions,i):
        link = ''
        if i < len(productions):
            production = productions[i]
            if i > 0:
                link += f'\n{i - 1} -> {i};'
            if production.input1:
                link += f'\n{i} -> {i}1;'
            if production.input2:
                link += f'\n{i} -> {i}2;'
            link += self.links(productions,i + 1)
        return link

    def branchTree(self,productions,i):
        dot = 'digraph G {\nNode[shape=none];\nEdge[arrowhead=none];'
        dot += self.nodes(productions,i)
        dot += self.subgraphs(productions,i)
        dot += self.links(productions,i)
        dot += '\n}'

        with open('Reports/BranchTree.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system('dot -Tpng Reports/BranchTree.txt -o Reports/BranchTree.png')
        webbrowser.open('Reports\BranchTree.png')