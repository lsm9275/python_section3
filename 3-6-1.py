import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.PhantomJS('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/webdriver/phantomJS/phantomjs')

driver.implicitly_wait(5)
driver.get('https://google.com')
driver.save_screenshot('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/web1.png')
driver.implicitly_wait(5)

driver.get('https://www.daum.net')
driver.save_screenshot('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/web2.png')
driver.implicitly_wait(5)
driver.quit()
print('스크린샷 완료')
