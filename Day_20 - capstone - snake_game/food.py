# type: ignore
import turtle, random

class Food:
    def __init__(self):
        self.food = (0,0)
        self.is_food_displayed = True
        self.food = turtle.Turtle("square")
        self.food.color('white')
        self.food.penup()

    def show_next_food(self):
        # screen.setup(width=600, height=600)
        food_position = (random.randint(-290, 290), random.randint(-290, 290))
        # while self.is_food_displayed:
        self.food.goto(food_position)
        self.food.showturtle()
            # if self.is_food_displayed == False:
            #     return
    def get_food_position(self):
        return self.food.pos()

    def hide_food(self):
        self.food.hideturtle()
        self.is_food_displayed = False


