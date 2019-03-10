# # -*- coding: utf-8 -*-
from model.contact import Contact
from datetime import datetime

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivanfirstlong", middlename="pupkin", lastname="last", nickname="supernick", title="sometitle", company="space", address="zeleka", home="5floar", mobile="9876", work="456", fax="45", email="65@qwe.ru", email2="4", email3="45", bday="", bmonth="February", byear="1992", aday="30", amonth="January", ayear="1980", new_group="", address2="someadr", phone2="000", notes="nothing"))
    app.session.logout()

