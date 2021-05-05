from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

driver = webdriver.Chrome(executable_path=r"C:\Users\Devika B Raj\Downloads\chromedriver")
driver.maximize_window()
time.sleep(5)
driver.get("http://127.0.0.1:8000/dashboard")
driver.find_element(By.ID,"title").send_keys("Test1")
driver.find_element(By.ID,"description").send_keys("Test sample document")
driver.find_element(By.ID,"priority").send_keys("6")
driver.find_element(By.XPATH,"/html/body/form/button").click()
driver.quit()


