import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#chrome_options = Options()
#chrome_options.add_argument('--headless')

#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

#driver.implicitly_wait(5)
driver.get('https://www.inflearn.com/')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="header"]/nav/div[2]/div/div[2]/div[2]/div[2]/a[1]').click()
time.sleep(1)
driver.find_element_by_class_name('input.email').send_keys('lsm9275@gmail.com')
time.sleep(1)
driver.find_element_by_class_name('input.pwd').send_keys('vhgkdrh50!')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/button').click()
time.sleep(1)

#time.sleep(5)
#driver.implicitly_wait(5)

'''driver.get('https://www.daum.net')
#time.sleep(5)
driver.save_screenshot('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section3/web2_ch.png')
#driver.implicitly_wait(5)
driver.quit()
print('스크린샷 완료')'''
