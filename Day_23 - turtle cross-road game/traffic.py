from car import Car
import random, time
LANES_COORDINATES = [ _ for _ in range(-200, 210, 20)]
# [-200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

class Traffic():
    def __init__(self):
        self.lanes = []
        self.cars = list
        self.level = 1
        self.create_random_cars()

    def increase_level(self):
        self.level += 1


    def create_random_cars(self):
        while True:
            time.sleep(random.randint(0,4))  # wait for 0.5 seconds before adding a new car
            self.add_car()
            print(len(self.cars))

    def add_car(self):
        random_y_coordinate = random.choice(LANES_COORDINATES)
        self.cars.append(Car(y_position=random_y_coordinate, speed=self.level))
