# # -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app, json_modcontact, db): #альтернативный вариант data_contacts (вместо json_contact)
    if app.contact.count() == 0:  # проверка наличия групп перед изменением
        app.contact.create(
            # Contact(firstname="without note", middlename="pupkin", lastname="last", nickname="supernick", photo=None,
            #         title="sometitle", company="space", address="zeleka", homephone="5floar", mobilephone="9876", workphone="456",
            #         fax="45", email="65@qwe.ru", email2="4", email3="45", bday="", bmonth="February", byear="1992",
            #         aday="30", amonth="January", ayear="1980", new_group=None, address2="someadr 78", secondaryphone="000",
            #         notes="important notice"))
             Contact(firstname="NewName", lastname="last"))
    #old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="NewName", lastname="last")  # вместо json
    index = randrange(len(old_contacts))  # рандомно выбираем какую группу изменить
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    #new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    assert len(old_contacts)  == len(new_contacts) #сравнение количества контактов после изменения группы
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max) # проверка содержания контактов
