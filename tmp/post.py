# coding=utf-8
#code=utf-8
import urllib2
import urllib
url='http://index.0256.cn/request_report_for_pub_price.action'
value={
    'orgId':'',
    'type':'-1',
    'marketId':'1',
    'cateId':'5',
    'startLine':'广州',
    'endLine':'北京',
    'startTime	':'',
    'endTime':''
}
data=urllib.urlencode(value)#对value进行编码，转换为标准编码#
req=urllib2.Request(url,data)#向url发送请求，并传送表单data#
response=urllib2.urlopen(req)#获取响应#
the_page=response.read()#解析#
print the_page#显示#