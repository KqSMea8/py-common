# encoding=utf-8
import datetime


# 获取昨天的格式化日期
def getYesterdayStr():
    # 获取昨天日期的字符串格式的函数
    # 获取今天的日期
    today = datetime.date.today()
    # 获取一天的日期格式数据
    oneday = datetime.timedelta(days=1)
    # 昨天等于今天减去一天
    yesterday = today - oneday
    # 获取昨天日期的格式化字符串 %Y-%m-%d %H:%M:%S
    yesterdaystr = yesterday.strftime('%Y-%m-%d')
    # 返回昨天的字符串
    return yesterdaystr
