# 1) Создай класс BankAccount с приватным __balance. Добавь методы:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        return 'Сумма пополнения должна быть положительной!'

    def withdraw(self, amount):
        if self.__balance >= amount and amount > 0:
            self.__balance -= amount
            return self.__balance
        return 'В балансе не хватает для снятия!'

    def get_balance(self):
        return self.__balance

obj = BankAccount(100)
print(obj.deposit(50))
print(obj.withdraw(150))
print(obj.get_balance())

obj2 = BankAccount(50)
print(obj2.deposit(-10))
print(obj2.withdraw(-10))
print(obj2.get_balance())


# 2) Создай класс User в котором (задание по теме getters/setters):
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def get_password(self):
        hidden_password = []
        for _ in self.__password:
            hidden_password.append('*')
        return ''.join(hidden_password)

    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            return 'Пароль успешно изменён'
        return 'Пароль должен быть больше 6 букв и цифр'

obj = User('Emir', 'adasd123')

print(obj.get_password())
print(obj.set_password('12345623423'))
print(obj.get_password())


# 3) Создайте класс Employee у которого есть:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 30_000:
            self.__salary = salary

obj = Employee('Emir', 35_000)
print(obj.salary)
obj.salary = 30_000
print(obj.salary)


# 4) Создайте класс Circle у которого есть:
from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius

    @property
    def area(self):
        return pi * self.__radius ** 2

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 0:
            self.__height = height


obj = Cylinder(7, 3)
print(obj.radius)
print(obj.area)
obj.radius = 5
print(obj.radius)
print(obj.area)

print(obj.height)
obj.height = 10
print(obj.height)
