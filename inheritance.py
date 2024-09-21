# Superclass
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        print(f"The {self.make} {self.model} is starting...")

# Subclass inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call the constructor of the superclass
        self.doors = doors
    
    def honk(self):
        print(f"The {self.make} {self.model} is honking!")

# Creating an instance of the Car subclass
my_car = Car("Toyota", "Corolla", 4)

# Accessing methods from both the superclass and subclass
my_car.start()  # Inherited from Vehicle
my_car.honk()   # Defined in Car
