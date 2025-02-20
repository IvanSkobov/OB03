class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Какой-то общий звук животного"

    def eat(self):
        return f"{self.name} ест."

    def to_string(self):
        return f"{self.__class__.__name__},{self.name},{self.age}"

class Bird(Animal):
    def make_sound(self):
        return "Чирик-чирик"

class Mammal(Animal):
    def make_sound(self):
        return "Рык или ворчание"

class Reptile(Animal):
    def make_sound(self):
        return "Ш-ш-ш"


def animal_sounds(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Смотритель кормит {animal.name}.")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}.")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено {animal.name} в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавлен {staff_member.__class__.__name__} в зоопарк.")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for animal in self.animals:
                file.write(animal.to_string() + "\n")
            for staff in self.staff:
                file.write(staff.__class__.__name__ + "\n")
        print("Данные зоопарка сохранены.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                self.animals = []
                self.staff = []
                for line in lines:
                    data = line.strip().split(',')
                    if len(data) == 3:
                        animal_type, name, age = data
                        self.animals.append(globals()[animal_type](name, int(age)))
                    else:
                        self.staff.append(globals()[data[0]]())
            print("Данные зоопарка загружены.")
        except (FileNotFoundError, KeyError):
            print("Не удалось загрузить данные зоопарка.")


# Пример использования
zoo = Zoo()
zoo.add_animal(Bird("Попугай", 2))
zoo.add_animal(Mammal("Тигр", 5))
zoo.add_animal(Reptile("Змея", 3))
zoo.add_staff(ZooKeeper())
zoo.add_staff(Veterinarian())

animal_sounds(zoo.animals)

zoo.save_to_file("zoo_data.txt")

new_zoo = Zoo()
new_zoo.load_from_file("zoo_data.txt")
animal_sounds(new_zoo.animals)
