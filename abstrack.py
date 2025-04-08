# 1. Абстрактный транспорт
# Создай абстрактный класс Transport с абстрактным методом move(). Реализуй два
# класса Car и Plane, которые наследуются от Transport и реализуют метод move() по-
# своему.
# Пример вывода:
# Car is moving on the road
# Plane is flying in the sky

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        ...

class Car(Transport):
    def move(self):
        return 'Car is moving on the road'

class Plane(Transport):
    def move(self):
        return 'Plane is flying in the sky'

def print_info(transports):
    print(transports.move())

car = Car()
print_info(car)

plane = Plane()
print_info(plane)


# 2. Платёжная система
# Создай абстрактный класс PaymentMethod с методом pay(amount). Сделай классы
# CreditCard и PayPal, реализующие этот метод с выводом способа оплаты и суммы.
# Пример вывода:
# Оплата 1000 через Credit Card
# Оплата 500 через PayPal

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        ...

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f'Оплата {amount} через Credit Card'

class PayPal(PaymentMethod):
     def pay(self, amount):
        return f'Оплата {amount} через PayPal'

obj1 = CreditCard()
print(obj1.pay(1000))

obj2 = PayPal()
print(obj2.pay(500))


# 3. Фигуры и площадь
# Создай абстрактный класс Shape с методом area(). Реализуй классы Circle и Rectangle с
# соответствующим вычислением площади.
# Пример вывода:
# Площадь круга: 78.5
# Площадь прямоугольника: 200

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def area(self):
        return f'Площадь круга: {pi * 5 ** 2:.1f}'

class Rectangle(Shape):
    def area(self):
        return f'Площадь прямоугольника: {20 * 10}'

def print_info(shapes):
    print(shapes.area())

obj1 = Circle()
print_info(obj1)

obj2 = Rectangle()
print_info(obj2)

# 4. Устройства вывода
# Определи абстрактный класс OutputDevice с методом display(text). Создай Monitor и
# Printer, которые выводят текст по-разному (например, просто через print, но с
# разными префиксами).
# Пример вывода:
# [Monitor] Hello, world!
# [Printer] Hello, world!

from abc import ABC, abstractmethod

class OutputDevice(ABC):
    @abstractmethod
    def display(self, text):
        ...

class Monitor(OutputDevice):
    def display(self, text):
        print(f'[Monitor] {text}')

class Printer(OutputDevice):
    def display(self, text):
        print(f'[Printer] {text}')

obj1 = Monitor()
obj1.display('Hello, Monitor!')

obj2 = Printer()
obj2.display('Hello, Printer!')


# 5. Абстрактный животный класс
# Создай абстрактный класс Animal с методом make_sound(). Создай два класса Dog и
# Cat, которые реализуют этот метод (выводят «Гав!» и «Мяу!» соответственно).
# Пример вывода:
# Гав!
# Мяу!

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...

class Dog(Animal):
    def make_sound(self):
        return 'Гав!'

class Cat(Animal):
    def make_sound(self):
        return 'Мяу!'

def print_info(voice):
    print(voice.make_sound())

dog = Dog()
print_info(dog)

cat = Cat()
print_info(cat)


# 6. Абстрактный работник
# Определи класс Employee с методом calculate_salary(). Сделай Developer и Manager,
# возвращающие зарплату с разными расчётами (фикс + бонус, почасовая и т.п.).
# Пример вывода:
# Зарплата разработчика: 5000
# Зарплата менеджера: 7000

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        ...

class Developer(Employee):
    salary = 4000
    bonus = 1000

    def calculate_salary(self):
        return f'Зарплата разработчика: {self.salary + self.bonus}'

class Manager(Employee):
    hourly = 50
    hours = 140

    def calculate_salary(self):
        return f'Зарплата менеджера: {self.hourly * self.hours}'

def print_info(employee):
    print(employee.calculate_salary())

obj1 = Developer()
print_info(obj1)

obj2 = Manager()
print_info(obj2)


# 7. Интерфейс базы данных
# Создай абстрактный класс Database с методами connect() и disconnect(). Реализуй
# классы MySQLDatabase и PostgreSQLDatabase, которые выводят информацию о
# подключении/отключении.
# Пример вывода:
# Подключение к MySQL
# Отключение от MySQL
# Подключение к PostgreSQL
# Отключение от PostgreSQL

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def disconnect(self):
        ...

class MySQLDatabase(Database):
    def connect(self):
        return 'Подключение к MySQL'

    def disconnect(self):
        return 'Отключение от MySQL'

class PostgreSQLDatabase(Database):
    def connect(self):
        return 'Подключение к PostgreSQL'

    def disconnect(self):
        return 'Отключение от PostgreSQL'

def print_info(database):
    print(database.connect())
    print(database.disconnect())

mysql_db = MySQLDatabase()
print_info(mysql_db)

postgres_db = PostgreSQLDatabase()
print_info(postgres_db)
