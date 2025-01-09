inheritance

class Fish(Animal):
    def __init__(self):
        super().__init__()

# new_learnen - extends attributes of Animal class, methods happen without this statement
class Fish(Animal):
    def __init__(self):
        # new_learnen - extends attributes of Animal class, methods happen without this statement
        super().__init__() 
        self.fins = 2

after creating turtle in any form - food, snakes, or score -- it shows up on board

# if I override this super classes method, I have an option to still implement it:
 def breathe()
    super().breathe()
    # do something

# when I inherit from super class, I get methods by default and attributes if I call super().__init__() in constructor