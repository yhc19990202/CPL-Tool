from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CPL_login(driver, root_url, username, password):
	driver.get(root_url)
	time.sleep(1)
	driver.find_element(By.CLASS_NAME, "ivu-btn-circle").click()
	driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
	driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
	driver.find_element(By.CLASS_NAME, "ivu-btn-long").click()
	time.sleep(1)
	driver.get(root_url + '/admin/user')
