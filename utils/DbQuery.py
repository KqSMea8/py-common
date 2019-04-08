import requests
import xmltodict
import json

'''
连接dbquery查询数据
requests.get(‘https://github.com/timeline.json’) #GET请求
requests.post(“http://httpbin.org/post”) #POST请求
requests.put(“http://httpbin.org/put”) #PUT请求
requests.delete(“http://httpbin.org/delete”) #DELETE请求
requests.head(“http://httpbin.org/get”) #HEAD请求
requests.options(“http://httpbin.org/get”) #OPTIONS请求

r = requests.get(url='http://www.itwhy.org')    # 最基本的GET请求
print(r.status_code)    # 获取返回状态
r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
print(r.url)
print(r.text)   #打印解码后的返回数据

requests.get('http://www.dict.baidu.com/s', params={'wd': 'python'})    #GET参数实例
requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})    #POST参数实例

r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())
#定制Header
data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)

r.status_code #响应状态码
r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#*特殊方法*#
r.json() #Requests中内置的JSON解码器
r.raise_for_status() #失败请求(非200响应)抛出异常
'''


# 登录系统
def login(session, payload):
    print("登录开始...")
    # 登录头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Host': 'dbquery.jd.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://ssa.jd.com/sso/login?ReturnUrl=http://dbquery.jd.com/login',
        'Connection': 'keep-alive'
    }
    loginAddr = "http://dbquery.jd.com/home"
    # 登录
    session.post(loginAddr, data=payload, headers=headers, allow_redirects=False)
    print("用户:{}登录成功...".format(payload.get('username')))
    return session


# 根据连接和信息获取数据
def getJsonData(connectSession):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Host': 'dbquery.jd.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://dbquery.jd.com/home/addTab.php?id=23482'
    }
    postUrl = 'http://dbquery.jd.com/home/ajaxQueryData'
    data = {'id': '23482',
            'sql': 'select * from trans_standard_201807 where business_no=\'ECO114369215766497\' '}
    resData = connectSession.post(postUrl, headers=headers, data=data, allow_redirects=False)
    print("获取结果resData:{}".format(resData))
    return resData.text


connectSession = requests.Session()
print("创建session文件...")
payload = {'username': 'guoqingyun',
           'password': 'Gqy$1993%0605'}
# 登录
connectSession = login(connectSession, payload)

# 根据配置文件生成报表
data = getJsonData(connectSession)
print("获取结果data:{}".format(data))
