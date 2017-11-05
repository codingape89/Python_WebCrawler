# coding=utf-8
import helper
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# get all transtype
data_transtype = helper.getTranstype()
print '*****************************************'
print '所有传输方式：'
helper.print_list2(data_transtype)
print
print

# get all city
data_city_from = helper.getCity()
data_city_to = helper.getCity()
print '*****************************************'
print '所有城市信息：'
helper.print_list0(data_city_from)
print
print
print

# query with all conditions
print '*****************************************'
all_data_result = []
counter = 1
page_count = 1
for one_transtype in data_transtype:
    transtype = one_transtype[0]
    for one_city_from in data_city_from:
        for one_city_to in data_city_to:
            print "开始处理组合： 传输方式=" + transtype + ' - CityFrom:' + one_city_from +  ' - CityTo:' + one_city_to
            if one_city_from=='北京' or one_city_to=='北京':
            # if 1==1:
                soup = helper.getsoup_by_query(str(transtype), str(one_city_from), str(one_city_to), '1')
                this_data = helper.getdata_from_soup(soup)
                print '--------当前第 1/'+str(page_count)+' 页--------'
                helper.print_list2(this_data)
                page_count = helper.getPageCount(soup)
                helper.add_list(all_data_result, this_data)
                for i in range(2, page_count):
                    soup = helper.getsoup_by_query(str(transtype), str(one_city_from), str(one_city_to), str(i))
                    this_data = helper.getdata_from_soup(soup)
                    print '--------当前第 '+str(i)+'/'+str(page_count)+' 页--------'
                    helper.print_list2(this_data)
                    helper.add_list(all_data_result, this_data)
                    if len(all_data_result)>=10000:
                        print '--------begin to make excel--------'
                        helper.write_excel2007('print/result_'+str(counter)+'.xlsx', all_data_result)
                        counter += 1
                        all_data_result = []
            else:
                print "--------不符合判断规则，跳过--------"

# print excel
if len(all_data_result)>0:
    helper.write_excel2007('print/result_'+str(counter)+'.xlsx', all_data_result)
