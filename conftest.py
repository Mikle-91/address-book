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
    browser = request.config.getoption("--browser")  # передаем опц значение в конструктор application
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
        #web_config = load_config(request.config.getoption("--target"))['web']
    else:
        if not fixture.is_valid(): # если фикстура сломалась, запускаем новую
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


# @pytest.fixture(scope="session")
# def db(request):
#     db_config = load_config(request.config.getoption("--target"))['db']
#     dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
#     def fin():
#         dbfixture.destroy()
#     request.addfinalizer(fin)
#     return dbfixture


@pytest.fixture(scope="session", autouse=True)  #scope session чтобы логаут был после прохождения всех тестов, autouse чтобы автоматом завершил сессию
#@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox") #store значит сохранить значение параметра
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")













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
