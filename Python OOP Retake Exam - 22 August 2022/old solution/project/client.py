import re


class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        mach = re.findall('(^0[0-9]*)', value)
        if not mach or len(mach[0]) > 10 or len(mach[0]) < 10:
            raise ValueError("Invalid phone number!")

        self._phone_number = value



