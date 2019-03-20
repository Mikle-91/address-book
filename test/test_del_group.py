from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:           # проверка наличия групп перед удалением
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()  #проверка удаления группы - берется состояние до внесения изменений
    group = random.choice(old_groups)   #рандомно выбираем какую группу удалить
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()     #проверка удаления группы - берется состояние после внесения изменений
    assert len(old_groups) - 1 == len(new_groups)   #проверка количесва групп после удаления
    old_groups.remove(group) #удаляем выбранный элемент из old_groups
    assert old_groups == new_groups     #проверка идентичности групп (за вычетом удаленной групы) после удаления полученные из БД
    if check_ui:
        def clean(group):  # clean убирает пробелы перед сравнением групп
            return Group(id=group.id, name=group.name.strip())
        db_new_groups= map(clean, db.get_group_list())
        assert sorted(db_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max) #сравниваем идентичность групп из БД и из UI









# предыдущая версия теста
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
