""" Practicing with different ways to design state machines.
    Treating state methods as first-class functions, 
    returning next state.
    
    https://en.wikipedia.org/wiki/First-class_function
    
    Michael A. Goodrich
    31 January 2023 
"""

class colonDash_FSM:
    def __init__(self):
        self.FSA_name = "colon-dash state machine"
        self.start_state = self.S0  # Initialize the starting state
        self.num_chars_read = 0
        self.accept_states = set()
        self.accept_states.add(self.S2)
        self.input_string = ""
        
    def Run(self,input_string):
        self.input_string = input_string
        current_state = self.start_state
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
        if current_state in self.accept_states:
            return True # Output this if the FSA ended in an accept state
        else: 
            return False # Output this if the FSA ended in anything other than an accept state
    
    def S0(self):
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

def main():
    my_FSM = colonDash_FSM()

    input_string = ":-"
    accept_status = my_FSM.Run(input_string)
    print("The output of ", my_FSM.get_FSA_Name(), " was ", accept_status," when the input was ",input_string)

    input_string = ":"
    accept_status = my_FSM.Run(input_string)
    print("The output of ", my_FSM.get_FSA_Name(), " was ", accept_status," when the input was ",input_string)


main()