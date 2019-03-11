# # -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups=app.group.get_group_list()   #проверка добавления группы - берется состояние до внесения изменений
    app.group.create(Group(name="uyt", header="headqwe", footer="footasd"))
    new_groups= app.group.get_group_list()  #проверка добавления группы - берется состояние после внесения изменений
    assert len(old_groups) +1 == len(new_groups) #проверка добавления группы - сравнение состояний после изменений

def test_add_empty_group(app):
    old_groups=app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups= app.group.get_group_list()
    assert len(old_groups) +1 == len(new_groups)
