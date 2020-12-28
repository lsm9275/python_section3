import sys
import io
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청 URL
URL = 'https://www.wishket.com/accounts/login/'

#Fake User Agent 생성
ua = UserAgent()
#print(ua.ie)
#print(ua.chrome)
#print(ua.random)

with requests.Session() as s:
    #URL 연결
    s.get(URL)
    #로그인 정보 페이로드
    LOGIN_INFO = {
        'identification':'lsm9275',
        'password':'vhgkdrh50!',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }
    #요청
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})
    #html 결과 확인
    #print('response', response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        projectList = soup.select('div.user-project > div')
        #print(projectList)
        for i in projectList:
            print(i.text)

