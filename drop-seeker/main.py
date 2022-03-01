import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {
    'userId': 'hyuntae0611',
    'userPassword': 'Hyuntae12#$'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://sugang.snu.ac.kr/', data=LOGIN_INFO)
    # 어떤 결과가 나올까요?
    print(login_req.status_code)

    if login_req.status_code != 200:
        raise Exception('로그인 실패!')

#x_path = '//*[@id="mbMenuCartEm"]'

post_one = s.get('https://sugang.snu.ac.kr/')
soup = bs(post_one.text, 'html.parser')

title = soup.select('#sugangGuideContents > div.con-box > div > span:nth-child(1) > font > b')
print(title[0].text)

##계속 list index out of range 오류가 뜬다.....

