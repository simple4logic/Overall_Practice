from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {
    'userId': 'hyuntae0611',
    'userPassword': 'Hyuntae12#$'
}

url = "https://sugang.snu.ac.kr/"

driver.get(url)
time.sleep(1)

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://sugang.snu.ac.kr/', data=LOGIN_INFO)

    print(login_req.status_code)

    if login_req.status_code != 200:
        raise Exception('로그인 실패!')

x_path1 = '//*[@id="header"]/div[2]/div[1]/button[1]'
searchbox = driver.find_element_by_xpath(x_path1)
searchbox.click()
time.sleep(1)

x_path2 = '//*[@id="HD100"]/div/div/div[1]/fieldset/div[3]/button[1]'
searchbox = driver.find_element_by_xpath(x_path2)
searchbox.click()
time.sleep(1)

html = driver.page_source
soup = bs(html, 'html.parser')
string = soup.select_one('#skip-con > div > div.course-list-wrap.pd-r > div.course-info-list > div:nth-child(1) > div.left > label > input[type=radio]:nth-child(1)')
