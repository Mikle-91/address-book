# # -*- coding: utf-8 -*-
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
#from pymysql.converters import decoders

class ORMFixture:
    db = Database() # объект на основании которого делается привязка

    class ORMGroup(db.Entity):
        _table_= "group_list"    #свойства класса привязываем к полям таблицы "group_list"
        id= PrimaryKey(int, column='group_id') # column - название столбца в базе
        name = Optional(str, column='group_name') # optional т.к. поле может быть пустым
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True) #определяем множество объектов типа ORMContact
        #address_in_groups - таблица связующая табл.групп и табл.контактов, column="id" -столбец соответсвующий контакту
        #reverse="groups" - groups парное свойство для contacts, lazy=True по умолчанию свойства contacts пропускаются для оптимизации

    class ORMContact(db.Entity):
        _table_ ='addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated') #для фильтрации
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):     #привязка к базе данных. 'mysql' тип базы
        self.db.bind('mysql', host=host, database=name, user=user, password=password) # #добавить conv=decoders если будут ошибки
        self.db.generate_mapping() # тут сопоставляются свойства описанных классов с таблицами и полями таблиц БД
        sql_debug(True) # показывать запросы sql

    def convert_groups_to_model(self, groups): #преобразуем из  ORM формата в модельный объект - список
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session     #запускаем сессию для функции
    def get_group_list(self): #запрашиваем список групп из БД
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup)) # выборка объектов в формате list comprehension

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None)) # deprecated is None значит отфильтровать удаленые контакты

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0] #извлекаем группу с заданным идентификатором, берем первый из списка
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
