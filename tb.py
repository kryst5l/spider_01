import time
import random
from fake_useragent import UserAgent
ua = UserAgent()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome()
driver.set_window_size(1080,5000)
driver.get("https://www.taobao.com/")
driver.find_element_by_id('q').send_keys('手机')
driver.find_element_by_class_name('btn-search').click()
time.sleep(2)
while driver.find_element_by_class_name('icon-btn-next-2'):
    num = driver.find_element_by_class_name('current').text
    driver.find_element_by_class_name('icon-btn-next-2').click()
    print(driver.save_screenshot('./淘宝/淘宝手机{}.png'.format(num)))
    print('ok')
    time.sleep(random.randint(2,5))
print('finished')
