from FSA_BaseClass_Definition import FSA

class ColonDash_FSA(FSA):
    def __init__(self):
        FSA.__init__(self,"colonDash_FSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.S2) # Since self.accept_states is defined in parent class, I can use it here
    
    def S0(self):
        current_input = self._FSA__getCurrentInput()
        if current_input == ':': next_state = self.S1
        else: next_state = self.Serr
        return next_state
    def S1(self):
        current_input = self._FSA__getCurrentInput()
        if current_input == '-': next_state = self.S2
        else: next_state = self.Serr
        return next_state
    def S2(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.S2 # loop in state S2
        return next_state
    def Serr(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.Serr # loop in state Serr
        return next_state
    
class Colon_FSA(FSA):
    def __init__(self):
        FSA.__init__(self,"colon_FSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.S1) # Since self.accept_states is defined in parent class, I can use it here
    
    def S0(self):
        current_input = self._FSA__getCurrentInput()
        if current_input == ':': next_state = self.S1
        else: next_state = self.Serr
        return next_state
    def S1(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.S1 # loop in state S1
        return next_state
    def Serr(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.Serr # loop in state Serr
        return next_state
    
class LeftParen_FSA(FSA):
    def __init__(self):
        FSA.__init__(self,"leftParen_FSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.S1) # Since self.accept_states is defined in parent class, I can use it here
    
    def S0(self):
        current_input = self._FSA__getCurrentInput()
        if current_input == '(': next_state = self.S1
        else: next_state = self.Serr
        return next_state
    def S1(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.S1 # loop in state S1
        return next_state
    def Serr(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.Serr # loop in state Serr
        return next_state

class RightParen_FSA(FSA):
    def __init__(self):
        FSA.__init__(self,"rightParen_FSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.S1) # Since self.accept_states is defined in parent class, I can use it here
    def S0(self):
        current_input = self._FSA__getCurrentInput()
        if current_input == ')': next_state = self.S1
        else: next_state = self.Serr
        return next_state
    def S1(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.S1 # loop in state S1
        return next_state
    def Serr(self):
        current_input = self._FSA__getCurrentInput()
        next_state = self.Serr # loop in state Serr
        return next_state