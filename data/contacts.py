# # -*- coding: utf-8 -*-
from model.contact import Contact


testdata = [
    Contact(firstname="Empty contact"),

    Contact(firstname="Ivan", middlename="Pupkin", lastname="Petrovich", nickname="testnickname", photo=None,
            title="sometitle", company="Gazprom", address="759 Lenin st.", homephone="5floar", mobilephone="9876",
            workphone="456",
            fax="45", email="65@qwe.ru", email2="4", email3="45", bday="", bmonth="February", byear="1992",
            aday="30", amonth="January", ayear="1980", new_group=None, address2="someadr", secondaryphone="49577884",
            notes="nothing")
]


