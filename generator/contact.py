# # -*- coding: utf-8 -*-
import pytest
import jsonpickle
import os.path
from model.contact import Contact
import random
import string
import getopt # для чтения командной строки
import sys # чтобы получить доступ к этим опциям
#файл генерирует тестовые данные в формате json для создания/редактирования контактов
#изменять длину генерируемых данных можно в "testdata =Contact(firstname=random_string("Fir.name", 5)
# где 5 это количество символов после слова Fir.name, а количество контактов можно указать в переменной n
# При вызове генератора через консоль, можно указать параметр-n и название файла с данными.
# Например: -n 10 -f data/test.json (10 контактов в файле test)


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"]) # n - задает кол-во генерируемых данных, f-файл куда будет помещаться
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5 #количество наборов данных(1 набор=1 контакт)
f= "data/contacts.json"

for o, a in opts: # o - название опции, a- значение опции
    if o=="-n":
        n=int(a) #если "-n" то задаем количество контакт
    elif o =="-f":
        f=a  #файл оставляем в виде строки



#генерим набор из букв, цифр, пробелов
def random_string(prefix, maxlen):  #prefix это слово перед сгенерированной кашей, maxlen это максимальная длина строки
    syblols = string.ascii_letters + string.digits +" "*10 #сгенерили строку с алфавитом и набором цифр и 10 пробелами
    return prefix + "".join([random.choice(syblols) for i in range(random.randrange(maxlen))]) #склеенный набор рандомных букв/цифр в строку

#генерим набор из цифр, пробелов, знаков -()+
def random_string_phone(prefix, maxlen):
    syblols = "-()+" + string.digits +" "*2
    return prefix + "".join([random.choice(syblols) for i in range(random.randrange(6, maxlen))])

#генерим месяц
def random_month():
    month_list = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    return random.choice(month_list)

#генерим email
def random_email(prefix, maxlen):
        syblols = string.ascii_lowercase + string.digits + "." + "-"
        return  ''.join([random.choice(syblols) for i in range(random.randrange(maxlen))]) +str(prefix)




#генерируемые данные:  первая статичная пустая, следом 5 сгенерированных строк
testdata = [Contact(firstname="", lastname="")] +  [
            Contact(firstname=random_string("Fir.name", 5),
                    middlename=random_string("midname", 10),
                    lastname=random_string("lname", 10),
                    nickname=random_string("nickname", 10),
                    photo=None,
                    title=random_string("title", 10),
                    company=random_string("company", 10),
                    address=random_string("address", 10),
                    homephone=random_string_phone("", 10),
                    mobilephone=random_string_phone("", 10),
                    workphone=random_string_phone("", 10),
                    fax=random_string_phone("", 10),
                    email=random_email("@gmail.com", 20),
                    email2=random_email("@gmail2.com", 20),
                    email3=random_email("@gmail3.com", 20),
                    bday=str(random.randint(1, 30)),
                    bmonth=random_month(),
                    byear=str(random.randint(1900, 2020)),
                    aday=str(random.randint(1, 30)),
                    amonth=random_month(),
                    ayear=str(random.randint(1900, 2020)),
                    new_group=None,
                    address2=random_string("address2", 10),
                    secondaryphone=random_string_phone("", 10),
                    notes=random_string("notes", 10),


            )
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) #задали путь к файлу куда будем записывать сгенерированные данные

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))   # dumps превращяет данные из словаря в строку json