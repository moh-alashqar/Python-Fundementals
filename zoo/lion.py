from animal import animal
class lion(animal):
    def __init__(self, name, age, weigth, health_level = 7, happiness_level = 7):
        super().__init__(name, age, health_level, happiness_level)
        self.weigth = weigth

    def display_info(self):
        print(super().display_info()+ f", Weight: {self.weigth}")