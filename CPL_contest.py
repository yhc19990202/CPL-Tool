import requests, openpyxl, json
import time, os, re
from OJ_API import get_contest_info, get_contest_submissions_all
from CPL_students import read_students

def save_scores(session, root_url, contest_id):
	contest_name, problems = get_contest_info(session, root_url, contest_id)
	problem_num = len(problems)
	# initalize score table
	students = read_students('./excel/student.xlsx')
	score_table = dict()
	for student_id in students:
		score_table[student_id] = [0] * problem_num
	# query all submissions in single contest by API
	submissions = get_contest_submissions_all(session, root_url, contest_id)
	for sub in submissions:
		username, problem_id, score = sub["username"], int(sub["problem"]), sub["statistic_info"]["score"]
		if score_table.get(username, None) is not None:
			score_table[username][problem_id-1] = max(score, score_table[username][problem_id-1])
	# save as excel
	wb = openpyxl.Workbook()
	sheet = wb.create_sheet(contest_name, 0)
	sheet.append(["ID"] + list(range(1, problem_num+1)))
	for student_id in students:
		sheet.append([student_id] + score_table[student_id])
	wb.save("./excel/" + contest_name + "_score.xlsx")

def save_codes(session, root_url, contest_id):
	contest_name, problems = get_contest_info(session, root_url, contest_id)
	problem_num = len(problems)
	# query all submissions in single contest by API
	submissions = get_contest_submissions_all(session, root_url, contest_id)

	os.chdir("./submissions/")
	for i, submission in enumerate(submissions):
		print('{}/{}'.format(1+i, len(submissions) ), end='\r')
		student_id = submission["username"]		
		problem_id = submission["problem"]
		score = submission["statistic_info"]["score"]

		code_url = root_url + "/api/submission?id=" + submission["id"]
		reply = json.loads( session.get(code_url).text )
		create_time = reply["data"]["create_time"][0:19]
		code = reply["data"]["code"]
		file_name = contest_name + '_' + student_id + '_' + str(problem_id) + '_score_' + str(score) + '_' + create_time
		file_name = re.sub(r'[ T]', '_', file_name)
		file_name = re.sub(r'[-:]', '', file_name)
		
		f = open( file_name + ".cpp", 'w', encoding='UTF-8' )
		f.write(code)
		f.close()
	os.chdir("../")

def download_contest(session, root_url, contest_id):
	contest_name, problems = get_contest_info(session, root_url, contest_id)

	id_dict = {}
	for problem in problems:
		id_dict[ problem["_id"] ] = problem["id"] 
	id_dict = dict(sorted(id_dict.items()))
	print(id_dict)

	for display_id, problem_id in id_dict.items():
		url = "{}/api/admin/export_problem?problem_id={}".format(root_url, problem_id)
		response = session.get(url)
		fn = "./problems/{}_{}.zip".format(contest_name, display_id)
		with open(fn, "wb") as file:
			file.write(response.content)
