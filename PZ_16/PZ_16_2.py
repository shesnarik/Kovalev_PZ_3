#Создайте класс "Фрукт", который содержит информацию о наименовании и весе
#фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса
#"Фрукт" и содержат информацию о цвете.
class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_info(self):
        return f"Фрукт {self.name} весит {self.weight} г."


class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

    def get_info(self):
        return f" {self.name} весит {self.weight} г. и имеет цвет {self.color}."


class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

    def get_info(self):
        return f" {self.name} весит {self.weight} г. и имеет цвет {self.color}."


apple = Apple("Яблоко", 200, "красное")
print(apple.get_info())

orange = Orange("Апельсин", 150, "оранжевое")
print(orange.get_info())
