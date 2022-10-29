class Player:
    player_names = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
    
    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name not valid!")
        elif value in self.player_names:
            raise Exception(f"Name {value} is already used!")

        self._name = value
        self.player_names.append(value)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self._age = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")
        self._stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

