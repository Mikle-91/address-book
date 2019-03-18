import time
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
        self.contact_cache = None


    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)



    def modify_contact_by_index(self, index, contact):
        driver = self.app.driver
        self.open_home_page()
        # open modification form
        link= "http://localhost/addressbook/edit.php?id=" +str(contact.id)
        driver.get(link)
        # fill contact form
        self.fill_contact_form(contact)
        # submit modification
        driver.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):  # выделение контакта из списка кликом по чекбоксу
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()


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
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
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




    contact_cache = None

    def get_contact_list(self):     #загрузка списка контактов(имя, фамилия) из таблицы homepage
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):   #берем строку содержащюю данные одного контакта
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text   # в столбце 1 фамилия

                lastname = cells[1].text    # в столбце 2 имя
                id = cells[0].find_element_by_tag_name("input").get_attribute("value") # в столбце 0 id
                all_phones = cells[5].text     # в столбце 5 номера телефонов контакта отображаемые в несколько строк.
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row =driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self,index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1) #через регулярные выражения извлекаем домашний телефон из страницы
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)
