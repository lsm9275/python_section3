import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print('hi')
class NcafeWriteAtt:
    #초기화 실행(Webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")#CLI
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

    #네이버카페 로그인
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        self.driver.find_element_by_name('id').send_keys('lsm9275')
        self.driver.find_element_by_name('pw').send_keys('vhgkdrh50!')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(30)
