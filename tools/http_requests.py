# -*- coding:utf-8 -*-
import requests
import json

class HttpResuest():
    @staticmethod
    def http_request(url,data,method,cookies=None,headers=None):
        requests.packages.urllib3.disable_warnings()
        # headers = {"Content-Type": "application/json"}
        # data = json.dumps(data)
        if method=="get":
            try:
                r = requests.get(url=url,data=data,headers=headers,cookies=cookies,verify=False)
                response=r.text
                print("get请求结果为：{}".format(response))
                return r
            except BaseException as e:
                print("get请求错误，错误原因：{}".format(e))
        elif method=="post":
            try:
                r = requests.post(url=url, data=data,headers=headers,cookies=cookies,verify=False)
                response = r.text
                print("post请求结果为：{}".format(response))
                return r
            except BaseException as e:
                print("post请求错误，错误原因：{}".format(e))
        elif method=="put":
            try:
                r = requests.put(url=url, data=data, headers=headers,cookies=cookies, verify=False)
                response = r.text
                print("post请求结果为：{}".format(response))
                return r
            except BaseException as e:
                print("put请求错误，错误原因：{}".format(e))

if __name__ == '__main__':
    data=json.dumps({"username":"13800000000","password":"123456"})
    # data={"vin":"BAL2WTDM53UC1HFKX","car_model_id":"1261","car_model_name":"宝马 5系 2005款 3.0L 自动 530Li","mileage":"11111","color_id":"1","is_color_changed":"0","production_date":"2017-05-16","license_issued_on":"2019-08-16","transfer_count":"0","last_transfer_date":"","belonged_province":"广东省","belonged_province_code":"440000","belonged_city":"深圳市","belonged_city_code":"440300","located_province":"广东省","located_province_code":"440000","located_city":"深圳市","located_city_code":"440300","plate_number":"粤CUQAIN","is_refitted":"false","car_character":"1", "car_character_name":"私户","usage_character":"2","usage_character_name":"非营运","emission_standard":"100","emission_standard_name":"国一", "channel":"1","channel_name":"销售端潜客","color_name":"黑","info_has_changes":"true"}
    # headers={"Content-Type":"application/json; charset=UTF-8"}
    headers={'X-CSRF-Token': '1568651065##3b8bf9b22ae0aa0beaf98bbcb664544ddbe081f5'}
    cookies={'session': '74b78d36-277c-4687-a349-99d93e5d4377', 'csrf-token': '1568651065##3b8bf9b22ae0aa0beaf98bbcb664544ddbe081f5'}
    print(HttpResuest().http_request(url="https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/5862",data=data,headers=headers,cookies=cookies,method="post"))