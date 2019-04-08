# encoding=utf-8



'''
(1)
<_io.TextIOWrapper name='E:\pyFileDemo\myPyFile.txt' mode='r' encoding='cp936'>    : 输出显示该myfile变量是myfile.txt文件的容器，并以只读模式打开文件
一旦调用该read方法，光标就会移动到文本的末尾。因此，当你再次调用read时，不会显示任何内容，因为已经没有更多要打印的文本了,调用seek()方法并使用0作为参数。
这会将光标移回文本文件的开头
'''
#file.seek(0)
#print(file.read())
#print('================')

'''
我们也可以逐行读取文件内容，而不是一次读取文件的所有内容。为此，我们需要执行readlines()方法，该方法可以将文本文件中的每一行作为列表项返回。
'''
# file.seek(0)
# print(file.readlines())
# print('================')

'''
在多数情况下，这会使文本更容易相处。例如，我们现在可以轻松遍历每一行并打印行中的第一个单词。
'''

'''
执行readline()方法,每次读取一行
'''
# file.seek(0)
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print('================')


#打开文件
#file=open("E:\pyFileDemo\myPyFile.txt")
#print(file.read())

##读取文件
#print(file.read())
#print('================')

# file.seek(0)
# for line in file:
#     print(line.split()[0])#获取首行单词
# print('================')

'''
要写入文本文件，只需在打开文件时将打开模式设置为w或w+,该方法会清空原本文件
a+模式打开文件，该模式能够添加和读取文件内容
'''
#file=open("E:\pyFileDemo\myPyFile2.txt","w+")

file=open("E:\pyFileDemo\myPyFile2.txt","a+")
file.write("\nThis is myPyFile2")
file.seek(0)
print(file.read())
print('================')

#关闭文件
'''
最后，在继续下一节之前，让我们看看在执行所需操作后如何使用上下文管理器自动关闭文件。
使用with关键字，如上所示，你不需要明确关闭文件。相反，上面的脚本打开文件，读取内容，然后自动关闭它。
'''
with open("E:\pyFileDemo\myPyFile2.txt") as myfile:
    print(myfile.read())