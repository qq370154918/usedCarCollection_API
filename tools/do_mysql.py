import pymysql
from tools.read_config import ReadConfig
from tools.get_path import *
db_config=eval(ReadConfig().read_config(config_path,'DATABASE','database'))

class DoMysql():
    def do_mysql(self,query_sql,status=1):
        cn=pymysql.connect(**db_config)
        cursor=cn.cursor()
        query=query_sql
        cursor.execute(query)
        if status=='all':
            res=cursor.fetchall()[0]
        else:
            res=cursor.fetchone()[0]
        return res
        cursor.close()
        cn.close()

if __name__ == '__main__':
    mobile = 13163750276
    mobile = str(mobile)
    print(mobile[9:11])
    query = 'select * from sms_db_{0}.t_mvcode_info_{1}'.format(mobile[9:11], mobile[8])
    print(query)
    res=DoMysql().do_mysql(query,'all')
    print(res)

