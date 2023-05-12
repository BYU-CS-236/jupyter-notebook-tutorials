class FSA:
    """ FSA Base or Super class"""
    def __init__(self,name):
        """ Class constructor """
        ###############################################################
        # Define the five elements of the FSA
        ###############################################################
        # Set of states: Each state S0, S1, S2, Serr will be represented by its own method
        # Set of inputs: I is the set of alphanumeric characters, checked by isalnum()
        self.start_state = self.S0  # We'll always have the start state named S0
        self.accept_states = set()  # No accept states defined
        # Transition function: Each transition will be defined in the state methods
        
        ###############################################################
        # Define four variables that are used within the FSA, some
        # to make the FSA run and some that help us understand how 
        # the FSA works
        ###############################################################
        self.input_string = ""      # Default empty input
        self.FSA_name = name
        self.num_chars_read = 0
            
    #########################################################
    # Define each state as a function                       #
    # Within each function, define the transition function. #
    # Each transition function reads the current input and  #
    # choose the next state based on the input              #
    #########################################################
    def S0(self):
        """ Every FSA must have a start state, and we'll always name 
        it S0. The method for the start state must be defined in the
        derived class since it's not defined here. """
        raise NotImplementedError()     # This line causes an error to 
                                        # occur if the child classes don't implement this method

    ############################
    # Public Manager Functions
    ############################
    def Run(self,input_string):
        ###############################################################
        # This function will be called to make the FSA execute
        # It records the input string,
        # sets the current state to the start state
        # and then calls a state method that returns the next state
        # Each state method accesses the input_string
        ###############################################################
            # Remember input_string
        self.input_string = input_string
            # Set current state to start state
        current_state = self.start_state
            # Call current state, which starts the FSA
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
            # Check whether the FSA ended in an accept state
        outcome = False 
        if current_state in self.accept_states: outcome = True # Accept if the FSA ended in an accept state
        return outcome
    def Reset(self):
        self.num_chars_read = 0
        self.history = []
    
    ############################
    # Public Getters and Setters
    ############################
    def get_Name(self): return self.FSA_name
    def set_Name(self,FSA_name): self.FSA_name = FSA_name
    
    ############################
    # Private Helper functions
    ############################
    def __getCurrentInput(self):  # The double underscore makes the method private
        current_input = self.input_string[self.num_chars_read]
        self.num_chars_read += 1
        return current_input