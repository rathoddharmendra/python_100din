def add(*args, **kwargs):
    print(args)
    print(kwargs)
    sum = 0
    for num in args:
        sum += num
    for key in kwargs:
        sum += kwargs[key]
    return sum

# print(add(1, 2, 3, 4, 5))

dict_object = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}

print(add(**dict_object))

def calculate(**kwargs):
    print(kwargs)

# calculate(add=5, multiply=4, divide=3,subract=1)

# similar implementation to TKinter
class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs.get('make')
        self.make = kwargs.get('make') if kwargs.get('make') else "Hero"
        # self.model = kwargs['model'] = "SX-124"
        self.model = kwargs.get('model') if kwargs.get('model') else "SX-124"
        self.year = kwargs.get('year') 
        # self.year = kwargs['year'] = "2024"

car = Car()
print(car.make)

car_1 = Car(make="Nissan", year="2025", model="GTR-S4")
print(car_1.model)