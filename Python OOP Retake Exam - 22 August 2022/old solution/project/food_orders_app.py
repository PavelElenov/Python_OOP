from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    RECEIPT_ID = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def find_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client
        return

    def register_client(self, client_phone_number):
        if self.find_client(client_phone_number):
            raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in ['Starter', 'MainDish', 'Dessert']:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        ll = [meal.details() for meal in self.menu]
        return '\n'.join(str(x) for x in ll)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        def have_meal():
            for item in self.menu:
                if item.name == meal:
                    if item.quantity < quantity:
                        raise Exception(f"Not enough quantity of {type(item).__name__}: {meal}!")
                    else:
                        return True
            raise Exception(f"{meal} is not on the menu!")

        def find_meal():
            for item in self.menu:
                if item.name == meal:
                    return Meal(meal, item.price, quantity)

        def decrease_meal_quantity():
            for item in self.menu:
                if item.name == meal.name:
                    item.quantity -= meal.quantity

        adding_meal = []

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not self.find_client(client_phone_number):
            self.register_client(client_phone_number)

        for meal, quantity in meal_names_and_quantities.items():
            if have_meal():
                meal = find_meal()
                adding_meal.append(meal)

        client = self.find_client(client_phone_number)
        for meal in adding_meal:
            client.shopping_cart.append(meal)
            client.bill += meal.price * meal.quantity
            decrease_meal_quantity()

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([meal.name for meal in client.shopping_cart])} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.find_client(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            for menu_meal in self.menu:
                if meal.name == menu_meal.name:
                    menu_meal.quantity += meal.quantity

        client.shopping_cart.clear()
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.find_client(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        receipt_id = self.RECEIPT_ID
        self.RECEIPT_ID += 1
        client.shopping_cart.clear()
        client.bill = 0

        return f"Receipt #{receipt_id} with total amount of {total_paid_money:.2f} was " \
               f"successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


