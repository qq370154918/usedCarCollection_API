from tools.get_data import GetData
import re
class DoRegx():
    @staticmethod
    def do_regx(pattern,s):
        while re.search(pattern,s):
            key =re.search(pattern,s).group(0)
            #print(key)
            value = re.search(pattern, s).group(1)
            #print(value)
            #从GetData中，将正则表达式匹配到的关键字（就是正则表达式（）里的内容）的值拿出来，替换原字符串
            s=s.replace(key,str(getattr(GetData,value)))
        return s

if __name__ == '__main__':
    data=str({'case_id': 2, 'title': '评估车辆信息-基本信息', 'url': 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/car_info/${car_id}',
 'data': '{"vin":"9X04YLCU8PZ56R3ED","car_model_id":"1261","car_model_name":"宝马 5系 2005款 3.0L 自动 530Li","mileage":"11111","color_id":"1","is_color_changed":"0","production_date":"2017-05-16","license_issued_on":"2019-08-16","transfer_count":"0","last_transfer_date":"","belonged_province":"广东省","belonged_province_code":"440000","belonged_city":"深圳市","belonged_city_code":"440300","located_province":"广东省","located_province_code":"440000","located_city":"深圳市","located_city_code":"440300","plate_number":car_no,"is_refitted":"false","car_character":"1", "car_character_name":"私户","usage_character":"2","usage_character_name":"非营运","emission_standard":"100","emission_standard_name":"国一", "channel":"1","channel_name":"销售端潜客","color_name":"黑","info_has_changes":"true"}',
 'method': 'post', 'query': None, 'excepted': 0, 'sheetname': 'usedCar'})
    re=DoRegx.do_regx('\$\{(.*?)\}',data)
    print(re)
    print(type(re))

