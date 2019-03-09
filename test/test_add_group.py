# # -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_app_dynamics_job(app):
    app.session.login(username="admin", password="secret")
    app.create_new_groupe(Group(name="uyt", header="headqwe", footer="footasd"))
    app.session.logout()
