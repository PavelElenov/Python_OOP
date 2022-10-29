from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    def animal_type(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def type_food_can_eat(self):
        pass

    @property
    @abstractmethod
    def weight_increase(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in self.type_food_can_eat:
            return f"{self.animal_type} does not eat {food_type}!"
        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.animal_type} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.animal_type} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
