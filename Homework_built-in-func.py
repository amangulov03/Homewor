# BUILT-INS:
#     1) Даны два списка:
#     names = ['Nikita', 'Katana', 'Toma']
#     ages = [25, 30, 35]
#     Создайте словарь, в котором ключи — это имена, а значения — соответствующие им возраста
names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
dict_ = zip(names, ages)
print(dict(dict_))


#     2) Дана строка:
#     text = "python"
#     при помощи определенной встроенной функции выведите индексы и символы, начиная с 1
text = "python"
for i, s in enumerate(text, 1):
    print(i, s)


#     3) Дан список строк с числами:
#     numbers = ["10", "20", "30", "40"]
#     Преобразуйте его в список целых чисел
numbers = ["10", "20", "30", "40"]
print(list(map(int, numbers)))


#     4) Дан список слов:
#     words = ["apple", "banana", "cherry", "dog", "elephant"]
#     Отфильтруйте и оставьте только те слова, которые начинаются с буквы d
words = ["apple", "banana", "cherry", "dog", "elephant"]
print(list(filter(lambda x: x.startswith('d'), words)))


#     5) Дан список чисел:
#     numbers = [1, -2, 3, -4, 5, -6]
#     Сначала удалите отрицательные числа при помощи filter, затем возведите оставшиеся числа в квадрат с помощью map
numbers = [1, -2, 3, -4, 5, -6]
print(list(map(lambda x: x ** 2, filter(lambda x: x > 0, numbers))))

# второй вариант
def square(x):
    return x ** 2
def remove_neg_num(x):
    return x > 0
numbers = [1, -2, 3, -4, 5, -6]
filtered = filter(remove_neg_num, numbers)
print(list(map(square, filtered)))


#     6) Даны два списка:
#     students = ["Alice", "Bob", "Charlie", "David"]
#     scores = [85, 92, 78, 90]
#     УСЛОВИЯ ЗАДАНИЯ:
#     	1.	Используйте zip, чтобы соединить студентов и их оценки
# 	    2.	С помощью filter оставьте только тех, у кого оценка больше 80
# 	    3.	Пронумеруйте оставшихся студентов, начиная с 1, используя enumerate
# 	    4.	Преобразуйте результат в список кортежей (номер, имя, оценка)
students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]
zipped = zip(students, scores)
filtered = filter(lambda x: x[1] > 80, zipped)
for num, student in enumerate(filtered, 1):
    print(num, student)
