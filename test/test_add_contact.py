# # -*- coding: utf-8 -*-
from model.contact import Contact
from datetime import datetime

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Ivan", last_name="", email="Ivanpet@gmail.com"))
    app.session.logout()

