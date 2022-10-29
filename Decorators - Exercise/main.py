from project.computer_store_app import ComputerStoreApp
from project.computer_types.laptop import Laptop

laptop = Laptop('ada', 'dfaad')
print(laptop.configure_computer('Apple M1 Pro', 16))
computer_store = ComputerStoreApp()
print(computer_store.build_computer('Laptop', 'Apple', 'Iphone 12', 'Apple M1 Pro', 8))
# print(computer_store.sell_computer(1500, 'Apple M1 Pr', 16))
print(computer_store.warehouse)