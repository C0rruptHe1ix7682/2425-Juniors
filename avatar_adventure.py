import pdb

class Character:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def introduce(self):
        return f"My name is {self.name}, and I am a {self.element} bender."
    
aang = Character("Aang", "Air")
katara = Character("Katara", "Water")
toph = Character("Toph", "Earth")

def journey_to_element(character):
    if character.element == "Air":
        return "Aang flies with his glider."
    elif character.element == "Water":
        return "Katara bends water to travel."
    elif character.element == "Earth":
        return "Toph creates earth walls to move forward."
    else:
        return "This character does not have an elemental power!"

pdb.set_trace()
print(aang.introduce())
print(journey_to_element(aang))
print(katara.introduce())
print(journey_to_element(katara))
print(toph.introduce())
print(journey_to_element(toph))