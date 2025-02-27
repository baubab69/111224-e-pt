# Задача: Создание класса-декоратора для времени выполнения функции
# Описание:
#
# Создайте класс-декоратор TimeLogger, который будет логировать время выполнения оборачиваемой функции.
# Класс должен использовать метод __call__ для измерения времени выполнения функции и вывода этой информации на экран.
#
# Требования:
#
# Класс TimeLogger должен принимать функцию в своем конструкторе.
# Метод __call__ должен измерять время выполнения функции и выводить эту информацию на экран.
# Напишите тестовый код, который демонстрирует использование этого декоратора.

# your src here

import datetime 


class TimeLogger:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        print(start)
        result = self.func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f'Время выполнения функции: {end - start}')
        return result

def main():
    @TimeLogger
    def test_func(*args):
        return sum(args)
    print(test_func(*range(100000)))
    # your src here
    pass


if __name__ == '__main__':
    main()
    