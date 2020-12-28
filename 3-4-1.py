import sys
import io
from bs4 import BeautifulSoup
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#login user information
LOGIN_INFO = {
    'user_id':'lsm9275',
    'user_pw':'vhgkdrh50!'
}

#session creation, maintain in with block
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    #html source check
    #print('login_req', login_req.text)
    #header check
    #print('heaters', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://bbs.ruliweb.com/market/board/45/read/186263?')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        article = soup.select_one('div.view_content.autolink > div').find_all('p')
        for i in article:
            if i.string is not None:
                print(i.string)
