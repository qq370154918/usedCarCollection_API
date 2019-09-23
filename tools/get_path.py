import os
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)

test_data_path=os.path.join(project_path,'test_data','test_data.xlsx')
config_path=os.path.join(project_path,'config','test.config')
test_report_path=os.path.join(project_path,'test_result','report.html')
logs_path=os.path.join(project_path,'test_result','log.txt')