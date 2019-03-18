# # -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_group_name(app,data_groups, db):
    if app.group.count() == 0:       # проверка наличия групп перед изменением
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()  # проверка изменения группы - берется состояние до внесения изменений из UI
    #old_groups = db.get_group_list()  # проверка изменения группы - берется состояние до внесения изменений из бд
    index = randrange(len(old_groups))  # рандомно выбираем какую группу изменить
    group = data_groups     # новые значения из файла data_groups или json по желанию
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()     #проверка изменения группы - берется состояние после внесения изменений
    #new_groups = db.get_group_list()
    assert len(old_groups)  == len(new_groups) #сравнение количества групп после изменения группы
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп



#предыдущая версия теста с проверкой списков групп загружающихся из UI, а изменялось только значение name
# def test_modify_group_name(app):
#     if app.group.count() == 0:       # проверка наличия групп перед изменением
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()  # проверка изменения группы - берется состояние до внесения изменений
#     index = randrange(len(old_groups))  # рандомно выбираем какую группу изменить
#     group = Group(name="New group")     # новое значение для name
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     new_groups = app.group.get_group_list()     #проверка изменения группы - берется состояние после внесения изменений
#     assert len(old_groups)  == len(new_groups) #сравнение количества групп после изменения группы
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп
#

