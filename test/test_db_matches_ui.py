from model.group import Group
from timeit import timeit

def test_group_list(app, db):
    ui_list = app.group.get_group_list()   #список загруженный через ui
    def clean(group): #clean убирает пробелы перед сравнением групп
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())   #список загруженный из db
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max) #сравнение списков

