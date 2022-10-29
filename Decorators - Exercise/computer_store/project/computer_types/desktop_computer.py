from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    RAMS = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600, 128: 700}

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        available_processors = {
            'AMD Ryzen 7 5700G': 500,
            'Intel Core i5-12600K': 600,
            'Apple M1 Max': 1800
        }
        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer"
                             f" {self.manufacturer} {self.model}!")

        if ram not in self.RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop "
                             f"computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += available_processors[processor] + self.RAMS[ram]

        return f"Created {self.manufacturer} {self.model} with {self.processor} " \
               f"and {self.ram}GB RAM for {self.price}$."
