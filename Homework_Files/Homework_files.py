
# 1) Создайте файл, внесите туда небольшой текст. В программе откройте этот файл и выведите содержимое на экран.
with open("test.txt", "w") as file:
    print(file.write("Python is a high—level programming language characterized by efficiency, simplicity, and versatility of use. It is widely used in the development of web applications and application software, as well as in machine learning and big data processing."))

with open("test.txt", "r") as file:
    print(file.read())


# 2)Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и
#     записывает в файл users.txt.
def register(login, password):
    with open("users.txt", "a+") as file:
        file.seek(0)
        users = file.readlines()

        for user in users:
            if login in user:
                print("Вы уже зарегистрированы!")
                return

        file.writelines([f"Логин: {login}\n", f"Пароль: {password}\n"])
        print("Регистрация успешна выполнена!")

login = input("Введите логин: ")
password = input("Введите пароль: ")
register(login, password)


# 3) Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет на экран
#     “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.
def letters(text):
    return "Да" if "w" in text else "Нет"

with open("test.txt", "r") as file:
    letter = file.read()

print(letters(letter))


# 4) Создайте текстовый файл python.txt и запишите в него следующий текст:
#     """
#     Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
#     you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
#     but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
#     """
#     Затем, считайте его. Найдите слова которые содержат букву  "o" и запишите в список o_words=[] и
#     выведите на экран все полученные слова.

def find_o(text):
    o_words = []
    for letter in text.split():
        if "o" in letter.lower():
            o_words.append(letter)
    return o_words

with open("python.txt", "w+") as file:
    file.write("Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions; you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2), but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.")
    file.seek(0)
    word = file.read()

print(find_o(word))


#  5) Возьмите следующий текст:
#     """
#     .detacilpmoc naht retteb si xelpmoC
#     .xelpmoc naht retteb si elpmiS
#     .ticilpmi naht retteb si ticilpxE
#     .ylgu naht retteb si lufituaeB
#     """
#     Запишите его в файл. Далее считайте этот текст с файла и выведите в обратном порядке.

def revers_words(text):
    revers_ = [i.strip()[::-1] for i in text]
    return "\n".join(revers_)

with open("test.txt", "r+") as file:
    file.write(".detacilpmoc naht retteb si xelpmoC\n.xelpmoc naht retteb si elpmiS\n.ticilpmi naht retteb si ticilpxE\n.ylgu naht retteb si lufituaeB")
    file.seek(0)
    words = file.readlines()
print(revers_words(words))


# 6) Создайте файл и запишите туда следующий текст:
#     """
#     123
#     aaa456
#     fxdya 5 0 0
#     """
#     В каждой строчке есть цифры, которые вместе дадут число.
#     Посчитайте сумму всех чисел.

def summa(number):
    s = 0
    for i in number:
        list1 = []
        for num in i:
            if num.isdigit():
                list1.append(num)
            else:
                list1.append(" ")
        num_str = "".join(list1)
        for j in num_str.split():
            s += int(j)
    return s

with open("number.txt", "w+") as file:
    file.write("""123
aaa456
fxdya 5 0 0
""")
    file.seek(0)
    text = file.readlines()

print(summa(text))
