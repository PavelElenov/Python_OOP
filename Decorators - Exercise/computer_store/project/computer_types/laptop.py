from project.computer_types.computer import Computer


class Laptop(Computer):
    RAMS = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600}

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        available_processors = {
            'AMD Ryzen 9 5950X': 900,
            'Intel Core i9-11900H': 1050,
            'Apple M1 Pro': 1200
        }
        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        if ram not in self.RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += available_processors[processor] + self.RAMS[ram]

        return f"Created {self.manufacturer} {self.model} with " \
               f"{self.processor} and {self.ram}GB RAM for {self.price}$."
