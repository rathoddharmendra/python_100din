# type: ignore
from turtle import Turtle

INITIAL_POSITION = (-375, 200)
BOUNCE_DEGREE = 45
MOVE_STEP = 2 # ideal 5-10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.7,0.7,0.1)
        self.resizemode("user")
        self.penup()
        self.speed('slowest')
        self.goto(INITIAL_POSITION)
        self.right(45)

    def move(self):
        # self.detect_paddle_collision() # sets direction
        # detect collision
        self.bounce_y()
        self.forward(MOVE_STEP)
        print(self.position())

    # def detect_paddle_collision(self) -> None | bool:
    #     x= self.xcor()
    #     if x < -390 or x > 390:
    #         self.bounce()
    #         print('loose')
    #         return True
    def bounce_y(self) -> bool:
        y = self.ycor()
        if y > 290 or y < -290:
            self.bounce()
            print('hit Y-wall')
            return True
    def bounce(self) -> None:
        self.left(90)
    

