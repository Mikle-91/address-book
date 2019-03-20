from fixture.orm import ORMFixture
from model.group import Group
from random import randrange
#тест проверяет создание принадлежности контакта группе

def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:           # проверка наличия групп
        app.group.create(Group(name="test"))
    contacts_list = db.get_contact_list() #загрузили список доступных контактов
    index = randrange(len(contacts_list))#выбрали рандомный контакт
    id=contacts_list[index].id #id рандомного контакта
    app.contact.add_contact_to_group_by_id(id) # добавили контакт в дефолтную группу в списке

    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    # input id группы, output: contacts В группе

    l = db.get_contacts_in_group(Group(id="386"))  # все контакты из группы-id

    if contacts_list[index] in l: #проверяем относится ли контакт с выбранным индексом к группе
        print("элемент добавлен")

    print("Добавлен контакт с индексом : " + str(index))
    print("Добавлен контакт с id : " + str(id))



