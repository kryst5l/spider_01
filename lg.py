import random
import time
from fake_useragent import UserAgent
import requests
ua = UserAgent()
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false'
header = {
    'Cookie':'_ga=GA1.2.293042736.1532056764; user_trace_token=20180720111924-b3f6433f-8bcb-11e8-9fab-525400f775ce; LGUID=20180720111924-b3f64660-8bcb-11e8-9fab-525400f775ce; _gid=GA1.2.228499205.1532056764; JSESSIONID=ABAAABAACBHABBI6B7E4612B6FB611AFDD6F27DFFEE0607; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532056764,1532061298; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=b212009e27317555b3eb0edfb29f8c17; LGSID=20180720152635-3bad65a3-8bee-11e8-9e4d-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fts%3D1532071594309%26serviceId%3Dlagou%26service%3Dhttps%25253A%25252F%25252Fwww.lagou.com%25252Fjobs%25252Flist_%252525E7%25252588%252525AC%252525E8%25252599%252525AB%25253FlabelWords%25253D%252526fromSearch%25253Dtrue%252526suginput%25253D%26action%3Dlogin%26signature%3D6115808270E248773EEB90EDDD47DE37; LG_LOGIN_USER_ID=be23fd44e90d3466ffa4caeb68b74bddcfdde697c4d9d80d97d599b61eca0ba9; _putrc=2093681E70058088123F89F2B170EADC; login=true; unick=%E9%BB%84%E4%BC%9F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=0fbe380e5294fe85687c94f8b35123c3749026b38acfa1bbc6c96e6d6cbfca7d; index_location_city=%E5%B9%BF%E5%B7%9E; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532071632; LGRID=20180720152712-51b7c485-8bee-11e8-9fc5-525400f775ce; SEARCH_ID=ef51b44a7a1c4e27bec4d6a8d03b2923',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':ua.chrome,
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}
# n = 1
# while n<21:
data = {
    'first': 'false',
    'pn':'21',
    'kd': '测试工程师',
}
res = requests.post(url, data=data, headers=header).content.decode()
with open('./拉钩/测试{}.html'.format(21), 'w',encoding=('utf8')) as f:
    f.write(res)
# n +=1
time.sleep(random.randint(5, 10))
print('finished')