import time

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
        driver.find_element_by_name("firstname").send_keys(contact.first_name)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)

        # submit contact
        driver.find_element_by_name("submit").click()



    def open_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    # def open_home_page(self):     # с таким кодом валятся тесты
    #     driver = self.app.driver
    #     driver.get("http://localhost/addressbook/")

