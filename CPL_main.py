import sys, time, random
import warnings, getpass
import requests
from selenium import webdriver
from open_chrome_driver import open_chrome_driver

from CPL_login import CPL_login
from copy_cookies import copy_cookies
from CPL_contest import save_scores, save_codes, download_contest
from CPL_user import enable_users, disable_users, generate_password

if __name__ == '__main__':
	warnings.filterwarnings('ignore')
	# Input Basic Information
	domain_name = input("Domain Name:")
	username = input("Username:")
	password = getpass.getpass("Password:")
	# Login
	root_url = "https://{}.ee.ntu.edu.tw".format(domain_name)
	driver = open_chrome_driver()
	CPL_login(driver, root_url, username, password)
	session = copy_cookies(driver)

	# Select Operations
	options = ["Contest", "User", "Password"]
	for idx, option in enumerate(options):
		print("{}: {}".format(idx, option))
	print("\n")

	opt = int(input("Operation: "))
	if opt == 0:
		contest_id = input("Contest ID: ")
		contest_func = {0: save_scores, 
						1: save_codes, 
						2: download_contest}
		
		for idx, func in contest_func.items():
			print("{}: {}".format(idx, func.__name__))
		contest_opt = int(input("Function: "))
		contest_func[contest_opt](session, root_url, contest_id)
	
	if opt == 1:
		idx_head = int(input("start: ") )
		idx_tail = int(input("end: ") ) + 1
		users = range(idx_head, idx_tail)
		user_func = {0: disable_users, 
					 1: enable_users}
		
		for idx, func in user_func.items():
			print("{}: {}".format(idx, func.__name__))
		user_opt = int(input("Function: "))
		user_func[user_opt](session, root_url, users)
	
	if opt == 2:
		postfix = str(input("postfix: "))
		generate_password(postfix)

	driver.quit()
	print("Finish!")
