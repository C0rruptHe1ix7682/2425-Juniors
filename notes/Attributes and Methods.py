class Dogs:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    
    def describe(self):
        return f"This dog is a {self.breed} and is {self.age} years old!"
    
dog1 = Dogs("Maltipoo", 4)

print(dog1.breed)
print(dog1.describe())