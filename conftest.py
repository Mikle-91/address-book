# # -*- coding: utf-8 -*-
import pytest
import json
import os.path
import importlib
#import jsonpickle

from fixture.application import Application
from fixture.db import DbFixture
fixture = None
target =None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser)
        fixture.session.login(username="admin", password="secret")
        #web_config = load_config(request.config.getoption("--target"))['web']
        if fixture is None or not fixture.is_valid():
            fixture = Application(browser=browser)
            fixture.session.login(username="admin", password="secret")
    # else:
    #     if not fixture.is_valid():
    #         fixture = Application()
    #         fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'],name=db_config['name'],user=db_config['user'], password=db_config['password'])
    def fin():
            dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


# @pytest.fixture #без пяти меннут переделаная на половину
# def app(request):
#     global fixture
#     if fixture is None:
#         browser = request.config.getoption("--browser")
#         web_config = load_config(request.config.getoption("--target"))['web'] # до сюда
#         fixture = Application(browser=browser)
#         fixture.session.login(username="admin", password="secret")
#     else:
#         if not fixture.is_valid():
#             fixture = Application()
#             fixture.session.login(username="admin", password="secret")
#     return fixture





# @pytest.fixture(scope="session")  #предыдущая версия фикстуры
# def app(request):
#     fixture = Application()
#     fixture.session.login(username="admin", password="secret")
#     def fin():
#         fixture.session.logout()
#         fixture.destroy()
#     request.addfinalizer(fin)
#     return fixture
