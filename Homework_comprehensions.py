# 1) Напишите list comprehension, который создаст список квадратов чисел от 1 до 10
print([i ** 2 for i in range(1, 11)])

# 2) Используя list comprehension, создайте список только из четных чисел от 1 до 20
print([i for i in range(1, 21) if i % 2 != 0])

# 3) Используя dict comprehension, создайте словарь, где ключ — число от 1 до 5, а значение — его квадрат.
print({i: i ** 2 for i in range(1, 6)})

# 4) вам дан список words = ["python", "java", "swift", "golang", "javascript"], используя list comprehension, создайте новый список из слов длиной больше 5 символов
words = ["python", "java", "swift", "golang", "javascript"]
print([i for i in words if len(i) > 5])

# 5) Вам дан список, words = ["apple", "banana", "cherry"], используя list comprehension, получите список этих слов в верхнем регистре
words = ["apple", "banana", "cherry"]
print([i.upper() for i in words])
