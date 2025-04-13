# 1. Агрегация
# Создай класс Team и класс Player. Команда может состоять из игроков, но игроки
# могут существовать и без команды.
# Добавь игрока в команду и выведи всех игроков в команде.
# Ожидаемый вывод:
# Players in team:
# Alice
# Bob
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_player(self):
        print(f'Players in team: "{self.name}"')
        for player_name in self.players:
            print(player_name.name)

class Player:
    def __init__(self, name):
        self.name = name

    def show_player(self):
        print(self.name)

team = Team("1")
player1 = Player("Эмир")
player2 = Player("Умар")

team.add_player(player1)
team.add_player(player2)
team.show_player()

player1.show_player()


# 2.Агрегация с несколькими связями
# Создай классы Company и Employee. Один сотрудник может работать в нескольких
# компаниях. Добавь одного сотрудника в две компании и выведи список
# сотрудников в каждой компании.
# Ожидаемый вывод:
# Employees in Company A:
# John
# Employees in Company B:
# John
class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employee(self):
        print(f'Employees in {self.name}')
        for employee_name in self.employees:
            print(employee_name.name)

class Employee:
    def __init__(self, name):
        self.name = name

company_a = Company('Company A:')
company_b = Company('Company B:')

employee1 = Employee('Эмир')
company_a.add_employee(employee1)
company_b.add_employee(employee1)
company_a.show_employee()
company_b.show_employee()


# 3. Композиция
# Создай класс House и класс Room. Комнаты создаются внутри дома и не могут
# существовать без него.
# Создай дом с двумя комнатами и выведи количество комнат в доме.
# Ожидаемый вывод:
# Number of rooms: 2
class House:
    def __init__(self):
        self.rooms = Room([1, 1])

    def show_rooms(self):
        print(f'Number of rooms: {self.rooms.add_rooms()}')

class Room:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def add_rooms(self):
        return len(self.numbers)

house = House()
house.show_rooms()


# 4. Композиция с вложенными объектами
# Создай класс Book и класс Page. Страницы создаются при создании книги и не
# используются отдельно. Выведи количество страниц в книге.
# Ожидаемый вывод:
# Pages in book: 3
class Book:
    def __init__(self, page):
        self.pages = [Page(i) for i in range(1, page + 1)]

    def show_pages(self):
        print(f'Pages in book: {len(book.pages)}')

class Page:
    def __init__(self, number):
        self.number = number

book = Book(3)
book.show_pages()


# 5. Композиция в цепочке
# Создай класс Computer, который при инициализации создаёт объекты классов CPU
# и RAM. Выведи информацию о составе компьютера.
# Ожидаемый вывод:
# Computer has:
# CPU: Intel i7
# RAM: 16GB
class Computer:
    def __init__(self, info_cpu, info_ram):
        self.info_cpu = CPU(info_cpu)
        self.info_ram = RAM(info_ram)

    def show_info(self):
        print('Computer has:')
        print(f'CPU: {self.info_cpu.model}')
        print(f'RAM: {self.info_ram.size}')

class CPU:
    def __init__(self, model):
        self.model = model

class RAM:
    def __init__(self, size):
        self.size = size

computer = Computer('Intel i7', '16GB')
computer.show_info()


# 6. Агрегация и удаление объектов
# Создай класс Playlist и класс Song. Песни добавляются в плейлист, но при
# удалении плейлиста сами песни не исчезают. Проверь, что песня существует
# после удаления плейлиста.
# Ожидаемый вывод:
# Song still exists: True
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

class Song:
    def __init__(self, song_titles):
        self.song_titles = song_titles

playlist = Playlist()
song = Song('Песня')
playlist.add_song(song)
del playlist

print(True if song else False)


# 7. Композиция и удаление объектов
# Создай класс Document и класс Paragraph. При удалении документа все
# параграфы должны быть уничтожены. Проверь, что параграфов больше не
# существует.
# Ожидаемый вывод:
# Paragraphs after document deletion: 0
class Document:
    def __init__(self, paragrafs):
        self.paragrafs = [Paragraph(i) for i in range(1, paragrafs + 1)]

    def get_paragraph(self):
        for paragraf in self.paragrafs:
            print(f'Paragraph: {paragraf.number}')

class Paragraph:
    def __init__(self, number):
        self.number = number

document = Document(3)
document.get_paragraph()
del document

try:
    document.get_paragraph()
except:
    print('Paragraphs after document deletion: 0')
