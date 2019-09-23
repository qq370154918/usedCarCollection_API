import logging
from tools.get_path import *
class MyLog():
    def my_log(self,msg,level):
        my_logger=logging.getLogger('test_logs')  #创建一个日志收集器
        my_logger.setLevel('DEBUG')    #设定收集日志级别
        format=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')   #设置输出格式

        ch=logging.StreamHandler()  #创建console控制台输出渠道
        ch.setLevel('ERROR')  #设定输出日志级别
        ch.setFormatter(format)  #设定输出日志格式

        fh=logging.FileHandler(logs_path,encoding='utf-8')  #创建file类输出渠道
        fh.setLevel('DEBUG')  # 设定输出日志级别
        fh.setFormatter(format)  #设定输出日志格式

        my_logger.addHandler(ch)   #日志收集与输出对接
        my_logger.addHandler(fh)   #日志收集与输出对接

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        #关闭渠道，不然会重复输出
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')
