# # -*- coding: utf-8 -*-
import pytest
import jsonpickle
import os.path
from model.group import Group
import random
import string
import getopt # для чтения командной строки
import sys # чтобы получить доступ к этим опциям

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"]) # n - задает кол-во генерируемых данных, f-файл куда будет помещаться
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f= "data/groups.json"

for o, a in opts: # o - название опции, a- значение опции
    if o=="-n":
        n=int(a) #если "-n" то задаем количество групп
    elif o =="-f":
        f=a  #файл оставляем в виде строки

def random_string(prefix, maxlen):  #prefix это слово перед сгенерированной кашей, maxlen это максимальная длина строки
    syblols = string.ascii_letters + string.digits +" "*10 #сгенерили строку с алфавитом и набором цифр и 10 пробелами
    return prefix + "".join([random.choice(syblols) for i in range(random.randrange(maxlen))]) #склеенный набор рандомных букв/цифр в строку


# первая статичная, следом 5 сгенерированных строк
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))   # dumps превращяет данные из словаря в строку json