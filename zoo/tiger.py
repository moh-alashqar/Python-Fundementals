from animal import animal
class tiger(animal):
    def __init__(self, name, age, hight, health_level = 12, happiness_level = 12):
        super().__init__(name, age, health_level, happiness_level)
        self.hight = hight

    def display_info(self):
        print(super().display_info()+ f", Hight: {self.hight}")