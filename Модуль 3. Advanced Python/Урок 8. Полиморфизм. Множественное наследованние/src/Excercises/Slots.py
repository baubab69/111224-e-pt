# Создайте два класса: один с использованием __slots__, а другой без его использования.
# Напишите методы для добавления, удаления и изменения атрибутов в обоих классах. Сравните использование памяти
# и поведение __dict__ в каждом случае.
#
# Шаги:
# Создайте класс ClassWithDict, который не использует __slots__, и реализуйте методы для добавления,
# удаления и изменения атрибутов.
# Создайте класс ClassWithSlots, который использует __slots__, и реализуйте аналогичные методы.
# Напишите код для создания экземпляров каждого класса, добавления, удаления и изменения атрибутов.
# Сравните использование памяти каждым классом.
# Попробуйте получить доступ к __dict__ в обоих классах и объясните результаты.


class ClassWithDict:
    def __init__(self, mark, year):
        self.mark = mark
        self.year = year

    def add_attr(self, attr, value):
        self.__dict__[attr] = value
        print(f"Added attribute {attr} with value {value}")
        print(self.__dict__)
        print(self.__dict__.keys())
        print(self.__dict__.values())
    
    def del_attr(self, attr):
        if attr in self.__dict__:
            del self.__dict__[attr]
            print(f"Deleted attribute {attr}")
            print(self.__dict__)
        else:
            print(f"Attribute {attr} not found")

class ClassWithSlots:
    __slots__ = ('mark', 'year')

    def __init__(self, mark, year):
        self.mark = mark
        self.year = year

    def add_attr(self, attr, value):
        self.__dict__[attr] = value
        print(f"Added attribute {attr} with value {value}")
        print(self.__dict__)
        print(self.__dict__.keys())
        print(self.__dict__.values())

    def del_attr(self, attr):
        if attr in self.__dict__:
            del self.__dict__[attr]
            print(f"Deleted attribute {attr}")
            print(self.__dict__)
        else:
            print(f"Attribute {attr} not found")
        
obj1 = ClassWithDict('Audi', 2020)
obj2 = ClassWithSlots('Audi', 2020)

print(obj1.__sizeof__())
        
print(obj2.__sizeof__())
