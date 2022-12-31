class Stack(list):
    def checkPop(self,pop):
        if len(self) == 0 and pop == '$':
            return True
        if len(self) > 0 and pop != '$':
            if pop == self[len(self) - 1]:
                return True
        if len(self) > 0 and pop == '$':
            return True
        return False

    def popStack(self,pop):
        if pop != '$':
            if pop == self[len(self) - 1]:
                self.pop()

    def addStack(self,add):
        if add != '$':
            self.append(add)