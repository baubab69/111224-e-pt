# Создайте класс BankAccount, который будет представлять банковский счет. Класс должен включать следующие функции:
#
# Инкапсуляция: Приватные атрибуты для номера счета и баланса.
# Конструктор: Метод для инициализации объекта с номером счета и начальным балансом.
# Геттеры и сеттеры: Методы для доступа и изменения баланса.
# Магические методы: Методы для добавления и снятия денег (__add__ и __sub__),
# сравнения балансов (__eq__, __lt__, __le__, и т.д.), строкового представления (__str__ и __repr__),
# и вызова объекта (__call__).
class BankAccount:

    def __init__(self):
        self.__account_number = 0
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    # Сеттер для установки баланса
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    # Метод для добавления денег
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    # Метод для снятия денег
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    # Магические методы для арифметических операций
    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self

    # Магические методы для сравнения
    def __eq__(self, other):
        return self.__balance == other.__balance

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __le__(self, other):
        return self.__balance <= other.__balance

    # Магические методы для представления объекта
    def __str__(self):
        return f"BankAccount(account_number={self.__account_number}, balance={self.__balance})"

    def __repr__(self):
        return f"BankAccount(account_number={self.__account_number}, balance={self.__balance})"
    
