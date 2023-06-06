from fsa_base_class_definition import FSA
from typing import Callable as function

class ColonDashFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "ColonDashFSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.s2) # Since self.accept_states is defined in parent class, I can use it here
    
    def s0(self) -> function:
        current_input: str = self._get_current_input()
        next_state: function = None
        if current_input == ':': next_state = self.s1
        else: next_state = self.s_err
        return next_state

    def s1(self) -> function:
        current_input: str = self._get_current_input()
        next_state: function = None
        if current_input == '-': next_state = self.s2
        else: next_state = self.s_err
        return next_state

    def s2(self) -> function:
        current_input: str = self._get_current_input()
        next_state: function = self.s2 # loop in state s2
        return next_state

    def s_err(self) -> function:
        current_input: str = self._get_current_input()
        next_state: function = self.s_err # loop in state s_err
        return next_state
    
class ColonFSA(FSA):
    def __init__(self):
        FSA.__init__(self,"ColonFSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.s1) # Since self.accept_states is defined in parent class, I can use it here
    
    def s0(self):
        current_input: str = self._get_current_input()
        next_state: function = None
        if current_input == ':': next_state = self.s1
        else: next_state = self.s_err
        return next_state

    def s1(self):
        current_input: str = self._get_current_input()
        next_state: function = self.s1 # loop in state s1
        return next_state

    def s_err(self):
        current_input = self._get_current_input()
        next_state: function = self.s_err # loop in state s_err
        return next_state
    
class LeftParenFSA(FSA):
    def __init__(self):
        FSA.__init__(self, "LeftParenFSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.s1) # Since self.accept_states is defined in parent class, I can use it here
    
    def s0(self):
        current_input: str = self._get_current_input()
        next_state: function = None
        if current_input == '(': next_state = self.s1
        else: next_state = self.s_err
        return next_state

    def s1(self):
        current_input: str = self._get_current_input()
        next_state: function = self.s1 # loop in state s1
        return next_state
    def s_err(self):
        current_input: str = self._get_current_input()
        next_state: function = self.s_err # loop in state s_err
        return next_state

class RightParenFSA(FSA):
    def __init__(self):
        FSA.__init__(self, "RightParenFSA") # You must invoke the __init__ of the parent class
        self.accept_states.add(self.s1) # Since self.accept_states is defined in parent class, I can use it here

    def s0(self):
        current_input: function = self._get_current_input()
        next_state: function = None
        if current_input == ')': next_state = self.s1
        else: next_state = self.s_err
        return next_state

    def s1(self):
        current_input: str = self._get_current_input()
        next_state: function = self.s1 # loop in state s1
        return next_state

    def s_err(self):
        current_input: str = self._get_current_input()
        next_state: function = self.s_err # loop in state s_err
        return next_state