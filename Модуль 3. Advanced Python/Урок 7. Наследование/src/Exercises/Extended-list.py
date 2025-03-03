# Создайте класс ExtendedList, который наследует от встроенного типа list и добавляет несколько новых методов.
# Используйте private и protected атрибуты для хранения состояния и добавьте методы для работы с этими атрибутами.
# Также проверьте, является ли ExtendedList подклассом list с помощью функции issubclass() и используйте super()
# для вызова методов суперкласса.
#
# Шаги:
# Создайте класс ExtendedList, который наследует от list.
# Добавьте private атрибут для хранения количества удалений элементов.
# Добавьте protected атрибут для хранения максимального размера списка.
# Добавьте метод append, который проверяет максимальный размер перед добавлением элемента.
# Добавьте метод remove, который увеличивает счетчик удалений при удалении элемента.
# Напишите методы для получения значений private и protected атрибутов.
# Проверьте, является ли ExtendedList подклассом list с помощью функции issubclass().

class ExtendedList(list,):
    def init(self, max_size):
        self._max_size = max_size
        self.deleted = 0
        super().init()

    def append(self, value):
        if len(self) < self._max_size:
            super().append(value)
        else:
            print("Лист заполнен")

    def remove(self, value):
        super().remove(value)
        self.deleted += 1

    def get_deleted(self):
        return self.__deleted

    def get_max_size(self):
        return self._max_size

def check():
    return issubclass(ExtendedList, list)


check_list = ExtendedList(max_size=3)
check_list.append(1)
check_list.append(2)
check_list.append(3)
check_list.append(4)
print(issubclass(ExtendedList, dict))

print(check_list)

print(check_list.get_deleted())
print(check_list.get_max_size())
