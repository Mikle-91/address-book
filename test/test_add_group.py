# # -*- coding: utf-8 -*-
from model.group import Group


def test_app_dynamics_job(app):
    app.group.create(Group(name="uyt", header="headqwe", footer="footasd"))

