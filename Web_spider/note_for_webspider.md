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
        
        
        
    