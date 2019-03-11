# # -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="changed first name4"))

def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="changed mid name4"))

def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="changed last name4"))


