from fixture.orm import ORMFixture
from model.group import Group
from random import randrange
from fixture.contact import Contact


def test_del_contact_from_group(app, db):
    #app.group.create(Group(name="test"))
    contacts_list = db.get_contact_list() #загрузили список доступных контактов
    index = randrange(len(contacts_list))#выбрали рандомный контакт
    id = contacts_list[index].id  # id рандомного контакта
    group_name="test"

    app.contact.add_contact_to_group_by_name(group_name, id)  # добавили рандомный контакт c id в тестовую группу group_name
    link = "http://localhost/addressbook/?group=" + str(group_name)
    app.contact.open_page(link) #открыли страницу группы с списком принадлежащих контактов
    app.contact.delete_contactid_from_group(id) #удаляем контакт с id из группы(стираем отношение одного объетка к другому)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="") #
    group_id = db.get_groupid_from_group_by_name(group_name)

    l = db.get_contacts_not_in_group(Group(id=group_id))  #все контакты не состоящие в группе id

    if contacts_list[index] in l: #проверяем относится ли контакт с выбранным индексом к контактам не состящим в группе
        print("контакт успешно удален из группы")

