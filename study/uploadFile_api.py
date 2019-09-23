# 有一个上传接口，地址如下：http://xx.xx.xx.xx//upload/stream
# 上传接口的参数如下所示 {"parentId":"","fileCategory":"personal","fileSize":179,"fileName":"summer_text_0920.txt","uoType":1}
import requests
upload_url='---'
header={"ct":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"}
files = {'file':open('D:\\test_data\\summer_test_data_05.txt','rb')}#此处是重点！我们操作文件上传的时候，把目标文件以open打开，然后存储到变量file里面存到一个字典里面
upload_data={"parentId":"","fileCategory":"personal","fileSize":179,"fileName":"summer_text_0920.txt","uoType":1}
upload_res=requests.post(upload_url,upload_data,files=files,headers=header)##此处是重点！我们操作文件上传的时候，接口请求参数直接存到upload_data变量里面，在请求的时候，直接作为数据传递过去
