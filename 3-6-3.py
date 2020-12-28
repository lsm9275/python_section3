import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument('--headless')

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path='D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/webdriver/firefox/geckodriver')
driver.set_window_size(1920,1280)

#driver.implicitly_wait(5)
driver.get('https://google.com')
driver.save_screenshot('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/web1_ff.png')
#time.sleep(5)
#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)
driver.save_screenshot('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/web2_ff.png')
#driver.implicitly_wait(5)
driver.quit()
print('스크린샷 완료')