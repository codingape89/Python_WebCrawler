# coding=utf-8
from bs4 import BeautifulSoup

import helper
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

# define result url
mainurl = "http://index.0256.cn/expx.htm"

# define query request url
requesturl = "http://index.0256.cn/expcenter_trend.action"

all_data_result = []

# define query paramaters
marketId = "1"
list_attribute1 = [["1","运输路线指数"]
    , ["2", "节点城市指数"]
    , ["3", "物流区域指数"]
    , ["4", "大类指数"]
    , ["5", "运价总指数"] ]
list_exponentTypeId = [["2", "周指数"]
    , ["3", "月指数"]
    , ["4", "季度指数"]
    , ["5", "年度指数"] ]
list_cateId = [["2", "整车运输"]
    , ["3", "零担重货"]
    , ["4", "零担轻货"] ]
list_attribute2 = helper.getattribute2(mainurl)
list_city = helper.getCity(mainurl)
list_startLine = helper.getCity(mainurl)
list_endLine = helper.getCity(mainurl)

attribute1 = ""
exponentTypeId = ""
cateId = ""
attribute2 = ""
city = ""
startLine = ""
endLine = ""

# reset function
def resetParas():
    global attribute1, exponentTypeId, cateId, attribute2, city, startLine, endLine
    attribute1 = ""
    exponentTypeId = ""
    cateId = ""
    attribute2 = ""
    city = ""
    startLine = ""
    endLine = ""

def resetResultList():
    global all_data_result
    all_data_result = [["marketId(all for 1)"
                           , "attribute1(5-运价总指数 | 4-大类指数 | 3-物流区域指数 | 2-节点城市指数 | 1-运输路线指数)"
                           , "exponentTypeId(2-周指数 | 3-月指数 | 4-季度指数 | 5-年度指数)"
                           , "cateId(2-整车运输 | 3-零担重货 | 4-零担轻货)"
                           , "attribute2"
                           , "city"
                           , "startLine"
                           , "endLine"
                           , "指数", "环比", "统计时间", "统计周期", "发布时间"]]

# reset function
def initParas():
    global marketId, attribute1, exponentTypeId, cateId, attribute2, city, startLine, endLine
    list = [["marketId", marketId]
        , ["attribute1", attribute1]
        , ["exponentTypeId", exponentTypeId]
        , ["cateId", cateId]
        , ["attribute2", attribute2]
        , ["city", city]
        , ["startLine", startLine]
        , ["endLine", endLine]]
    return list

resetResultList()

# query main type 1
resetParas()
one_attribute1 = list_attribute1[4]
print "开始处理： 大类=" + one_attribute1[0] + ' - ' + one_attribute1[1]
attribute1 = one_attribute1[0]
for one_exponentTypeId in list_exponentTypeId:
    print "----------" + one_exponentTypeId[0] + ' - ' + one_exponentTypeId[1]
    exponentTypeId = one_exponentTypeId[0]
    paralist = initParas()
    page = helper.getsoup_by_query2(str(requesturl), paralist )
    # print page
    this_data = helper.getdata_from_soup(page, paralist)
    helper.add_list(all_data_result, this_data)
helper.write_excel2007('print/5-total.xlsx', all_data_result)
resetResultList()

# query main type 2
resetParas()
one_attribute1 = list_attribute1[3]
print "开始处理： 大类=" + one_attribute1[0] + ' - ' + one_attribute1[1]
attribute1 = one_attribute1[0]
for one_exponentTypeId in list_exponentTypeId:
    for one_cateId in list_cateId:
        print "----------" + one_exponentTypeId[0] + ' - ' + one_exponentTypeId[1] + " | " + one_cateId[0] + ' - ' + one_cateId[1]
        exponentTypeId = one_exponentTypeId[0]
        cateId = one_cateId[0]
        paralist = initParas()
        page = helper.getsoup_by_query2(str(requesturl), paralist )
        # print page
        this_data = helper.getdata_from_soup(page, paralist)
        helper.add_list(all_data_result, this_data)
helper.write_excel2007('print/4-transtype.xlsx', all_data_result)
resetResultList()

# query main type 3
resetParas()
one_attribute1 = list_attribute1[2]
print "开始处理： 大类=" + one_attribute1[0] + ' - ' + one_attribute1[1]
attribute1 = one_attribute1[0]
for one_exponentTypeId in list_exponentTypeId:
    for one_attribute2 in list_attribute2:
        print "----------" + one_exponentTypeId[0] + ' - ' + one_exponentTypeId[1] + " | " + one_attribute2
        exponentTypeId = one_exponentTypeId[0]
        attribute2 = one_attribute2
        paralist = initParas()
        page = helper.getsoup_by_query2(str(requesturl), paralist )
        # print page
        this_data = helper.getdata_from_soup(page, paralist)
        helper.add_list(all_data_result, this_data)
helper.write_excel2007('print/3-attribution.xlsx', all_data_result)
resetResultList()

# query main type 4
resetParas()
one_attribute1 = list_attribute1[1]
print "开始处理： 大类=" + one_attribute1[0] + ' - ' + one_attribute1[1]
attribute1 = one_attribute1[0]
for one_exponentTypeId in list_exponentTypeId:
    for one_city in list_city:
        print "----------" + one_exponentTypeId[0] + ' - ' + one_exponentTypeId[1] + " | " + one_city
        exponentTypeId = one_exponentTypeId[0]
        city = one_city
        paralist = initParas()
        page = helper.getsoup_by_query2(str(requesturl), paralist )
        # print page
        this_data = helper.getdata_from_soup(page, paralist)
        helper.add_list(all_data_result, this_data)
helper.write_excel2007('print/2-city.xlsx', all_data_result)
resetResultList()

# query main type 5
resetParas()
one_attribute1 = list_attribute1[0]
counter = 1
print "开始处理： 大类=" + one_attribute1[0] + ' - ' + one_attribute1[1]
attribute1 = one_attribute1[0]
for one_exponentTypeId in list_exponentTypeId:
    for one_startLine in list_startLine:
        for one_endLine in list_endLine:
            print "----------" + one_exponentTypeId[0] + ' - ' + one_exponentTypeId[1] + " | " + one_startLine + ' - ' + one_endLine
            exponentTypeId = one_exponentTypeId[0]
            startLine = one_startLine
            endLine = one_endLine
            paralist = initParas()
            page = helper.getsoup_by_query2(str(requesturl), paralist )
            # print page
            this_data = helper.getdata_from_soup(page, paralist)
            helper.add_list(all_data_result, this_data)
        if len(all_data_result) >= 10000:
            print '--------begin to make excel--------'
            helper.write_excel2007('print/1-city_to_city_"+counter+".xlsx', all_data_result)
            resetResultList()
            counter += 1
