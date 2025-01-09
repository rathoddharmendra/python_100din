class Animal:
    def __init__(self):
        self.eyes = 2
        
    def breathe(self):
        print('Inhale, exhale')
    def smile(self):
        print('Smiling cheekily')

class Fish(Animal):
    def __init__(self):
        # new_learnen - extends attributes of Animal class, methods happen without this statement
        super().__init__() 
        self.fins = 2
    
    def swim(self):
        print('Swimming away...🐟')
    
    def breathe(self):
        super().breathe()
        print('breating under water')

nemo = Fish()
nemo.breathe()
# print(nemo.eyes)
nemo.smile()