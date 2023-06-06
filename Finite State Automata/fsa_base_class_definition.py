from typing import Callable as function
class FSA:
    """ FSA Base or Super class"""
    def __init__(self, name: str) -> None:
        """ Class constructor """
        ###############################################################
        # Define the five elements of the FSA
        ###############################################################
        # Set of states: Each state S0, S1, S2, Serr will be represented by its own function
        # Set of inputs: I is the set of alphanumeric characters, checked by isalnum()
        self.start_state: function = self.s0  # We'll always have the start state named S0
        self.accept_states: set[function] = set()  # No accept states defined
        # Transition function: Each transition will be defined in the state functions
        
        ###############################################################
        # Define four variables that are used within the FSA, some
        # to make the FSA run and some that help us understand how 
        # the FSA works
        ###############################################################
        self.input_string: str = ""      # Default empty input
        self.fsa_name: str = name
        self.num_chars_read: int = 0
            
    #########################################################
    # Define each state as a function                       #
    # Within each function, define the transition function. #
    # Each transition function reads the current input and  #
    # choose the next state based on the input              #
    #########################################################
    def s0(self) -> NotImplemented:
        """ Every FSA must have a start state, and we'll always name 
        it S0. The function for the start state must be defined in the
        derived class since it's not defined here. """
        raise NotImplementedError()     # This line causes an error to 
                                        # occur if the child classes don't implement this function

    ############################
    # Public Manager Functions
    ############################
    def run(self, input_string: str) -> bool:
        ###############################################################
        # This function will be called to make the FSA execute
        # It records the input string,
        # sets the current state to the start state
        # and then calls a state function that returns the next state
        # Each state function accesses the input_string
        ###############################################################
            # Remember input_string
        self.input_string = input_string
            # Set current state to start state
        current_state: function = self.start_state
            # Call current state, which starts the FSA
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
            # Check whether the FSA ended in an accept state
        outcome: bool = False 
        if current_state in self.accept_states: outcome = True # Accept if the FSA ended in an accept state
        return outcome
    
    def reset(self) -> None:
        self.num_chars_read = 0
        self.history = []
    
    ############################
    # Public Getters and Setters
    ############################
    def get_name(self) -> str: return self.fsa_name
    def set_name(self, fsa_name: str) -> None: self.fsa_name = fsa_name
    
    ############################
    # Private Helper functions
    ############################
    def _get_current_input(self) -> str:  # The double underscore makes the function private
        current_input: str = self.input_string[self.num_chars_read]
        self.num_chars_read += 1
        return current_input