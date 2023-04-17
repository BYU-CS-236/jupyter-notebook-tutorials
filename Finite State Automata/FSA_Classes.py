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

class FSA:
    """ FSA Base or Super class"""
    def __init__(self,name):
        """ Finite state automata must have a 
        • set of states 
        • start state
        • input alphabet
        • set of accept states
        • transition function
        """
        self.FSA_name = name        # name of your state machine
        self.start_state = self.S0  # start state always named S0 in this implementation
        self.accept_states = set()  # set of accept states must be specified in derived class
        self.input_string = ""      # input string and
        self.num_chars_read = 0     # current input character
    
    def Run(self,input_string):
        """ The workhorse of the FSA shared by all the FSAs in project 1.
        • record the input string
        • initialize the start state
        • while there are still characters to read in the input string ...
        • transition between states
        • return something useful if the final state is an accept state """
        self.input_string = input_string
        current_state = self.start_state
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
        if current_state in self.accept_states:
            return True # Output this if the FSA ended in an accept state
        else: 
            return False # Output this if the FSA ended in anything other than an accept state
    def Reset(self):
        self.num_chars_read = 0
        self.input_string = ""
    def S0(self):
        """ Every FSA must have a start state, and we'll always name 
        it S0. The method for the start state must be defined in the
        derived class since it's not defined here. """
        pass
    def get_FSA_Name(self): return self.FSA_name

class colonDash_FSA(FSA):
    def __init__(self,name):
        FSA.__init__(self,name) # You must invoke the __init__ of the parent class
        self.accept_states.add(self.S2)
    def S0(self):
        """ define the start state in the derived class """
        #print("In state S0. S0's information is ",self.S0)
        if self.input_string[self.num_chars_read] != ':': next_state = self.Serr
        else: next_state = self.S1
        self.num_chars_read += 1
        return next_state
    def S1(self):
        #print("In state S1. S1's information is ",self.S1)
        if self.input_string[self.num_chars_read] != '-': next_state = self.Serr
        else: next_state = self.S2
        self.num_chars_read += 1
        return next_state
    def S2(self):
        #print("In state S2. S2's information is ",self.S2)
        next_state = self.Serr # if any inputs, go to error state
        self.num_chars_read += 1
        return next_state
    def Serr(self):
        #print("In state Serr. Serr's information is ",self.Serr)
        next_state = self.Serr # stay in error state on all inputs
        self.num_chars_read += 1
        return next_state
    def get_FSA_Name(self): return self.FSA_name
class colon_FSA(FSA):
    def __init__(self,name):
        FSA.__init__(self,name) # You must invoke the __init__ of the parent class
        self.accept_states.add(self.S1)
    def S0(self):
        """ define the start state in the derived class """
        if self.input_string[self.num_chars_read] != ':': next_state = self.Serr
        else: next_state = self.S1
        self.num_chars_read += 1
        return next_state
    def S1(self):
        next_state = self.Serr # if any inputs, go to error state
        self.num_chars_read += 1
        return next_state
    def Serr(self):
        next_state = self.Serr # stay in error state on all inputs
        self.num_chars_read += 1
        return next_state

class LParen_FSA(FSA):
    def __init__(self,name):
        FSA.__init__(self,name) # You must invoke the __init__ of the parent class
        self.accept_states.add(self.S1)
    def S0(self):
        """ define the start state in the derived class """
        #print("In state S0. S0's information is ",self.S0)
        if self.input_string[self.num_chars_read] != '(': next_state = self.Serr
        else: next_state = self.S1
        self.num_chars_read += 1
        return next_state
    def S1(self):
        #print("In state S1. S1's information is ",self.S1)
        next_state = self.Serr # if any inputs, go to error state
        self.num_chars_read += 1
        return next_state
    def Serr(self):
        #print("In state Serr. Serr's information is ",self.Serr)
        next_state = self.Serr # stay in error state on all inputs
        self.num_chars_read += 1
        return next_state
