from selenium.webdriver import Chrome
import time
driver = Chrome()
driver.get("https://search.51job.com/list/180200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")
time.sleep(2)
n = 1
while n<=9:
    next = driver.find_element_by_id('rtNext').click()
    content = driver.page_source
    with open('./前程无忧/测试{}.html'.format(n), 'w',encoding='utf-8') as f:
        f.write(content)
    time.sleep(2)
    n+=1

driver.close()

