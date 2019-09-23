import unittest
from tools.http_requests import HttpResuest
from tools.do_excel import DoExcle
from tools.get_path import *
from tools.do_mysql import DoMysql
from tools.login_getCookies import login
from tools.get_data import GetData
from tools.my_log import MyLog
from ddt import ddt,data
import json
cookies,headers=login()
test_data=DoExcle(test_data_path).get_data()
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)
    def test_usedCar_collection(self,item):
        print("用例名称：{}".format(item["title"]))
        # print("car_id:{}".format(getattr(GetData,'car_id')))
        if item['url'].find('#{car_id}')!=-1:
            '''从反射里拿到car_id替换${car_id}'''
            item['url']=item['url'].replace('#{car_id}',getattr(GetData,'car_id'))
        if item['url'].find('#{car_info_id}')!=-1:
            '''从反射里拿到{car_info_id}替换#{car_info_id}'''
            item['url']=item['url'].replace('#{car_info_id}',getattr(GetData,'car_info_id'))
        if item['data'].find('${car_num}')!=-1:
            '''从反射里拿到车牌号替换${car_num}'''
            item['data']=item['data'].replace('${car_num}',getattr(GetData,'car_num'))
        else:
            pass
        if item['data'].find('${car_num}')!=-1:
            '''从反射拿到生成的car_num，替换${car_num}'''
            item['data'] = item['data'].replace('${car_num}', str(getattr(GetData, 'car_num')))
        else:
            pass
        #对参数中的的嵌套字典进行处理
        d = eval(item["data"])
        if "inspection" in d.keys():
            d["inspection"] = json.dumps(d["inspection"])
        elif "info" in d.keys():
            d["info"] = json.dumps(d["info"])
        print("url:{}".format(item['url']))
        MyLog().info("请求的参数是：{0}".format(d))
        res = HttpResuest.http_request(url=item['url'], data=d, method=item['method'], headers=headers,
                                       cookies=cookies)
        r = json.loads(res.text)  # 将response格式转化为python字典格式
        print("code:{}".format(r["code"]),     "message:{}".format(r["message"]))
        if item['title']=='新建线索':
            '''将新建线索生成的车辆id保存，用于下一个接口查询car_id'''
            car_id=r["data"]["id"]
            setattr(GetData,'car_id',str(car_id))
            # MyLog().info('存储car_id为{0}'.format(car_id))
            print('存储car_id为{0}'.format(car_id))
        elif item['title']=='获取car_info_id':
            '''将新建线索生成的车辆的car_info_id获取到并储存起来，用于后续接口'''
            car_info_id=r["data"]["car_info_id"]
            setattr(GetData,'car_info_id',str(car_info_id))
            #MyLog().info('存储car_id为{0}'.format(car_id))
            print('存储car_info_id为{0}'.format(car_info_id))
        try:
            self.assertEqual(str(r["code"]),str(item['excepted']))
            test_result='pass'
        except AssertionError as e:
            test_result='fail'
            MyLog().error("执行用例出错：{0}".format(e))
            print(e)
            raise
        finally:
            '''结果写回excel'''
            DoExcle(test_data_path).write_back(item['sheetname'],int(item['case_id'])+1,8,str(r))
            DoExcle(test_data_path).write_back(item['sheetname'],int(item['case_id'])+1,9,test_result)
            MyLog().error("获取到的结果是：{0}".format(res))











