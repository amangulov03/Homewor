# # Таск 1. Универсальный принтер
# class Document:
#     def __init__(self, name):
#         self.name = name

#     def print_info(self):
#         return self.name

# class PDFDocument(Document):

#     def print_info(self):
#         return self.name

# class WordDocument(Document):

#      def print_info(self):
#         return self.name

# def print_document_info(doc):
#     print(doc.print_info())

# documents = [Document('Документ'), PDFDocument('PDF-Документ'), WordDocument('Word-Документ')]

# for document in documents:
#     print_document_info(document)


# # Таск 2. Животные говорят
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return 'Звуки животных!'

# class Dog(Animal):

#     def make_sound(self):
#         return f'{self.name} - гав-гав'

# class Cat(Animal):

#     def make_sound(self):
#         return f'{self.name} - мяу-мяу'

# class Cow(Animal):

#     def make_sound(self):
#         return f'{self.name} - муу-муу'

# def make_animals_talk(animals: list):
#     for animal in animals:
#         print(animal.make_sound())

# objects = [Dog('Собака'), Cat('Кошка'), Cow('Корова')]

# make_animals_talk(objects)


# # Таск 3. Игрушки
# class Toy:

#     def play_sound(self):
#         return 'Звуки игрушек'

# class Car(Toy):

#     def play_sound(self):
#         return '🚗 Бип-Бип!'

# class Doll(Toy):

#     def play_sound(self):
#         return '🪆  Привет я кукла!'

# class Drum(Toy):

#     def play_sound(self):
#         return '🥁 Бум-Бум!'

# toys = [Car(), Doll(), Drum()]

# print('Добро пожаловать в магазин игрушек!')
# print('Вот звуки игрушек!')

# for toy in toys:
#     print(toy.play_sound())

# # Таск 4. Фигуры и площадь
# from math import pi, sqrt

# class Shape:
#     def area(self):
#         ...

# class Circle(Shape):
#     def area(self):
#         return pi * 18 ** 2

# class Rectangle(Shape):
#     def area(self):
#         return 50 * 50

# class Triangle(Shape):
#     def area(self):
#         p = (4 + 5 + 6) / 2
#         return sqrt(p * (p - 4) * (p - 5) * (p - 6))

# obj2 = Circle()
# print(obj2.area())

# obj1 = Rectangle()
# print(obj1.area())

# obj3 = Triangle()
# print(obj3.area())


# Таск 5. Банкомат
class Card:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        ...

class CreditCard(Card):
    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

class DebitCard(Card):
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return self._balance
        return 'Недостаточно средств!'

obj1 = CreditCard(100)
print(obj1.withdraw(50))

obj2 = DebitCard(20)
print(obj2.withdraw(10))
