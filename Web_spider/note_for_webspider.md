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