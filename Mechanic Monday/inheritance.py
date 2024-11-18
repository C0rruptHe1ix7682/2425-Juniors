class Bender:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def bend(self):
        return f"{self.name} is bending {self.element}."

class Firebender(Bender):
    def __init__(self, name):
        super().__init__(name, "Fire")

class Earthbender(Bender):
    def __init__(self, name):
        super().__init__(name, "Earth")

Zuko = Firebender("Zuko")
Toph = Earthbender("Toph")

print(Zuko.bend())
print(Toph.bend())