class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def sound(self):
        return "This animal makes a sound."

class Dog(Animal):
    def sound(self): 
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

print(dog.sound())
print(cat.sound())