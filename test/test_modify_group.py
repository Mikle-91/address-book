# # -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_group_name(app):
    if app.group.count() == 0:       # проверка наличия групп перед изменением
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()  # проверка изменения группы - берется состояние до внесения изменений
    index = randrange(len(old_groups))  # рандомно выбираем какую группу изменить
    group = Group(name="New group")     # новое значение для name
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()     #проверка изменения группы - берется состояние после внесения изменений
    assert len(old_groups)  == len(new_groups) #сравнение количества групп после изменения группы
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп




#
# def test_modify_group_header(app):
#     if app.group.count() == 0:       # проверка наличия групп перед изменением
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()  # проверка изменения группы - берется состояние до внесения изменений
#     index = randrange(len(old_groups))  # рандомно выбираем какую группу изменить
#     group = Group(header="New header2") # новое значение для header
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     new_groups = app.group.get_group_list()     #проверка изменения группы - берется состояние после внесения изменений
#     assert len(old_groups)  == len(new_groups) #сравнение количества групп после изменения группы
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп
#

