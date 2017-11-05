# coding=UTF-8
import urllib
import urllib2

from bs4 import BeautifulSoup

import helper

# attribute2 = helper.getattribute2("http://index.0256.cn/expx.htm")
# for data in attribute2:
#     print data

# city = helper.getCity("http://index.0256.cn/expx.htm")
# for data in city:
#     print data

# value = {
#     'markedId': 1,
#     'attribute1': 5,
#     'exponentTypeId': 5,
#     'cateId': 2,
#     'attribute2': "%E5%8D%8E%E5%8C%97"
# }
# data = urllib.urlencode(value)
# req = urllib2.Request("http://index.0256.cn/expcenter_trend.action?marketId=1&attribute1=5&exponentTypeId=5&cateId=2&attribute2=&city=&startLine=&endLine=")
# req = urllib2.Request("http://index.0256.cn/expcenter_trend.action?markedId=1&attribute1=5&exponentTypeId=5&cateId=2&attribute2=&city=&startLine=&endLine=")
# req = urllib2.Request("http://index.0256.cn/expcenter_trend.action?marketId=1&attribute1=5&exponentTypeId=5")
# response = urllib2.urlopen(req)
# the_page = response.read()
# soup = BeautifulSoup(the_page, 'html.parser')

# soup = helper.getsoup_by_query("http://index.0256.cn/expcenter_trend.action", 1, 5, 5, 2, str("华北"), "", "", "")
# print soup
#
#
# req = urllib2.Request("http://index.0256.cn/expcenter_trend.action?marketId=1&attribute1=5&exponentTypeId=5")
# response = urllib2.urlopen(req)
# the_page = response.read()
# soup = BeautifulSoup(the_page, 'html.parser')

# soup = helper.getsoup_by_query("http://index.0256.cn/expcenter_trend.action", 1, 5, 5, 2, str("华北"), "", "", "")
# print soup



mainurl = "http://index.0256.cn/expx.htm"
list_attribute2 = helper.getattribute2(mainurl)
for data in list_attribute2:
    print(data)
