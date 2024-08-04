import requests
import json, openpyxl, csv
import random, time
from CPL_students import read_students
from OJ_API import get_user_data

# user_url_prefix = "https://bach.ee.ntu.edu.tw" + "/api/admin/user?id="
change_url = "https://bach.ee.ntu.edu.tw" + "/api/admin/user"

# def read_user_data(session, user_url):
# 	reply = json.loads( session.get(user_url, verify = False).text )
# 	if reply["error"] == "error":
# 		return "error"
# 	return reply["data"]

def enable_users(session, root_url, users):
	for idx in users:
		user_data = get_user_data(session, root_url, idx)
		if user_data == "error":
			print( "User {} doesn't exist.".format(idx) )
		else:
			user_data["is_disabled"] = False
			reply = session.put(change_url, data = json.dumps(user_data), verify = True)
			print( "User {} success.".format(idx) )
		time.sleep(0.2)

def disable_users(session, root_url, users):
	for idx in users:
		user_data = get_user_data(session, root_url, idx)
		if user_data == "error":
			print( "User {} doesn't exist.".format(idx) )
		else:
			user_data["is_disabled"] = True
			reply = session.put(change_url, data = json.dumps(user_data), verify = False)
			print( "User {} success.".format(idx) )
		time.sleep(0.2)

def random_string(sample_string, length):
	result = ''.join((random.choice(sample_string)) for x in range(length))
	return result

def generate_password(postfix):
	students = read_students('./excel/student.xlsx')

	with open('./excel/exam_account.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)

		for i, student in enumerate(students):
			S = random_string('QWERTYUPASDFGHJKLZXCVBNM', 3) + random_string('0123456789', 4)
			writer.writerow([student+postfix, S, student+"@ntu.edu.tw", student])
