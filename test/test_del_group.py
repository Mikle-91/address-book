from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() ==0:           # проверка наличия групп перед удалением
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()  #проверка удаления группы - берется состояние до внесения изменений
    index =  randrange(len(old_groups))     #рандомно выбираем какую группу удалить
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()     #проверка удаления группы - берется состояние после внесения изменений
    assert len(old_groups) - 1 == len(new_groups)   #проверка количесва групп после удаления
    old_groups[index:index+1] = [] #удалили первый элемент из old_groups
    assert old_groups == new_groups     #проверка идентичности групп(за вычетом удаленной групы) после удаления



# def test_delete_first_group(app): # удаление первой группы в списке
#     if app.group.count() ==0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     index =  0
#     app.group.delete_first_group()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[index:index+1] = []
#     assert old_groups == new_groups
