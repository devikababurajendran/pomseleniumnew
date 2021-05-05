from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\Devika B Raj\Downloads\chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.ID, "welcome").click()
        self.driver.find_element(By.LINK_TEXT,"Logout").click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


