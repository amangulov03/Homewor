# 1) напишите полный синтаксис конструкции try-except
try:
    raise ValueError
except Exception:
    print("Ошибка")
else:
    print('Норм')
finally:
    print("До свидания")

# 2)Напишите код, который пытается вывести значение переменной, не определенной ранее,
# и обрабатывает исключение, выводя сообщение "Такой переменной не существует!".
try:
    print(num)
except NameError:
    print("Такой переменной не существует!")

# 3) Напишите код, который принимает два числа от пользователя и выводит результат их деления.
# Обработайте исключение, которое выйдет при делении на ноль, выводя сообщение "На ноль делить нельзя"
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(num1 / num2)
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("Введите корректное число!")
else:
    print("Все верно")

# 4)Напишите код, который принимает две строки от пользователя, преобразует их в целые числа и выводит их сумму.
# Обработайте исключение которое выйдет в случае если пользователь передал не число а строку, выводя сообщение "Введите число!"
while True:
    try:
        num1 = input("Введите число: ")
        num2 = input("Введите число: ")
        print(f"Сумма: {int(num1) + int(num2)}")
    except ValueError:
        print("Вы не ввели число!")
        break
    else:
        print("Все верно")
        break

# 5)  Напишите код, который пытается получить значение по ключу из словаря. Обработайте исключение,
# которое выйдет если такого ключа нет, выводя сообщение "Нет такого ключа!".
try:
    dict1 = {'a': 1, 'b': 2}
    key = input("Введите ключ: ")
    print(dict1[key])
except KeyError:
    print("Нет такого ключа!")
else:
    print("Все верно")

# 6)напишите код, который пытается получить элемент списка по индексу. Обработайте исключение
# которое выйдет если такого индекса нет, выводя сообщение "Нет такого элемента!"
try:
    list1 = [1, 2, 3, 4]
    get_index = int(input("Введите индекс элемента: "))
    print(list1[get_index])
except IndexError:
    print("Нет такого элемента!")

# 7)Напишите код, который принимает возраст от пользователя и выбрасывает исключение
# ValueError с сообщением "Доступ запрещён", если возраст меньше 18. Обработайте это исключение,
# выводя сообщение "Введён некорректный возраст". Используйте блоки else и finally для вывода сообщений "Спасибо" и "До свидания!" соответственно.
try:
    user_input = input("Введите возраст: ")
    if not user_input.isdigit():
        raise ValueError("Вы ввели строку")
    user = int(user_input)
    if user < 18:
        raise ValueError("Доступ запрещён")
except ValueError as e:
    print(e)
else:
    print("Спасибо")
finally:
    print("До свидания!")

# 8) Напишите код, который принимает два числа от пользователя и выводит результат их деления.
# Обработайте исключения ValueError и ZeroDivisionError, выводя сообщение "Произошла ошибка!".
try:
    num1 = int(input("Введите число: "))
    num1 = int(input("Введите число: "))
    print(num1 / num1)
except (ZeroDivisionError, ValueError):
    print("Произошла ошибка!")

# 9) Напишите код, который принимает сумму денег от пользователя и выбрасывает исключение
# ValueError с сообщением "Сумма не может быть отрицательной!", если сумма меньше 0.
# Обработайте это исключение и выведите сообщение ошибки. Если исключение не возникло, выведите сумму.
try:
    user_input = input("Введите сумму денег: ")
    if user_input.isalpha():
        raise ValueError("Ошибка")
    user = int(user_input)
    if user < 0:
        raise ValueError("Сумма не может быть отрицательной!")
    print(f"Сумма денег: {user}")
except ValueError as e:
    print(e)

# 10) Напишите код, который пытается сложить строку и число. Обработайте исключение TypeError, выводя сообщение "Unsupported option"

try:
    user_input1 = input("Введите первое значение: ")
    user_input2 = input("Введите второе значение: ")

    num1 = int(user_input1)
    num2 = int(user_input2)

    print(f"Результат: {num1 + num2}")
except (ValueError, TypeError):
    print("Unsupported option")
