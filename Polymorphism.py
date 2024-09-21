# Superclass
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Subclass 3
class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Function demonstrating polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Creating instances of the subclasses
dog = Dog()
cat = Cat()
cow = Cow()

# Passing different objects to the same function
animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
