# 1) Напишите декоратор, который перед вызовом функции будет выводить сообщение "Выполнение функции..."
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("Выполнение функции...")
        return func(*args, **kwargs)
    return wrapper

@func_decorator
def my_func(x):
    return x ** 2
print(my_func(5))

# 2) Создайте декоратор, который будет умножать результат выполнения числовой функции на 2
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("До")
        res = func(*args, **kwargs)
        print(res)
        print("После")
        print(res * 2)
    return wrapper

@func_decorator
def my_func(x, y):
    return x + y
my_func(5, 3)

# 3) Создайте декоратор, который к строковому результату функции добавляет "!" в конце
def string_decorator(func):
    def wrapper(*args, **kwargs):
        res_func = func(*args, **kwargs)
        result = res_func + '!'
        return result
    return wrapper

@string_decorator
def my_func(x):
    return x
print(my_func("Hello World"))

# 4) Создайте декоратор, который ограничит выполнение функции 3 вызовами Если функция вызывается больше 3 раз, выводить сообщение "Функция больше недоступна"
def counter_decorator(func):
    def wrapper(*args, **kwargs):
        if wrapper.count < 3:
            wrapper.count += 1
            return func(*args, **kwargs)
        else:
            return "Функция больше недоступна"
    wrapper.count = 0
    return wrapper

@counter_decorator
def my_func(x):
    return x

for i in range(4):
    print(my_func("Hi"))

# 5) Создайте декоратор, который будет выводить переданные аргументы перед вызовом функции
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@func_decorator
def my_func(x):
    return x ** 2
print(my_func(5))
