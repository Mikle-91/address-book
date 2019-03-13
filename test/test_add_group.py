# # -*- coding: utf-8 -*-
from sys import maxsize
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):  #prefix это слово перед сгенерированной кашей, maxlen это максимальная длина строки
    syblols = string.ascii_letters + string.digits +" "*10 #сгенерили строку с алфавитом и набором цифр и 10 пробелами
    return prefix + "".join([random.choice(syblols) for i in range(random.randrange(maxlen))]) #склеенный набор рандомных букв/цифр в строку


# первая статичная, следом 5 сгенерированных строк
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

#перебор вариантов пустых и генерированных данных
# testdata = [
#     Group(name=name, header=header,footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups=app.group.get_group_list()   #проверка добавления группы - берется состояние до внесения изменений
    #group= Group(name="grIvan", header="title", footer="sometext") # group используется 2 раза, для теста и для его проверки
    app.group.create(group)
    assert len(old_groups) +1 == app.group.count() #проверка добавления группы - сравнение состояний после изменений
    new_groups = app.group.get_group_list()  # проверка добавления группы - берется состояние после внесения изменений
        #проверка содержания групп
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп






# def test_add_group(app):
#     old_groups=app.group.get_group_list()   #проверка добавления группы - берется состояние до внесения изменений
#     group= Group(name="grIvan", header="title", footer="sometext") # group используется 2 раза, для теста и для его проверки
#
#     app.group.create(group)
#     assert len(old_groups) +1 == app.group.count() #проверка добавления группы - сравнение состояний после изменений
#     new_groups = app.group.get_group_list()  # проверка добавления группы - берется состояние после внесения изменений
#         #проверка содержания групп
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп
#

# def test_add_empty_group(app):
#     old_groups=app.group.get_group_list()
#     group =Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups= app.group.get_group_list()
#     assert len(old_groups) +1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп
