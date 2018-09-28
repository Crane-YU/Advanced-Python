# Web Spider
- Web connector sends request, and the web will respond to the web connector
- The first step to the information of the web is `GET`
    - To prepare, install python modules
        
            pip3 install requests
            pip3 install BeautifulSoup4
            
    - `Request`
        - URL request module
        - `POST`, `PUT`, `GET`, `DELETE`
        
# urllib
- 包含模块
    - urllib.request: 打开和读取urls
    - urllib.error: 使用try捕捉
    - urllib.parse: 包含解析url方法
    - urllib.robotparse: 解析robots.txt文件
    - EXAMPLE1
    
- urlopen返回对象
    - 处理返回异常的状况
    - urlopen里面不能使用data，功能受限制

- request.data的使用
    - get:
        - 利用参数给服务器传递信息
        - 参数为字典形式，然后用parse编码
        
    - post:
        - 一般向服务器传递参数
        - 把信息自动加密处理
        - 我们如果想使用post参数，需要用data参数
        - 使用post，一位置http的请求头需要更改
            - Content-Type: application/x-www/form.urlencode
            - Content-Length: 数据长度
            - 简而言之，一旦请求更改方法，其他请求头部信息也要改变
        - 　　urllib.parse.urlencode可以自动将字符串转化为上面的值
        - example3
        
    - 为了更多的设置请求信息，单纯的urlopen函数已经不能满足了，需要利用request.Request
    
- request.Request
    - example4
    - 可以在header里面加东西来隐藏身份
    
- urllib.error
    - URL error 产生原因：
        - no internet access
        - 服务器失效，找不到指定服务器
        - OS error的子类
        - example7
    - HTTP error (subset of urlerror):
        - example8
        
- userAgent(python伪装为浏览器)
    - 属于headers的一部分，服务器通过UA来判断访问者的身份
    - 常用的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    
- 设置UA可以通过两种方式：
    - headers
    - add_header
    - example9
    
- ProxyHandler处理（代理服务器）
    - 使用代理IP，是爬虫的常用手段
    - 如何寻找一个代理服务器？
        - 获取地址：
            - www.xicidaili.com
            - www.goubanjia.com
        - 使用大量的代理服务器进行网页的访问，否则也会被认为是爬虫，从而代理被封掉
    - 如何使用代理
        - 设置代理地址
        - 创建ProxyHandler
        - 创建Opener
        - 安装Opener
    - example10
    
- cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发放给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息

    - cookie 和 session 的区别
        - 存放位置不同
        - cookie不安全
        - session会保存在服务器上一定时间，会过期
        - 单个cookie保存数据不超过4k， 很多浏览器限制一个站点最多保存20个

    - session的存放位置
        - 存放在服务器端
        - 一般情况，session放在数据库（默认）中或者内存里
        - 没有cookie登录 example11
        
    - 使用cookie登录
        - http模块包含一些cookie的模块，我们可以自动使用cookie
            - CookieJar
                - 管理储存cookie，向传出的http请求添加cookie
                - cookie存储在内存中
            - FileCookieJar(filename, delayload=None, policy=None)
                - 使用文件管理cookie
                - cookie保存在文件里
            - MozillaCookieJar(filename, delayload=None, policy=None)
            - LwpCookieJar
        - 利用CookieJar访问人人 example12
    
    - cookie的属性：
        - name
        - value
        - domain：可以访问此cookie的域名
        - path：可以访问此cookie的页面路径
        - expires：过期时间
        - size：大小
        - Http字段
        
- SSL
    - SSL证书是遵守SSL安全套阶层协议的服务器数字证书（SecureSocketLayer）

- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常取md5值）
    - 经过加密，传输的就是密文，但是加密的函数或者过程一定是在浏览器完成的，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就乐意模拟出加密过程，从而达到破解
    - 过程参看example13
    
- ajax
    - 异步请求
    - 一定会有url，请求方法，可能有数据
    - 一般使用json
    - 案例，example14(豆瓣电影)
    
# Requests
- HTTP for Humans
- 继承了urllib所有的特征
- 底层使用的是urllib3
- 中文档案： http://docs.python-requests.org/zh_CN/latest/index.html
- get请求
    - requests.get()
    - requests.request("get", url)
    - 可以带有参数headers和params
    - 案例, example15
- get返回内容
    - 案例, example16
    
- post
    - requests.post(url = url, data = data)
    - 参看案例, example17
    
- proxy
        
        proxies = {
        "http": "address of proxy"
        "https": "address of proxy"
        }
        
        rsp = requests.request("get", "hrrp://xxxxxxx", proxies=proxies)
        
    - 代理可能报错，如果使用人数多，考虑到安全问题，可能会被强行关闭

- 用户验证
    - 代理验证
    
            #可能需要使用HTTP basic Auth， 可以这样
            # 格式为  用户名:密码@代理地址：端口地址
            proxy = { "http": "china:123456@192.168.1.123：4444"}
            rsp = requests.get("http://baidu.com", proxies=proxy)
- web端用户验证
    - 如果遇到web客户端验证，需要添加auth=（用户名，密码）
    
            autu=("test1", "123456")#授权信息
            rsp = requests.get("http://www.baidu.com", auth=auth)   

- cookie
    - requests可以自动处理cookie信息
    
            rsp = requests.get("http://xxxxxx")
            # 如果对方服务器传回来一个cookie信息，则可以通过反馈的cookie属性得到
            # 返回一个cookiejar实例
            cookiejar = rsp.cookies
            
            # 可以将cookiejar转化为字典格式
            cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
 
- session
    - 和服务器上的session不是一个概念
    - 模拟一次对话，从客户端浏览器链接服务器开始，到客户端浏览器断开
    - 能让我们跨请求时保持某些参数，比如在同一个session实例发出的 所有请求之间保持cookie
    
            # 创建session对象，可以保持cookie值
            ss = requests.session()
            headers = {"User-Agetn":"xxxxxxxxxxxxxxxxxx"}  
            data = {"name":"xxxxxxxxxxx"}
              
            # 此时，由创建的session管理请求，负责发出请求，
            ss.post("http://www.baidu.com", data=data, headers=headers)  
            rsp = ss.get("xxxxxxxxxxxx")

- https请求验证ssl证书
    - 参数verify负责表示是否需要验证ssL证书，默认是True
     -如果不需要验证ssl证书，则设置成False表示关闭

            rsp = requests.get("https://www.baidu.com", verify=False)
            # 如果用verify=True访问12306，会报错，因为他证书有问题 
        
# 页面解析和数据处理
- 结构化数据：先有结构，再有数据
    - JSON文件
        - JSON Path
        - 转换成Python类型进行操作（json类）
    - XML文件
        - 转换成python类型（xmltodict）
        - XPath
        - CSS选择器
        - 正则
- 非结构化数据：先有数据，再有结构
    - 文本
    - 电话号码
    - 邮箱地址
        - 通常处理此类数据，使用正则表达式
    - Html文件
    - 正则
    - XPath
    - CSS选择器
      
# CSS选择器 BeautifulSoup4
- 几个常用提取信息工具的比较：
    - 正则: 很快，不好用，不许安装
    - beautifulsoup: 慢，使用简单，安装简单
    - lxml: 比较快，使用简单，安装一般
    - 案例18
- 四大对象
    - Tag
    - NavigableString
    - BeautifulSoup
    - Comment
- Tag
    - 对应html中的标签
    - 可以通过soup.tag_name
    - tag两个重要属性
        - name
        - attrs
    - 案例19
- NavigableString
    - 对应内容值
- BeautifulSoup
    - 表示的是一个文档的内容，大部分可以把他当做tag对象
    - 一般我们可以用soup来表示
- Comment  
    - 特殊类型的NavigableString对象
    - 对其输出，则内容不包括注释符号  