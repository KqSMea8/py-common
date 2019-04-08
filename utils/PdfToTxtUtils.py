# encoding =utf-8
import PyPDF2


def transPdfToTxt(source_file_path, tar_file_name):
    tar_txt_file = open(tar_file_name, 'a+')
    source_pdf_file = open(source_file_path, mode='rb')
    doc_read = PyPDF2.PdfFileReader(source_pdf_file)
    for i in range(doc_read.numPages):
        source_line = doc_read.getPage(i).extractText()
        msg = "数据为：" + source_line
        print(msg)
        tar_txt_file.write(source_line)

    return tar_txt_file


##创建txt文件
source_file_path = "E:\pyFileDemo\Lorem-Ipsum.pdf"
tar_file_name = "E:\pyFileDemo\myTxt.txt"
file = transPdfToTxt(source_file_path, tar_file_name)
print('文件{}创建成功'.format(tar_file_name))
