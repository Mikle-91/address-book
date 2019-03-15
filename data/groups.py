from sys import maxsize
from model.group import Group
import random
import string

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]











##ниже предыдущая версия файла

# def random_string(prefix, maxlen):  #prefix это слово перед сгенерированной кашей, maxlen это максимальная длина строки
#     syblols = string.ascii_letters + string.digits +" "*10 #сгенерили строку с алфавитом и набором цифр и 10 пробелами
#     return prefix + "".join([random.choice(syblols) for i in range(random.randrange(maxlen))]) #склеенный набор рандомных букв/цифр в строку
#



#перебор вариантов пустых и генерированных данных
# testdata = [
#     Group(name=name, header=header,footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]



# первая статичная, следом 5 сгенерированных строк
# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#     for i in range(2)
# ]