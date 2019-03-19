from model.contact  import Contact
import random
import time

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:         # проверка наличия групп перед удалением
        app.contact.create(Contact(firstname="Ivan"))
    old_contacts = db.get_contact_list()  #проверка удаления группы - берется состояние до внесения изменений
    contact = random.choice(old_contacts)   #рандомно выбираем какой контакт
    app.contact.delete_contact_by_id(contact.id)    #удаляем элемент из списка и сбрасываем кэш get_contact_list
    time.sleep(0.5) # ждем сброса кэша
    new_contacts = db.get_contact_list()     #проверка удаления группы - берется состояние после внесения изменений

    assert len(old_contacts) - 1 == len(new_contacts)   #проверка количесва групп после удаления
    old_contacts.remove(contact) #удаляем выбранный элемент из old_contacts
    assert old_contacts == new_contacts     #проверка идентичности групп (за вычетом удаленной групы) после удаления полученные из БД
    if check_ui:
        def clean(contact):  # clean убирает пробелы перед сравнением групп
            return Contact(id=contact.id, firstname=contact.firstname.strip())
        db_new_contacts= map(clean, db.get_contact_list())
        assert sorted(db_new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max) #сравниваем идентичность групп из БД и из UI

