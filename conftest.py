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
    global target
    browser = request.config.getoption("--browser")  # передаем опц значение в конструктор application
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))  # путь к файлу target.json
        with open (config_file) as f:
            target=json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])   # если фикстура сломалась, запускаем новую
        #web_config = load_config(request.config.getoption("--target"))['web']
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)  #scope session чтобы логаут был после прохождения всех тестов, autouse чтобы автоматом завершил сессию
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox") #store значит сохранить значение параметра
    parser.addoption("--target", action="store", default="target.json")
