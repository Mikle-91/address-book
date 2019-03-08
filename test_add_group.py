# # -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest
from group import Group

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/addressbook/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        self.login(username="admin", password="secret")
        self.create_new_groupe(Group(name="uyt", header="headqwe", footer="footasd"))
        self.logout()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_link_text("Logout").click()

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

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_id("LoginForm").submit()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit() #закрытие браузера

if __name__ == "__main__":
    unittest.main()