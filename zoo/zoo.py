from animal import animal
from bear import bear
from lion import lion
from tiger import tiger

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal_type, name, age, color_weigth_height, *args):
        if animal_type == "lion":
            self.animals.append(lion(name, age, color_weigth_height, *args))
        elif animal_type == "tiger":
            self.animals.append(tiger(name, age, color_weigth_height, *args))
        elif animal_type == "bear":
            self.animals.append(bear(name, age, color_weigth_height, *args))
        else: 
            self.animals.append(animal(name, age, color_weigth_height, *args))
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

zoo1 = Zoo("John's Zoo")
zoo1.add_animal("lion", "Nala", 20, 100).add_animal("bear", "Shere Khan", 15, "Brown").add_animal("tiger", "Rajah", 7, 1).print_all_info()