'''
利用parse模版模拟post请求
分析百度词典
分析步骤：
1. 打开F12
2. 尝试输入单词girl，发现每输入一个字母后都有请求
3. 请求地址是 http://fanyi.baidu.com/sug
4. 利用network->all->headers 查看，发现formadata的值是 kw:girl
5. 检查返回内容的格式，发现返回的是json格式内容->需要用到json包
'''

from urllib import parse, request
import json

'''
大致流程：
1. 利用data构造内容，然后urlopen打开
2. 返回一个json格式的内容
3. 结果就应该是girl的释义
'''

base_url = 'http://fanyi.baidu.com/sug'

# 存放用来模拟form的数据一定是dict模式
data = {
    # girl是输入的需要翻译的内容，应该有用户输入，此处使用的是硬编码
    'kw': 'girl'
}

# 需要用parse模块对data进行编码
data = parse.urlencode(data).encode("utf-8")

# 构造一个header，请求头至少包含传入数据的长度
# REQUEST 要求传入的请求头是一个dict格式
header = {
    # 因为使用post，至少应该包含content-length
    'Content-Length': len(data)
}

# 有了header，data，url，就可以尝试发出请求了
# urlopen中无headers属性
rsp = request.urlopen(base_url, data=data)
json_data = rsp.read().decode()

# 解码之后json格式无法识别
print(json_data)
print(type(json_data))
print(json_data)

# 把json字符串转化为python字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], '--', item['v'])
    print("")
