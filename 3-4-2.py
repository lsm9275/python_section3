import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.parse as rep
import urllib.request as req
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#login user information
LOGIN_INFO = {
    'email':'lsm9275@gmail.com',
    'password':'vhgkdrh50!'
}

#session creation, maintain in with block
with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/api/signin', data=LOGIN_INFO)
    #html source check
    #print('login_req', login_req.text)
    #header check
    #print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        base = 'https://www.inflearn.com/dashboard'
        #quote = 'python-'+rep.quote_plus('파이썬-웹-데이터-크롤링/')
        #print(quote)
        #board = 'dashboard'
        post_one = s.get(base)
        #print(post_one.text)
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        course = soup.select('div.course_container > a > div')
        print(course[0])
        #for i,z in enumerate(course,1):
        #    print(z)
            #fullFileName = os.path.join('c:/',str(i)+'txt')
            #req.urlretrieve()
        #print(course.text)
       