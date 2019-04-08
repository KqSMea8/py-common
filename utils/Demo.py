# encoding=utf-8
from utils import JdbcUtils, ExcelUtils, EmailUtils, MyEmail as mail,DateUtils


def main():
    mysql = "SELECT exp_no '标准单号',exp_date '计费日期',seller_no  '商家编号',  system_source '来源系统',order_type '单据类型',transaction_type '交易类型' FROM  trans_standard_201807 ;"
    # 生成数据
    my_data = JdbcUtils.get_datas(mysql)
    # 生成字段名称
    my_fields = JdbcUtils.get_fields(mysql)
    yesterdayStr = DateUtils.getYesterdayStr()
    # 生成文件名称
    my_file_name = 'file_' + yesterdayStr + '.xlsx'
    # 生成文件路径
    my_file_path = 'E:/toolsResult/' + my_file_name
    # 生成excel
    ExcelUtils.get_excel(my_data, my_fields, my_file_path)

    my_email = mail.MyEmail(emailFrom='gqy1084@126.com', emailTo='1093253239@qq.com',
                            emailSubject='【标准单数据】' + yesterdayStr,
                            emailText='Dear all：\n\t附件为昨天的标准单数据，请查收！',
                            annexPath=my_file_path, annexName=my_file_name)

    # 生成邮件
    my_email_msg = EmailUtils.create_email(my_email)
    my_receiver = ['1093253239@qq.com']
    EmailUtils.send_email('gqy1084@126.com', 'Gqy1084', my_receiver, my_email_msg)


if __name__ == "__main__":
    try:
        main()
        print("运行成功:")
    except Exception as e:
        print("运行失败:", e)
