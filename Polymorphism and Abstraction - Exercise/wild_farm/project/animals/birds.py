from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    @property
    def type_food_can_eat(self):
        return ['Meat']

    @property
    def weight_increase(self):
        return 0.25


class Hen(Bird):
    @property
    def type_food_can_eat(self):
        return ["Vegetable", 'Meat', 'Fruit', 'Seed']

    @property
    def weight_increase(self):
        return 0.35

    def make_sound(self):
        return 'Cluck'
