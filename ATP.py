class ATP:
    def __init__(self):
        self.name = None
        self.alphabet = None
        self.stackSymbols = None
        self.initialState = None
        self.acceptanceState = None

class Transition:
    def __init__(self,origin,entrance,stackOutput,destiny,stackInput):
        self.origin = origin
        self.entrance = entrance
        self.stackOutput = stackOutput
        self.destiny = destiny
        self.stackInput = stackInput