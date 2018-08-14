# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get('https://www.google.com.au/search?q=MySignals.initSensorUART()&oq=MySignals.initSensorUART()&aqs=chrome..69i57.429j0j7&sourceid=chrome&ie=UTF-8')
#
# html_sample = ' \
# <html> \
#  <body> \
#  <h1 id="title">Hello World</h1> \
#  <a href="#" class="link">This is link1</a> \
#  <a href="# link2" class="link">This is link2</a> \
#  </body> \
#  </html>'
#
# soup = BeautifulSoup(html_sample, 'html.parser')
# print(soup.text)

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.sina.com.cn/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.select('.Tit_08'):
    a = news.select('a')[0].text
    b = news.select('a')[0]['href']

    print(a, b)
