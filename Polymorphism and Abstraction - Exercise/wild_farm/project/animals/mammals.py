from project.animals.animal import Mammal


class Mouse(Mammal):

    @property
    def type_food_can_eat(self):
        return ['Vegetable', 'Fruit']

    @property
    def weight_increase(self):
        return 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def type_food_can_eat(self):
        return ['Meat']

    @property
    def weight_increase(self):
        return 0.40

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    @property
    def type_food_can_eat(self):
        return ['Vegetable', 'Meat']

    @property
    def weight_increase(self):
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    @property
    def type_food_can_eat(self):
        return ['Meat']

    @property
    def weight_increase(self):
        return 1.00

    def make_sound(self):
        return 'ROAR!!!'
