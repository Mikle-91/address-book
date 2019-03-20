# # -*- coding: utf-8 -*-
from model.contact import Contact
# статичные тестовые данные для создания контакта

testdata = [
    Contact(firstname="Empty contact"),

    Contact(firstname="Ivan", middlename="Pupkin", lastname="Petrovich", nickname="testnickname", photo=None,
            title="sometitle", company="Gazprom", address="759 Lenin st.", homephone="(987)4132", mobilephone="9123876",
            workphone="456123",
            fax="4 5321", email="65@qwe.ru", email2="4987zd@gmail.com", email3="asdfg@gmail.com", bday="8", bmonth="March", byear="1917",
            aday="30", amonth="January", ayear="1980", new_group=None, address2="someadr", secondaryphone="49577884",
            notes="nothing")
]


