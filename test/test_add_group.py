# # -*- coding: utf-8 -*-
from sys import maxsize
from model.group import Group
import pytest
import random
import string
from data.add_group import constant as testdata
# можно заменить рандомные данные в тесте на статичные путем замены
# from data.add_group import testdata   на
# from data.add_group import constant as testdata


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




#Ниже предыдущие версии теста:

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
