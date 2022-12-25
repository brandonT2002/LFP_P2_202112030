class GLC:
    def __init__(self):
        self.name = None
        self.nonTerminals = None
        self.terminals = None
        self.initialNonTerminal = None
        self.productions = None

class Production:
    def __init__(self,origin,input1 = '',destiny = '',input2 = ''):
        self.origin = origin
        self.input1 = input1
        self.destiny = destiny
        self.input2 = input2