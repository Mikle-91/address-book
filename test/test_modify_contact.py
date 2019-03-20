# # -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app, db): #изменяем данные рандомного контакта
    if app.contact.count() == 0:  # проверка наличия контакта перед изменением
        app.contact.create(     #если нет ни одного контакта, то создаем новый
            Contact(firstname="Ivan", middlename="pupkin", lastname="last", nickname="supernick", photo=None,
                    title="sometitle", company="space", address="zeleka", homephone="5floar", mobilephone="9876", workphone="456",
                    fax="45", email="65@qwe.ru", email2="4", email3="45", bday="", bmonth="February", byear="1992",
                    aday="30", amonth="January", ayear="1980", new_group=None, address2="someadr 78", secondaryphone="000",
                    notes="important notice"))

    #old_contacts = app.contact.get_contact_list() #этот вариант берет список контактов из UI
    old_contacts = db.get_contact_list()    #этот вариант берет список контактов из БД
    #создаем переменную с новыми данными для редактируемого контакта
    contact = Contact(firstname="Ivan", middlename="Pupkin", lastname="Petrovich", nickname="testnickname", photo=None,
            title="sometitle", company="Gazprom", address="759 Lenin st.", homephone="(987)4132", mobilephone="9123876",
            workphone="456123",
            fax="4 5321", email="65@qwe.ru", email2="4987zd@gmail.com", email3="asdfg@gmail.com", bday="8", bmonth="March", byear="1917",
            aday="30", amonth="January", ayear="1980", new_group=None, address2="someadr", secondaryphone="49577884",
            notes="nothing")
    index = randrange(len(old_contacts))  # рандомно выбираем какой контакт изменить
    contact.id = old_contacts[index].id #запомнили id выбранного контакта
    app.contact.modify_contact_by_index(index, contact) #изменяем выбранный контакт
    #new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list() #берем обновленный список контактов из БД
    assert len(old_contacts)  == len(new_contacts) #сравнение количества контактов после изменения
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max) # проверка содержания контактов
