from urllib import request

if __name__ == '__main__':
    url = "https://www.baidu.com/"
    # 打开相应的url，并把相应的页面作为返回
    rsp = request.urlopen(url)

    # 把返回的结果读取出来，读取结果为bytes
    html = rsp.read()

    # 解码bytes
    html = html.decode('utf-8')

    print(html)
