# Создайте абстрактный класс Device, который определяет абстрактные методы turn_on() и turn_off().
# Затем создайте несколько подклассов, таких как Laptop, Smartphone и Tablet, которые реализуют эти методы
# для включения и выключения устройств.
#
# Используйте полиморфизм, чтобы создать функцию, которая принимает список устройств и выполняет действия
# включения и выключения для каждого устройства.

from abc import ABC, abstractmethod
from typing import List

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class Laptop(Device):
    def turn_on(self):
        print('Laptop is turning on')

    def turn_off(self):
        print('Laptop is turning off')
    
class Smartphone(Device):
    def turn_on(self):
        print('Smartphone is turning on')

    def turn_off(self):
        print('Smartphone is turning off')
    
class Tablet(Device):
    def turn_on(self):
        print('Tablet is turning on')   

    def turn_off(self):
        print('Tablet is turning off')

def turn_on_off(devices: List[Device]):
    for device in devices:
        device.turn_on()
        device.turn_off()

devices = [Laptop(), Smartphone(), Tablet()]
turn_on_off(devices)
