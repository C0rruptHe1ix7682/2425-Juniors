class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def sound(self):
        return "This animal makes a sound."

class Dog(Animal):
    def sound(self):
        return "Woof woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"


dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

def make_animal_sound(animal):
    print(animal.sound())

make_animal_sound(dog)
make_animal_sound(cat)