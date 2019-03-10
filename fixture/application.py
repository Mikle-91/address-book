from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/addressbook/"  # удалить?
        self.verificationErrors = []# удалить?
        self.accept_next_alert = True   # удалить?
        self.session =SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)



    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()# закрытие браузера