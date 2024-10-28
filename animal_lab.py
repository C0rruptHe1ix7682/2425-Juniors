class Animal:
    def __init__(self, name, habitat, sound):
        self._name = name
        self._habitat = habitat
        self._sound = sound

    def get_name(self):
        return self._name
    
    def get_habitat(self):
        return self._habitat
    
    def speak(self):
        return f"{self._name} makes a sound: {self._sound}"
    
class Dog(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, habitat, "Woof!")

def speak(self):
    return f"{self.get_name()} says: {self._sound} loudly in {self.get_habitat()}"

def fetch(self):
    return f"{self.get_name()} is fetching the ball!"

class Cat(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, habitat, "Meow")

    def speak(self):
        return f"{self.get_name()} softly says: {self._sound} in {self.get_habitat()}"
    
    def climb(self):
        return f"{self.get_name()} is climbing a tree!"
    
def main():
    buddy = Dog("Buddy", "the backyard")
    whiskers = Cat("Whiskers", "the living room")

    print(buddy.speak())
    print(buddy.fetch())

    print(whiskers.speak())
    print(whiskers.climb())

if __name__ == "__main__":
    main()