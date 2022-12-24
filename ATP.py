class ATP:
    def __init__(self):
        self.name = None
        self.alphabet = None
        self.stackSymbols = None
        self.states = None
        self.initialState = None
        self.acceptingStates = None
        self.transitions = None

class Transition:
    def __init__(self,origin,entrance,stackOutput,destiny,stackInput):
        self.origin = origin
        self.entrance = entrance
        self.stackOutput = stackOutput
        self.destiny = destiny
        self.stackInput = stackInput