import requests
from selenium import webdriver

def copy_cookies(driver):
	session = requests.session()
	for cookie in driver.get_cookies():
		session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

	csrf = session.cookies.get("csrftoken")
	user_agent = driver.execute_script("return navigator.userAgent;")	
	session.headers.update({"user-agent": user_agent, 
							"X-Csrftoken": csrf, 
							"Content-Type": "application/json;charset=UTF-8"})
	return session