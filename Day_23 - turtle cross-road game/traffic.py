# type: ignore

from car import Car
import random, time
from level import level_number

LANES_COORDINATES = [ _ for _ in range(-160, 170, 20)]
# [ -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160]

class Traffic():
    def __init__(self):
        self.cars: list(Car) = []

    def add_car(self):
        random_y_coordinate = random.choice(LANES_COORDINATES)
        self.cars.append(Car(y_position=random_y_coordinate, speed=level_number)) 

    def create_traffic(self):
        self.add_car()
        print(f'{len(self.cars)=}')

    def move_cars(self):
        for car in self.cars:
            car.move()

    
