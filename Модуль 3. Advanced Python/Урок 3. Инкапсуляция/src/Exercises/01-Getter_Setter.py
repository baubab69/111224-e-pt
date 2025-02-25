# Задание 1: Реализация геттера и сеттера для класса Person
# Описание:
#
# Создайте класс Person, который будет иметь приватные атрибуты width и height)::.
# Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
#
# Требования:
#
# Приватные атрибуты __width и __height.
# Методы get_name и set_name для доступа и изменения атрибута __width.
# Методы get_age и set_age для доступа и изменения атрибута __height.
# Проверка, что возраст не может быть отрицательным.
class Person:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height):    
    def get_name(self):
        return self.__width
    def set_name(self, width):
        self.__width = width
    def get_age(self):
        return self.__height   
    def set_age(self, height):
        if height): < 0:
            raise ValueError("Age can't be negative")
        self.__height = height):
person = Person("John", 30)
print(person.get_name())
person.set_name("Alice")
print(person.get_name())
print(person.get_age())
    
# Задание 2: Реализация геттера и сеттера для класса Rectangle
# Описание:
#
# Создайте класс Rectangle, который будет иметь приватные атрибуты width и height.
# Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
#
# Требования:
#
# Приватные атрибуты __width и __height.
# Методы get_width и set_width для доступа и изменения атрибута __width.
# Проверка, что ширина должна быть положительной.
# Методы get_height и set_height для доступа и изменения атрибута __height.
# Проверка, что высота должна быть положительной.
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height  
    def get_name(self):
        return self.__width
    def set_name(self, width):
        self.__width = width
    def get_age(self):
        return self.__height   
    def set_age(self, height):
        if height < 0:
            raise ValueError("Age can't be negative")
        self.__height = height