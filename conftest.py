# # -*- coding: utf-8 -*-
import pytest
import json
import os.path
import importlib
import jsonpickle

from fixture.application import Application
from fixture.db import DbFixture
fixture = None
target =None


def load_config(file): # выполняется загрузка конфигурации
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
    web_config = load_config(request.config.getoption("--target"))['web'] #загрузка конфигурации фикстуры из файла
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])   # если фикстура сломалась, запускаем новую
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope="session") #фикстура для тестов БД без запуска браузера
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db'] #загрузка конфигурации фикстуры из файла
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

def pytest_generate_tests(metafunc): #metafunc позволяет получить информацию о тестовой функции, динамически подставлять значения параметров
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"): #фильтруем по префиксу data_
            testdata = load_from_module(fixture[5:]) #загружаем тестовые данные из модуля с названием как фикстура минус первые 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata]) #параметризуем загруженную функцию
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f: #открываем файл с данными в json
        return jsonpickle.decode(f.read())          #читаем из него данные и перекодируем

