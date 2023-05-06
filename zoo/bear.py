from animal import animal
class bear(animal):
    def __init__(self, name, age, color, health_level = 5, happiness_level = 5):
        super().__init__(name, age, health_level, happiness_level)
        self.color = color

    def display_info(self):
        print(super().display_info()+ f", Color: {self.color}")
