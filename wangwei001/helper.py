# coding=utf-8
import urllib
import urllib2
import xlrd
from pyExcelerator import *
import xlsxwriter

from bs4 import BeautifulSoup

url_transport = "http://index.0256.cn/pricex.htm"

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def getTranstype():
    soup_transtype = getHtml(url_transport)
    # print soup_transtype
    question = soup_transtype.findAll('div', {'class': "w_cx"})
    select = question[0].contents[1]
    data_list = []
    for d in select.findAll('option'):
        str_id = d['value']
        str_name = d.string
        # print str_id + ' - ' + str_name
        row_list = []
        row_list.append(str_id)
        row_list.append(str_name)
        data_list.append(row_list)
    return data_list

def getCity():
    soup_City = getHtml(url_transport)
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

def getPageCount(soup_query):
    question = soup_query.findAll('div', {'class': "w_page"})
    # print question
    select = question[0].contents[3]
    select = select.string
    # print select
    begin = select.index('/')+1
    # print begin
    end = len(select)-3
    # print end
    page_count = select[begin:end]
    page_count = int(page_count)
    # print page_count
    return page_count

def getsoup_by_query(transtype, city_from, city_to, pagenum):
    url='http://index.0256.cn/request_report_for_pub_price.action'
    value={
        'orgId':'',
        'type':'-1',
        'marketId':'1',
        'cateId':transtype,
        'startLine':city_from,
        'endLine':city_to,
        'startTime	':'',
        'pageNumber':pagenum,
        'endTime':''
    }
    data=urllib.urlencode(value)
    req=urllib2.Request(url,data)
    response=urllib2.urlopen(req)
    the_page=response.read()
    soup = BeautifulSoup(the_page, 'html.parser')
    return soup

def getdata_from_soup(soup):
    data_list = []
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            foundAllTd = tr.findAll("td");
            # print foundAllTd
            if(foundAllTd):
                transtype = foundAllTd[0].string;
                way = foundAllTd[1].string;
                price = foundAllTd[2].string;
                compare = str(foundAllTd[3]);
                date = foundAllTd[4].string;
                compare = compare.replace('<div style="width: 75px;height: 40px;margin: 0 auto;border: none;"><img src="images3/arrow_down.png" style="height:13px; "/><span style="float: right;">','').replace('<div style="width: 75px;height: 40px;margin: 0 auto;border: none;"><img src="images3/arrow_up.png" style="height:13px; margin-left: 3px;"/><span style="float: right;">','').replace('</span></div>','').replace('<td>','').replace('</td>','').replace(' ','')
                row_list = []
                row_list.append(transtype)
                row_list.append(way)
                row_list.append(price)
                row_list.append(compare)
                row_list.append(date)
                data_list.append(row_list)
    # print_list1(data_list)
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
