# coding=utf-8
#code=utf-8
import urllib2
url="http://www.baidu.com"
req=urllib2.Request(url)#req表示向服务器发送请求#
response=urllib2.urlopen(req)#response表示通过调用urlopen并传入req返回响应response#
the_page=response.read()#用read解析获得的HTML文件#
print the_page
#在屏幕上显示出来#