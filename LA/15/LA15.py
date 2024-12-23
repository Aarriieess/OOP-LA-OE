class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Bark!")
        
class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Meow!")

class Bird():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Chirp!")

class Fish():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

doggy = Dog("Doggy")
catty = Cat("Catty")
birdy = Bird("Birdy")
fishy = Fish("Fishy")


def animal_sound(animal):
    animal.speak()

for animal in (doggy, catty, birdy, fishy):
    animal_sound(animal)

