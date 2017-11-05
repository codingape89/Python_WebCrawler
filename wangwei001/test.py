# coding=utf-8
#code=utf-8
import urllib2
import urllib

from bs4 import BeautifulSoup

from wangwei001 import helper

# url='http://index.0256.cn/request_report_for_pub_price.action'
# value={
#     'orgId':'',
#     'type':'-1',
#     'marketId':'1',
#     'cateId':'5',
#     'startLine':'广州',
#     'endLine':'北京',
#     'startTime	':'',
#     'pageNumber':'1',
#     'endTime':''
# }
# data=urllib.urlencode(value)#对value进行编码，转换为标准编码#
# req=urllib2.Request(url,data)#向url发送请求，并传送表单data#
# response=urllib2.urlopen(req)#获取响应#
# the_page=response.read()#解析#
# # print the_page#显示#
#
# soup = BeautifulSoup(the_page, 'html.parser')
# helper.getPageCount(soup)


# data_city_from = helper.getCity()
# for data in data_city_from:
#     print data

# soup = helper.getsoup_by_query('5', '广州', '北京', '2')
# # print soup
# helper.getdata_from_soup(soup)

helper.write_excel2007('1', '2');
