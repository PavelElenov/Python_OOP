from vehicle import Vehicle
from point import Point
from circle import Circle
from glass import Glass
from smartphone import Smartphone

'''Vehicle'''
# car = Vehicle(20)
# print(car.max_speed)
# print(car.mileage)
# print(car.gadgets)
# car.gadgets.append('Hudly Wireless')
# print(car.gadgets)


"""Point"""
# p = Point(2, 4)
# print(p)
# p.set_x(3)
# p.set_y(5)
# print(p)


"""Cicle"""
# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())


"""Glass"""
# glass = Glass()
# print(glass.fill(251))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())


"""Smartphone"""
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
