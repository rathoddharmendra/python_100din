# type: ignore

import pandas, os
from turtle import Turtle
from name import Name

data_file_path = os.path.join(os.path.dirname(__file__),'50_states.csv')

class States:
    def __init__(self):
        self.states_data = pandas.read_csv(data_file_path)
        # self.states_list = [state.lower() for state in self.states_data.state.to_list()]
        self.guessed_states = []
        

    def find_state_by_name(self, name: str):
        if name.title() in self.guessed_states:
            return False
        if name.title() in self.states_data.state.to_list():
            try:
                state = self.states_data[self.states_data['state'] == name.title()]
            
                x = int(state.x.values[0])
                y = int(state.y.values[0])
                state_name = state.state.values[0]
                new_state = Name(x=state.x.item(), y=state.y.item(), name=state.state.item())
                # new_state = Name(x=x, y=y, name=state_name)
                self.guessed_states.append(state_name)  # add guessed state to list
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                return False
            
            return True
        else:
            return False

    # def create_unguessed_states(self):
    #     unguessed_states = [state for state in self.states_data.state.to_list() if state not in self.guessed_states]
    #     return unguessed_states
    
    def create_unguessed_states_csv(self):
        # Filter unguessed states by excluding guessed states
        print(~self.states_data.state.isin(self.guessed_states))
        print(type(~self.states_data.state.isin(self.guessed_states)))
        unguessed_states = self.states_data[~self.states_data.state.isin(self.guessed_states)]
        
        # Save the unguessed states to a CSV file
        unguessed_states.to_csv(os.path.join(os.path.dirname(__file__),'read_unguessed_states.csv'), index=False)
        
        # Print the shape of the remaining states
        print(unguessed_states.shape)


# states = States()
# state = states.states_data[states.states_data['state'] == 'Louisiana']
# print(states.states_data.state.to_list())
# print(type(int(state.x.values[0])))
# print(states.find_state_by_name('Louisiana'))
