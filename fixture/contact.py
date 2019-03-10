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
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)

        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)

        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)

        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)

        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home)

        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)

        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.work)

        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)

        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)

        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email2)

        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email3)

        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").send_keys(contact.byear)

        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").send_keys(contact.ayear)

        # если не указан аргумент группы, то тест падает т.к. открывает селект лист
        #driver.find_element_by_name("new_group").click()
        #Select(driver.find_element_by_name("new_group")).select_by_visible_text(contact.new_group)
        #driver.find_element_by_name("new_group").send_keys(contact.new_group)

        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.address2)

        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.phone2)

        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact
        driver.find_element_by_name("submit").click()

    def open_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

#### нахуевертил удаление элемента
    # def delete_first_contact(self):
    #     driver = self.app.driver
    #     self.open_home_page()
    #     driver.find_element_by_name("selected[]").click()        #select first contact
    #     self.accept_next_alert = True # подтверждение удаления
    #     # delete contact
    #     driver.find_element_by_xpath(
    #         "(.//*[normalize-space(text()) and normalize-space(.)='Select all'])[1]/following::input[2]").click()
    #     self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")

###


    # def open_home_page(self):     # с таким кодом валятся тесты
    #     driver = self.app.driver
    #     driver.get("http://localhost/addressbook/")

