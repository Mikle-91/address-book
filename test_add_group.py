# # -*- coding: utf-8 -*-
from application import Application
import time, unittest
from group import Group

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_app_dynamics_job(self):
        self.app.login(username="admin", password="secret")
        self.app.create_new_groupe(Group(name="uyt", header="headqwe", footer="footasd"))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()