# # -*- coding: utf-8 -*-
from model.group import Group


def test_app_dynamics_job(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="uyt", header="headqwe", footer="footasd"))
    app.session.logout()
