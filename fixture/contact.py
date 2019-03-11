import time
from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        self.open_home_page()
        #init contact creation
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        self.fill_contact_form_date(contact)
        # submit form
        driver.find_element_by_name("submit").click()


    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        driver.find_element_by_xpath("//img[contains(@title,'Edit')]").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        driver.find_element_by_name("update").click()
        self.open_home_page()

    def open_home_page(self):
        driver = self.app.driver
        if not len(driver.find_elements_by_xpath("//a[contains(.,'All e-mail')]")) > 0:
            driver.find_element_by_link_text("home").click()


    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form_date(self, contact): # отдельная обработка т.к. там dropdown list элементы
        driver = self.app.driver
        self.change_field_value_date("bday", contact.bday)
        self.change_field_value_date("bmonth", contact.bmonth)
        self.change_field_value_date("aday", contact.aday)
        self.change_field_value_date("amonth", contact.amonth)

    def change_field_value_date(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            Select(driver.find_element_by_name(field_name)).select_by_visible_text(text)


    def count(self):
        driver = self.app.driver
        self.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

