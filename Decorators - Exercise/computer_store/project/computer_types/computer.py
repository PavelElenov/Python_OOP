import abc


class Computer:
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @staticmethod
    def is_empty(value):
        if len(value.strip()) == 0:
            return True
        return False

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if self.is_empty(value):
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if self.is_empty(value):
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abc.abstractmethod
    def configure_computer(self, processor, ram):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
