import datetime
import pandas as pd
import requests

from utils import ExcelUtils, JdbcUtils

'''
尝试连接dbquery查询数据
'''


# 登录系统
def login(session, loginAddr, payload):
    print("登录开始...")
    # 登录头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Host': 'ssa.jd.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://ssa.jd.com/sso/login?ReturnUrl=http://dbsv4.jd.com/login',
        'Connection': 'keep-alive'
    }
    # 登录
    session.post(loginAddr, data=payload, headers=headers, allow_redirects=False)
    print("用户:{}登录成功...".format(payload.get('username')))
    return session


# 根据连接和信息获取数据
def getJsonData(connectSession, data):
    print("获取数据开始...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Host': 'dbquery.jd.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://dbsv4.jd.com/dbquery/queryData'
    }

    postUrl = 'http://dbsv4.jd.com/dbquery/queryData'
    try:
        resData = connectSession.post(postUrl, headers=headers, data=data, allow_redirects=False)
        # type(resData.json()['data']) --- <class 'dict'>
        my_datas = resData.json()['data']['dataList']['1']
        print("查询数据成功,my_datas:{}".format(my_datas))

    except Exception as e:
        print("查询数据失败!", e)
    return my_datas;


connectSession = requests.Session()
print("创建session文件...")
payload = {'username': 'guoqingyun',
           'password': 'Gqy$1993%0605'}
# 登录
loginAddr = "https://ssa.jd.com/sso/login?ReturnUrl=http://dbsv4.jd.com/login"
connectSession = login(connectSession, loginAddr, payload)
# 根据配置文件生成报表
data = {'dbName': 'lbs_master',
        'domain': 'my16115sa.mysql.jddb.com',
        'sql': 'select  dept_no,source_org_no from   warehouse_move_plan where dept_no=\'EBU4418046517236\''}

my_data = getJsonData(connectSession, data)


def buildDataList(my_data,ls=[]):
    df = pd.DataFrame(my_data).fillna('')
    ls = df.values.tolist()
    ls.insert(0, df.columns.tolist())
    return ls


datas = buildDataList(my_data)
filelds = datas[0]
my_file_name = '查询搬仓计划_' + datetime.date.today().strftime('%Y-%m-%d') + '.xlsx'
# 生成文件
ExcelUtils.get_excel(datas[1:], filelds, 'E:/toolsResult/' + my_file_name)
print('文件{}创建成功'.format(my_file_name))
