# encoding=utf-8
#  -*- coding:utf-8 -*-
#1.Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。使用coding=utf-8（=左右没有空格）或者-*- coding:utf-8 -*-
#2.Python 可以同一行显示多条语句，方法是用分号 ;
#3.Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行（否则会报IndentationError: unindent does not match any outer indentation level
# :表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。）
#4.Python语句中一般以新行作为语句的结束符。但是我们可以使用斜杠（ \）将一行的语句分为多行显示。
#5.Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
#6.python中单行注释采用 # 开头。python 中多行注释使用三个单引号(''')或三个双引号(""")。
#7.print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,

#1.Python 中的变量赋值不需要类型声明。每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#2.Python允许你同时为多个变量赋值,例如：a = b = c = 1(创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。)
#也可以为多个对象指定多个变量,例如：a, b, c = 1, 2, "john"
#3.使用del语句删除一些对象的引用。del语句的语法是：del var1[,var2[,var3[....,varN]]]]
#4.Python有五个标准的数据类型：Numbers（数字）String（字符串）List（列表）Tuple（元组）Dictionary（字典）
#5.Python支持四种不同的数字类型：int（有符号整型）long（长整型[也可以代表八进制和十六进制]）float（浮点型）complex（复数）
#6.字符串或串(String)是由数字、字母、下划线组成的一串字符。
#python的字串列表有2种取值顺序:  从左到右索引默认0开始的，最大范围是字符串长度少1
                                # 从右到左索引默认-1开始的，最大范围是字符串开头
                                #[头下标:尾下标] 获取的子字符串,含头不含尾
                                #[头下标:] 输出从第n个字符开始的字符串
                                #加号（+）是字符串连接运算符，星号（*）是重复操作
#7.List（列表） 是 Python 中使用最频繁的数据类型。列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。列表用 [] 标识，是 python 最通用的复合数据类型。
#list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tinylist = [123, 'john']
#print list               # 输出完整列表
#print list[0]            # 输出列表的第一个元素
#print list[1:3]          # 输出第二个至第三个元素
#print list[2:]           # 输出从第三个开始至列表末尾的所有元素
#print tinylist * 2       # 输出列表两次
#print list + tinylist    # 打印组合的列表
#8.Python元组 元组是另一个数据类型，类似于List（列表）。元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
#9.字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
#两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典用"{ }"标识。字典由索引(key)和它对应的值value组成。


#def hello(name):
#    str = "hello" + name;
#   return str;
#print(hello("刘阳"));

#if True:
#    print("a");
# print("d");

"""
if True:
    print("a");
"""

#raw_input("按下 enter 键退出，其他任意键显示...\n");

"""
print('a'),
print('b')
"""

#var =1L;
#print(var);
#del var;
#print(var)


#s="abcdef";
#print(s[-5:-1]);

#tinylist = [123, 'john']
#tinylist[0]='liuyang';
#print(tinylist);

#tinyTuple = (123, 'john');
#tinyTuple[0]='liuyang';
#print(tinyTuple);

#dict = {}
#dict['one'] = "This is one"
#dict[2] = "This is two"
#tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#print dict
#print tinydict             # 输出完整的字典
#print tinydict.keys()      # 输出所有键
#print tinydict.values()    # 输出所有值
#print tinydict['name']