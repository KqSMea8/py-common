'''
 spaCy
 (1)安装
spaCy库与NLTK都是最流行的NLP库之一。这两个库的基本区别在于，NLTK包含多种算法来解决一个问题，而spaCy只包含一种算法，但它是解决问题的最佳算法。
pip安装命令: pip install -U spacy

下载并安装spaCy之后，下一步是下载语言模块。我们将使用英语语言模块。语言模块用于执行各种NLP任务，我们将在后面的内容中看到。
pip命令： python -m spacy download en

(2)基本功能
当使用该模块创建文档时，SpaCy会自动将文档分解为一系列标记。
标记是指句子中具有某种语义价值的单个部分。我们来看看我们的文档中都有哪些标记:
.pos_  : 标记的词性 ,你可以看到，我们句子中的每个单词或标记都被指定了一个词性。例如，“Manchester”被标记为专有名词，“Looking”被标记为动词，等等
dep_   : 依赖项解析 ,例如在我们的句子中有一个单词isn’t。依赖项解析器将其分解为两个单词，并说明n"t实际上是对前一个单词的否定。
 []    : 你还可以检查一个句子是否以特定标记开头。你可以使用索引和方括号(类似于数组)获取单个标记:(索引是从零开始，句点作为标记)
is_sent_start : 要查看文档中是否有以The开头的句子，我们可以使用is_sent_start属性

(3)标记化
标记化是将文档分解为单词、标点符号、数字等的过程。
(4)检测实体

'''
import spacy

'''
载入spaCy语言模块
创建一个简单的spaCy文档
'''

sp = spacy.load('en_core_web_sm')
# sentence = sp(u'Manchester United is looking to sign a forward for $90 million')
# sentence = sp(u"Manchester United isn't looking to sign any forward")
#
# for world in sentence:
#     #打印单词，词性，依赖项
#     print(world.text, world.pos_, world.dep_)

# 打印句子
document = sp(u"lily,Manchester United isn't looking to sign any forward.Isn't it? let's go!")
for sen in document.sents:
    print(sen.text + "-" + sen.label_ + "-" + str(spacy.explain(sen.label_)) + "-" + str(len(sen)))
print("============")

# #获取单个标记
# print(document[2])
# #查看文档中是否有以该标记开头的句子
# print(document[2].is_sent_start)
# #文件标记的数量
# print(len(document))
