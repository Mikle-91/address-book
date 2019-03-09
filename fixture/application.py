from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/addressbook/"  # удалить?
        self.verificationErrors = []# удалить?
        self.accept_next_alert = True   # удалить?
        self.session =SessionHelper(self)



    def create_new_groupe(self, Group):
        driver = self.driver
        self.open_groups_page()
        # init groupe creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(Group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(Group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(Group.footer)
        # submit group
        driver.find_element_by_name("submit").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()



    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")


    def destroy(self):
        self.driver.quit()  # закрытие браузера