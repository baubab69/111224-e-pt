## 1. Метод `__bool__`
# **Задание:**
# Создайте класс `BankAccount`, который:
# - Имеет атрибут `balance` (остаток на счете).
# - Реализует метод `__bool__`, который возвращает `True`, если баланс положительный, и `False`, если баланс 
#нулевой или отрицательный.
#срвнить 

# **Пример работы:**
# ```python

# print(bool(acc1))  # True
# print(bool(acc2))  # False



class BankAccount:

	def __init__(self, balance):
	 	self.__balance = balance 

	def __bool__(self):
		return self.__balance >= 0

	def __eq__(self, other):
		return self.__balance == other.__balance

	def __lt__(self, other):
		return self.__balance < other.__balance

	def __le__(self, other):
		return self.__balance <= other.__balance


acc1 = BankAccount(100)
acc2 = BankAccount(100)
print(bool(acc1))
print(acc1 == acc2)