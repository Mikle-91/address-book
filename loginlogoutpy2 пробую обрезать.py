# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium import webdriver
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
