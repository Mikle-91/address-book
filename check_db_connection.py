import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group
#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#отладочный файл

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l =db.get_contacts_not_in_group(Group(id="332")) # все группы из БД
    for item in l:
        print(item)
    print(len(l)) #количество групп в БД
finally:
    pass #db.destroy()
