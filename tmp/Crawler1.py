# coding=utf-8
#code=utf-8
import urllib2
import urllib
url='http://index.0256.cn/pricex.htm'
value={
    'name':'BUPT',
    'age':'60',
    'location':'Beijing'#字典中的内容随意，不影响#
}
data=urllib.urlencode(value)
#对value进行编码，转换为标准编码#
req=urllib2.Request(url,data)#向url发送请求，并传送表单data#
response=urllib2.urlopen(req)#获取响应#
the_page=response.read()#解析#
print the_page#显示#