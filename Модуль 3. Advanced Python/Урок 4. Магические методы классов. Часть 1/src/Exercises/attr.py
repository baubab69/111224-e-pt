# Создание класса с логированием доступа к атрибутам
# Описание:
#
# Создайте класс LoggedAttributes, который будет вести лог всех операций по установке, получению и
# удалению атрибутов, а также предоставлять значения по умолчанию для отсутствующих атрибутов.
# Все операции должны логироваться в список log.
#
# Требования:
# Переопределите метод __setattr__ для логирования установки атрибутов.
# Переопределите метод __getattribute__ для логирования доступа к атрибутам.
# Переопределите метод __getattr__ для логирования и предоставления значения по умолчанию для отсутствующих атрибутов.
# Переопределите метод __delattr__ для логирования удаления атрибутов.
# Шаги:
# Создайте класс LoggedAttributes.
# Добавьте список log в качестве атрибута класса для хранения логов операций.
# Реализуйте методы __setattr__, __getattribute__, __getattr__ и __delattr__ с логированием операций.
# Тестируйте класс, создавая экземпляр и выполняя различные операции с атрибутами.


class LoggedAttributes:

    def __init__(self):
        super().__setattr__('log', [])
    
    def __setattr__(self, key, value):
        self.log.append(f'Setting attribute {key} to {value}')
        super().__setattr__(key, value)
    
    def __getattribute__(self, name):
        log = super().__getattribute__('log')
        if name != 'log':
            log.append(f'Getting attribute {name}')
        return super().__getattribute__(name)
    
    def __getattr__(self,name):
        self.log.append(f'Attribute {name} not found, returning default value')
        return 'Default Value'
    
    def __delattr__(self, name):
        self.log.append(f'Deleting attribute {name}')
        super().__delattr__(name)

def main():
    test = LoggedAttributes()
    test.value = 10
    print(test.value)
    del test.value
    print(test.value)
    print(test.log)
if __name__ == '__main__':
    main()
    