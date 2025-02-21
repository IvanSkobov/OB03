class Animal():
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав")

class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу")

class Cow(Animal):
    def make_sound(self):
        print("Мууууу")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()


