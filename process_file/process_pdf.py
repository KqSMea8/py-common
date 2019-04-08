# encoding=utf-8
'''
默认情况下，Python没有任何可用于读取或写入PDF文件的内置库,可以使用PyPDF2
在我们使用PyPDF2库之前，需要安装它。如果你使用pip安装程序，则可以使用以下命令安装PyPDF2库：
pip install PyPDF2
'''
import PyPDF2

'''
值得一提的是，在打开PDF文件时，必须将模式设置为“读取二进制”的rb模式，因为大多数PDF文件都是二进制格式。
打开文件后，我们需要调用PyPDF2库中的PdfFileReader()函数，如下所示：
现在使用pdf_document变量，我们可以执行各种读取功能。例如，要获取PDF文档中的总页数，我们可以使用以下numPages属性 
由于我们只有一页文档，在我们的PDF文档中，你将在结果中看到1。
最后，要从PDF文档中提取文本，首先需要使用getPage()函数获取PDF文档的页面。
接下来，你可以调用extractText()函数从特定页面中提取文本。
以下脚本从PDF的第一页中提取文本，然后将其打印在控制台上。
'''
# 打开pdf
# myPdf=open("E:\pyFileDemo\Lorem-Ipsum.pdf",mode='rb')
# 读取pdf
# pdf_document=PyPDF2.PdfFileReader(myPdf)
# pdf_document.numPages
# first_page=pdf_document.getPage(0)
# print(first_page.extractText())

'''
上面的脚本读取了我们PDF文档的第一页。现在，我们可以使用以下脚本将第一页中的内容写入新的PDF文档：
上面的脚本创建了一个可用于将内容写入PDF文件的对象。首先，我们将向这个对象添加一个页面，并将我们从另一个PDF中检索到的页面传递给它。
接下来，我们需要打开一个具有wb（写二进制）权限的新文件。打开具有此类权限的文件会创建一个新文件，如果文件不存在的话。
最后，我们需要在PDF编写对象上调用write()方法并将新创建的文件传递给它。
关闭mypdf和pdf_output_file文件，然后转到程序的工作目录。你应该在编辑器中看到一个新文件new_pdf_file.pdf。打开文件，你应该看到它包含来自原始PDF的第一页的内容。
让我们尝试阅读新创建的PDF文档的内容：
'''

# 打开pdf
myPdf2 = open("E:\pyFileDemo\Lorem-Ipsum2.pdf", mode='rb')

# 读取pdf
pdf_document = PyPDF2.PdfFileReader(myPdf2)
pdf_document.numPages
page_one = pdf_document.getPage(0)

# 写入pdf
pdf_document_writer = PyPDF2.PdfFileWriter()
pdf_document_writer.addPage(page_one)
pdf_outPut_file = open("Lorem-Ipsum-new.pdf", "wb")
pdf_document_writer.write(pdf_outPut_file)

# 读取新文件
pdf_document_read2 = PyPDF2.PdfFileReader(myPdf2)
pdf_document_read2.numPages
for i in range(pdf_document_read2.numPages):
    this_page = pdf_document_read2.getPage(i)
    print(this_page.extractText())
