class GLC:
    def __init__(self):
        self.name = None
        self.nonTerminals = None
        self.terminals = None
        self.initialNonTerminal = None
        self.productions = None
        self.path = {}

class Production:
    def __init__(self,origin,input1 = None,destiny = None,input2 = None):
        self.origin = origin
        self.input1 = input1
        self.destiny = destiny
        self.input2 = input2