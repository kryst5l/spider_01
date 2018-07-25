"""
拉钩
"""
# import csv
# import json
#
# n = 1
# position = []
# while n<=21:
#     with open('./拉钩/测试{}.html'.format(n), 'r',encoding=('utf8'))as f:
#        res = f.read()
#     res = json.loads(res)
#     con_list = res['content']['positionResult']['result']
#     position.append(con_list)
#     n+=1
#
# with open('拉钩测试岗位.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows([['companyFullName', 'city', 'education', 'workYear','salary']])
#     for i in position:
#         for n in i:
#             writer.writerows([[n['companyFullName'], n['city'], n['education'], n['workYear'], n['salary']]])
import csv

"""
智联
"""
# import csv
# import json
#
# n = 1
# position = []
# while n<=6:
#     with open('./zhilian/第{}页.json'.format(n), 'r',encoding=('utf8'))as f:
#        res = f.read()
#     res = json.loads(res)
#     con_list = res['data']['results']
#     position.append(con_list)
#     n+=1
#
# with open('智联测试岗位.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows([['companyFullName', 'city', 'education', 'workYear','salary']])
#     for i in position:
#         for n in i:
#             writer.writerows([[n['company']['name'], n['city']['display'], n['eduLevel']['name'], n['workingExp']['name'], n['salary']]])

# """
# boss测试岗位
# """
#
# from lxml import etree
# n = 1
# with open('BOSS测试岗位.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows([['companyFullName', 'city', 'education', 'workYear','salary']])
#     while n <= 10:
#         with open('./BOSS/第{}页.html'.format(n), 'r', encoding=('utf-8'))as f:
#             res = f.read()
#         html = etree.HTML(res)
#         li_list = html.xpath('//*[@id="main"]/div/div[2]/ul/li')
#         dic = {}
#         for li in li_list:
#             # print(li)
#             dic['companyFullName'] = li.xpath("./div/div[2]/div/h3/a/text()")[0]
#             dic['salary'] = li.xpath("./div/div[1]/h3/a/span/text()")[0]
#             dic['edu'] = li.xpath("./div/div[1]/p/text()")[2]
#             dic['workYear'] = li.xpath("./div/div[1]/p/text()")[1]
#             dic['city'] = li.xpath("./div/div[1]/p/text()")[0]
#             writer.writerows([[dic['companyFullName'], dic['city'],  dic['edu'], dic['workYear'], dic['salary']]])
#         n +=1

"""
前程无忧测试岗位
"""
# from lxml import etree
# n = 1
# with open('前程无忧测试岗位.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows([['companyFullName', 'city', 'education', 'workYear','salary']])
#     while n < 10:
#         print(1)
#         with open('./前程无忧/测试{}.html'.format(n), 'r', encoding=('utf-8'))as f:
#             print(2)
#             res = f.read()
#         html = etree.HTML(res)
#         li_list = html.xpath('//div[@id="resultList"]/div[@class="el"]')
#         print(li_list)
#         for i in li_list:
#             print(4)
#             company_name = i.xpath('./span[1]/a/@title')[0]
#             city = i.xpath('./span[2]/text()')[0]
#             try:
#                 salary = i.xpath('./span[3]/text()')[0]
#             except:
#                 pass
#             else:
#                 salary = '保密'
#             try:
#                 salary = i.xpath('./span[3]/text()')[0]
#             except:
#                 salary = '保密'
#
#             print(company_name)
#             writer.writerows([[company_name,city ,'', '', salary]])
#         n+=1
#
