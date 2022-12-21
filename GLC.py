class GLC:
    def __init__(self):
        self.name = None
        self.nonTerminal = None
        self.terminals = None
        self.initialNonTerminal = None
        self.productions = None

class Produccion:
    def __init__(self,origin,entrance1,destiny = '',entrance2 = ''):
        self.origin = origin
        self.entrance1 = entrance1
        self.destiny = destiny
        self.entrance2 = entrance2