import requests, json, time
from math import ceil

def get_user_data(session, root_url, user_id):
	payload = {"id": user_id}
	reply = json.loads( session.get(root_url + "/api/admin/user", params = payload).text )
	if reply["error"] == "error":
		return "error"
	return reply["data"]

def get_contest_info(session, root_url, contest_id):
	payload = {"id": contest_id}
	reply = json.loads( session.get(root_url + "/api/contest", params = payload).text )
	contest_name = reply["data"]["title"]

	payload = {"contest_id": contest_id}
	reply = json.loads( session.get(root_url + "/api/contest/problem", params = payload).text )
	problems = reply["data"]

	return contest_name, problems

def get_contest_submissions(session, root_url, myself=0, result='', username='', page=0, contest_id=0, limit=10, offset=0):
	payload = {}
	for key, value in locals().items():
		if key != 'session' and key != 'root_url':
			payload[key] = value

	return json.loads( session.get(root_url + "/api/contest_submissions", params = payload).text )

def get_contest_submissions_all(session, root_url, contest_id):
	reply = get_contest_submissions(session, root_url, contest_id=contest_id)
	total_sub = reply["data"]["total"]
	max_query = 250 # due to API retriction
	page_num = ceil(total_sub / max_query)
	submissions = []
	for page in range(page_num):
		print( "{}/{}".format(min(max_query*(page+1), total_sub), total_sub) )
		reply = get_contest_submissions(session, root_url, contest_id=contest_id, limit=max_query, offset=max_query*page)		
		submissions += reply["data"]["results"]
		time.sleep(1)
	return submissions
