from bs4 import BeautifulSoup
from urllib import request

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs自动转码
content = soup.prettify()
print(content)
print("=="*36)

print(soup.head)
print("=="*36)

print(soup.meta)
print("=="*36)

print(soup.link)
print("=="*36)

print(soup.link.name)
print("=="*36)

print(soup.link.attrs)
print("=="*36)

print(soup.link.attrs['type'])