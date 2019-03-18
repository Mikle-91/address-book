# # -*- coding: utf-8 -*-
import pytest
import jsonpickle
import os.path
from model.group import Group
import random
import string
import getopt # для чтения командной строки
import sys # чтобы получить доступ к этим опциям
#изменять длину генерируемых данных можно в "testdata =[Group(name=random_string("name", 10)"..]
# где 10 это количество символов после слова name, а количество групп можно указать в переменной n
# При вызове генератора через консоль, можно указать параметр-n и название файла с данными.
# Например: -n 10 -f data/test.json (10 групп в файле test)


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"]) # n - задает кол-во генерируемых данных, f-файл куда будет помещаться
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5 #количество наборов данных(1 набор=1 группа)
f= "data/groups.json"

for o, a in opts: # o - название опции, a- значение опции
    if o=="-n":
        n=int(a) #если "-n" то задаем количество групп
    elif o =="-f":
        f=a  #файл оставляем в виде строки
#


def random_string(prefix, maxlen):  #prefix это слово перед сгенерированной кашей, maxlen это максимальная длина строки
    syblols = string.ascii_letters + string.digits +" "*10 #сгенерили строку с алфавитом и набором цифр и 10 пробелами
    return prefix + "".join([random.choice(syblols) for i in range(random.randrange(maxlen))]) #склеенный набор рандомных букв/цифр в строку


#генерируемые данные:  первая статичная, следом 5 сгенерированных строк
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) #задали путь к файлу куда будем записывать сгенерированные данные

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))   # dumps превращяет данные из словаря в строку json