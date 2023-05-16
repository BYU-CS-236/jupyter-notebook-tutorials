""" File containing the base class and all of the FSAs required
    for project 1.

    Augment the FSAs to grant access to the string that brought
    it to the accept state. We'll do this tracking the string that
    was read up to the time that we entered an accept state.
    This means that we are adding functionality over our base
    FSAs. This augmentation is relative to the FSA_example_with_inheritance.py
    
    Michael A. Goodrich
    Brigham  Young University
    
    15 February 2023
"""
from typing import Callable as function

class FSA:
    """ FSA Base or Super class"""
    def __init__(self, name: str):
        """ Finite state automata must have a 
        • set of states 
        • start state
        • input alphabet
        • set of accept states
        • transition function
        """
        self.fsa_name: str = name        # name of your state machine
        self.start_state: function = self.s0  # start state always named s0 in this implementation
        self.accept_states: set[function] = set()  # set of accept states must be specified in derived class
        self.input_string: str = ""      # input string and
        self.num_chars_read: int = 0     # current input character
    
    def run(self, input_string: str) -> bool:
        """ The workhorse of the FSA shared by all the FSAs in project 1.
        • record the input string
        • initialize the start state
        • while there are still characters to read in the input string ...
        • transition between states
        • return something useful if the final state is an accept state """
        self.input_string = input_string
        current_state: function = self.start_state
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
        if current_state in self.accept_states:
            return True # Output this if the FSA ended in an accept state
        else: 
            return False # Output this if the FSA ended in anything other than an accept state

    def reset(self) -> None:
        self.num_chars_read = 0
        self.input_string = ""

    def s0(self) -> NotImplemented:
        """ Every FSA must have a start state, and we'll always name 
        it s0. The method for the start state must be defined in the
        derived class since it's not defined here. """
        pass

    def get_fsa_name(self) -> str: return self.fsa_name

class ColonDashFSA(FSA):
    def __init__(self, name):
        FSA.__init__(self, name) # You must invoke the __init__ of the parent class
        self.accept_states.add(self.s2)

    def s0(self) -> function:
        """ define the start state in the derived class """
        #print("In state s0. s0's information is ",self.s0)
        next_state: function = None
        if self.input_string[self.num_chars_read] != ':': next_state = self.s_err
        else: next_state = self.s1
        self.num_chars_read += 1
        return next_state

    def s1(self) -> function:
        #print("In state s1. s1's information is ",self.s1)
        next_state: function = None
        if self.input_string[self.num_chars_read] != '-': next_state = self.s_err
        else: next_state = self.s2
        self.num_chars_read += 1
        return next_state

    def s2(self) -> function:
        #print("In state s2. s2's information is ",self.s2)
        next_state: function = self.s_err # if any inputs, go to error state
        self.num_chars_read += 1
        return next_state

    def s_err(self) -> function:
        #print("In state s_err. s_err's information is ",self.s_err)
        next_state = self.s_err # stay in error state on all inputs
        self.num_chars_read += 1
        return next_state

class ColonFSA(FSA):
    def __init__(self, name):
        FSA.__init__(self, name) # You must invoke the __init__ of the parent class
        self.accept_states.add(self.s1)

    def s0(self) -> function:
        """ define the start state in the derived class """
        next_state: function = None
        if self.input_string[self.num_chars_read] != ':': next_state = self.s_err
        else: next_state = self.s1
        self.num_chars_read += 1
        return next_state

    def s1(self) -> function:
        next_state: function = self.s_err # if any inputs, go to error state
        self.num_chars_read += 1
        return next_state

    def s_err(self) -> function:
        next_state: function = self.s_err # stay in error state on all inputs
        self.num_chars_read += 1
        return next_state

class LeftParenFSA(FSA):
    def __init__(self, name):
        FSA.__init__(self, name) # You must invoke the __init__ of the parent class
        self.accept_states.add(self.s1)

    def s0(self) -> function:
        """ define the start state in the derived class """
        #print("In state s0. s0's information is ",self.s0)
        next_state: function = None
        if self.input_string[self.num_chars_read] != '(': next_state = self.s_err
        else: next_state = self.s1
        self.num_chars_read += 1
        return next_state

    def s1(self) -> function:
        #print("In state s1. s1's information is ",self.s1)
        next_state: function = self.s_err # if any inputs, go to error state
        self.num_chars_read += 1
        return next_state

    def s_err(self) -> function:
        #print("In state s_err. s_err's information is ",self.s_err)
        next_state: function = self.s_err # stay in error state on all inputs
        self.num_chars_read += 1
        return next_state
