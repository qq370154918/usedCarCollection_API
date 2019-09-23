import configparser
#读取配置文件
class ReadConfig():
    def read_config(self,filename,section,option):
        cf=configparser.ConfigParser()
        cf.read(filename)
        return cf.get(section, option)
