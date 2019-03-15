# # -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_empty(app):
    app.contact.create(Contact(firstname="noInfo Man"))

def test_add_contact(app):
     app.contact.create(Contact(firstname="Ivan", middlename="pupkin", lastname="last", nickname="supernick", photo=None,
                 title="sometitle", company="space", address="zeleka", homephone="5floar", mobilephone="9876", workphone="456",
                 fax="45", email="65@qwe.ru", email2="4", email3="45", bday="", bmonth="February", byear="1992",
                 aday="30", amonth="January", ayear="1980", new_group=None, address2="someadr", secondaryphone="49577884",
                 notes="nothing"))
