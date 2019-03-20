import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group
#отладочный файл
#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


#input id группы, output: contacts ВНЕ ГРУППЫ
# try:
#     l =db.get_contacts_not_in_group(Group(id="386")) # все группы из БД
#     for item in l:
#         print(item)
#     print(len(l)) #количество групп в БД
# finally:
#     pass #db.destroy()


#input id группы, output: contacts В группе
# try:
#     #l =db.get_contacts_in_group(Group(id="386")) # все группы из БД
#     l = db.get_group_list()  # все группы из БД
#
#
#     for item in l:
#         print(item)
#     print(len(l)) #количество групп в БД
# finally:
#     pass #db.destroy()
#     orm_group=None
#     l=None

#нужно получить id группы test
l5= db.get_groupid_from_group_by_name("test")

print(l5)


# idl=l.id
# print(idl)

