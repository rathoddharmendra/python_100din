# type: ignore
import turtle, random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color('blue')
        self.penup()
        self.resizemode("user")
        self.shapesize(0.5, 0.5, outline=0.5)
        self.refresh()

    def refresh(self):
        food_position = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(food_position)
        print('nom nom nom')

    def get_food_position(self):
        return self.position

    def hide_food(self):
        self.hideturtle()
        self.is_food_displayed = False


