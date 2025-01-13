# type: ignore

from car import Car
import random, time
from level import level_number

LANES_COORDINATES = [ _ for _ in range(-160, 170, 20)]
# [ -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160]

class Traffic():
    def __init__(self):
        self.cars: list(Car) = []
        self.level = 1

    def add_car(self):
        random_y_coordinate = random.choice(LANES_COORDINATES)
        self.cars.append(Car(y_position=random_y_coordinate, speed=self.level))  

    def increase_level(self):
        self.level += 1
    def create_traffic(self):
        self.add_car()
        self.garbage_collect()
        print(f'{len(self.cars)=}')

    def move_cars(self):
        for car in self.cars:
            car.move()

    def garbage_collect(self):
        for car in self.cars:
            if car.xcor() < -280:
                self.cars.remove(car)

    
