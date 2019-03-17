# # -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_group(app, db, json_contacts): #альтернативный вариант data_contacts (вместо json_contact)
    contact = json_contacts
    app.contact.create(contact)





# def test_add_group(app, db, json_groups):
#     group = json_groups # читаем тестовые данные которые динамически подставил pytest_generate_tests из conftest.py
#     old_groups=db.get_group_list()   #проверка добавления группы - берется состояние до внесения изменений. Список загружается из db
#     app.group.create(group)
#     new_groups = db.get_group_list()  # проверка добавления группы - берется состояние после внесения изменений
#         #проверка содержания групп
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # проверка содержания групп
#




########
# #Ниже предыдущая версия теста, которая брала тестовые данные из текущего файла.
#
# def test_add_contact_empty(app):
#     app.contact.create(Contact(firstname="noInfo Man"))
#
# def test_add_contact(app):
#      app.contact.create(Contact(firstname="Ivan", middlename="pupkin", lastname="last", nickname="supernick", photo=None,
#                  title="sometitle", company="space", address="zeleka", homephone="5floar", mobilephone="9876", workphone="456",
#                  fax="45", email="65@qwe.ru", email2="4", email3="45", bday="", bmonth="February", byear="1992",
#                  aday="30", amonth="January", ayear="1980", new_group=None, address2="someadr", secondaryphone="49577884",
#                  notes="nothing"))

