import requests

url = "http://www.baidu.com"

# 两种请求方法
rsp = requests.get(url=url)
print(rsp.text)

rsp = requests.request("get", url)
print(rsp.text)
