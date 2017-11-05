# coding=utf-8
import json
import urllib
import urllib2
import xlrd
from pyExcelerator import *
import xlsxwriter

from bs4 import BeautifulSoup

def getattribute2(url):
    soup_attribute2 = getHtml(url)
    # print soup_transtype
    question = soup_attribute2.findAll('div', {'class': "starTime sct2"})
    select = question[1].contents[1]
    data_list = []
    for d in select.findAll('option'):
        str_id = d['value']
        data_list.append(str_id)
    return data_list

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def getCity(url):
    soup_City = getHtml(url)
    question = soup_City.findAll('div', {'class': "tcdiv_ul"})
    len = (int)(question.__len__())
    data_list = []
    for i in range(0,len):
        select = question[i].contents[1]
        # print select
        for d in select.findAll('li'):
            str_name = d.string
            # print str_name
            data_list.append(str_name)
    return data_list

# soup = helper.getsoup_by_query(str(requesturl), str(marketId), str(attribute1), str(exponentTypeId), str(cateId), str(attribute2), str(city), str(startLine), str(endLine) )
def getsoup_by_query(requesturl, marketId, attribute1, exponentTypeId, cateId, attribute2, city, startLine, endLine):
    value={
        'marketId':marketId,
        'attribute1':attribute1,
        'exponentTypeId':exponentTypeId,
        'cateId':cateId,
        'attribute2':attribute2,
        'city	':city,
        'startLine':startLine,
        'endLine':endLine
    }
    data=urllib.urlencode(value)
    req=urllib2.Request(requesturl,data)
    response=urllib2.urlopen(req)
    the_page=response.read()
    soup = BeautifulSoup(the_page, 'html.parser')
    return soup

# soup = helper.getsoup_by_query(str(requesturl), str(marketId), str(attribute1), str(exponentTypeId), str(cateId), str(attribute2), str(city), str(startLine), str(endLine) )
def getsoup_by_query2(requesturl, paralist):
    # "http://index.0256.cn/expcenter_trend.action?marketId=1&attribute1=5&exponentTypeId=5&cateId=2&attribute2=%E5%8D%8E%E5%8C%97&city=&startLine=&endLine="
    queryurl = str(requesturl);
    for i in range(0, len(paralist)):

        if i==0 :
            queryurl += "?" + paralist[i][0] + "=" + paralist[i][1];
        else :
            queryurl += "&" + paralist[i][0] + "=" + paralist[i][1];
    # print(queryurl)
    req=urllib2.Request(queryurl)
    response=urllib2.urlopen(req)
    the_page=response.read()
    return the_page

def getdata_from_soup(page, paralist):
    data_list = []
    ddict = json.loads(page)
    rownum = int(ddict['pager']['total'])
    dataresult = ddict['pager']['list']
    for i in range(0, rownum):
        row_list = []
        # print(dataresult[i])
        for para in paralist:
            row_list.append(para[1])
        dataonerow = dataresult[i];
        row_list.append(100*(dataonerow.get('exp1')))
        row_list.append(dataonerow.get('chain'))
        row_list.append(dataonerow.get('year'))
        row_list.append(dataonerow.get('cycle'))
        row_list.append(dataonerow.get('periodTime'))
        row_list.append(100*(dataonerow.get('exp1')))
        row_list.append(100*(dataonerow.get('exp2')))
        row_list.append(100*(dataonerow.get('exp3')))
        data_list.append(row_list)
    # print data_list
    return data_list

def add_list(list_all, list_part):
    size_part = len(list_part)
    for i in range(0, size_part):
        list_all.append(list_part[i])

def read_excel2003(filename, list):
    bk = xlrd.open_workbook(filename)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % filename
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows, ncols)
    # 获取第一行第一列数据
    cell_value = sh.cell_value(1, 1)
    # print cell_value
    list = []
    # 获取各行数据
    for i in range(1, nrows):
        row_data = sh.row_values(i)
        list.append(row_data)

def write_excel2003(filename, list):
    w = Workbook()  # 创建一个工作簿
    ws = w.add_sheet('Hey, Hades')  # 创建一个工作表
    size_list = len(list)
    for i in range(0, size_list):
        list_row = list[i]
        size_list_row = len(list_row)
        for j in range(0, size_list_row):
            ws.write(i, j, size_list_row[j])
    w.save(filename)

def read_excel2007(filename, list):
    print 'not yet done'

def write_excel2007(filename, tlist):
    test_book = xlsxwriter.Workbook(filename)
    worksheet = test_book.add_worksheet('sheet1')
    size_list = len(tlist)
    for i in range(0, size_list):
        list_row = tlist[i]
        size_list_row = len(list_row)
        for j in range(0, size_list_row):
            worksheet.write(i, j, list_row[j])
    test_book.close()

def print_list0(list):
    for data in list:
        print str(data)+' | ',
    print

def print_list1(list):
    for data in list:
        print data

def print_list2(list):
    for data in list:
        print_list0(data)
