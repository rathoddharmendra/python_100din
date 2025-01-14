# type: ignore

import pandas, os
from turtle import Turtle

data_file_path = os.path.join(os.path.dirname(__file__),'50_states.csv')

class Name(Turtle):
    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(name, align='center', font=(("Arial", 16, "normal")))

class States:
    def __init__(self):
        self.states_data = pandas.read_csv(data_file_path)
        self.states_list = [state.lower() for state in self.states_data.state.to_list()]
        self.guessed_states = []
        self.scoreboard = Scoreboard()
    def find_state_by_name(self, name: str):
        if name in self.states_list:
            print(self.states_data)
            state = self.states_data[self.states_data['state'] == name.title()]
            print(state)
            x = int(state.x.values[0])
            y = int(state.y.values[0])
            state_name = state.state.values[0]
            new_state = Name(x=x, y=y, name=state_name)
            self.scoreboard.update_scoreboard()
            self.guessed_states.append(state_name)  # add guessed state to list
            return True
        else:
            return False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-290, y=280)
        self.hideturtle()
        self.score = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}/50", align='center', font=(("Arial", 16, "normal")))
# states = States()
# state = states.states_data[states.states_data['state'] == 'Louisiana']
# print(states.states_data.state.to_list())
# print(type(int(state.x.values[0])))
# print(states.find_state_by_name('Louisiana'))
