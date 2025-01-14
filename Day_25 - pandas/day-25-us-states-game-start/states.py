import pandas, os, turtle

data_file_path = os.path.join(os.path.dirname(__file__),'50_states.csv')

class Name(turtle.Turtle):
    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(name, align='center', font=(("Arial", 8, "normal")))

class States:
    def __init__(self):
        self.states_data = pandas.read_csv(data_file_path)

    def find_state_by_name(self, name):
        if name in self.states_data.state.to_list():
            state = self.states_data.state[self.states_data['state'] == name]
            x = int(state.x.values[0])
            y = int(state.y.values[0])
            new_state = Name(x=x, y=y, name=name)
            return 
        else:
            return False

# states = States()
# state = states.states_data[states.states_data['state'] == 'Louisiana']
# print(states.states_data.state.to_list())
# print(type(int(state.x.values[0])))
# print(states.find_state_by_name('Louisiana'))
