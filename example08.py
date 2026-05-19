'''
本程序为木子编程系列课第八课示例程序
主要引导大家学习：
        CSV文件读写
进一步深入编程世界
'''
import time

#自定义函数
  
'''
睡眠打印字符串方法
msg_str        需要打印输出的字符串
stepTime       输出间隔时间
'''
def print_sleep(msg_str,stepTime):
    time.sleep(stepTime)
    print(msg_str)
    return True
    
'''
展示列表信息方法
msgList        需要打印输出的列表
stepTime    输出间隔时间
'''
def showMsg_list(msgList,stepTime):
    for msg in msgList:
        time.sleep(stepTime)
        print(msg)
    return True

'''
做小测试的方法
question        需要回答的问题
answer          问题的答案
award           答对问题的奖励
'''
def test(question,answer,award):
    print()
    print_sleep('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^',2)
    test1_1 = input(question)
    while test1_1 != answer:
        print('很遗憾，回答错误！请结合前面的内容仔细观察或呼叫公主殿下！')
        test1_1 = input(question)
    print('回答正确!',award)
    print()
    return True

msg_data = '''
        算术运算：
\t除:/（有小数）\t取整：//（商的整数部分）\t取模：%（取除法竖式运算的余数部分）\t求幂：**（10**3，结果为：1000，10的3次方）',
        关系运算：判断关系运算符两边数据的关系，运算结果为：True或False。',
        逻辑运算：not、and、or；运算结果为：True或False。',
        赋值运算：（=），符号右侧创建值对象后，将左边的变量与右边的值进行绑定。',
        运算优先级：算术运算>关系运算>逻辑运算>赋值运算。
'''

msg_while1 = '''
----------------  不停判断，不停循环  --------------
while 循环条件：
        循环内容
'''

msg_for1 = '''----------------  依次访问序列中的数据  ----------------
for 循环控制变量 in 序列:
        循环内容
'''

msg_range = '''
~~~~~~~~~~~~~~~~~~~~    整数序列  range    ~~~~~~~~~~~~~~~~~~~~
range(start,stop,step) ,
从 start 开始，到小于 stop的最大整数结束，间隔为step。step省略值为1。
'''
msg_list = '''
~~~~~~~~~~~~~~~~~~~~    列表 list    ~~~~~~~~~~~~~~~~~~~~
使用一对英文的中括号[  ]，将多个数据围起来
使用英文的逗号，将这多个数据分开
使用下标的方式查找列表数据：list[下标]
有序、可修改、可重复
'''
msg_dict = '''
~~~~~~~~~~~~~~~~~~~~    字典 dict   ~~~~~~~~~~~~~~~~~~~~
使用一对英文的大括号{  }，将多个键值对数据围起来。键值对  写作     键（key） : 值（value）
使用英文的逗号，将这多个键值对分开
无序、键唯一
value = dict[key] #查找key对应的值
'''
msg_f = '''
~~~~~~~~~~~~~~~~~~~~    自定义函数   ~~~~~~~~~~~~~~~~~~~~
    关键字：def
    函数名：与函数功能相关
    参  数：写在函数名后的括号里，多个参数使用英文逗号分开
    返回值：return 函数运行后的结果
    在使用（调用）前定义函数
'''

msg_try = '''
#~~~~~~~~~~~~~~ 处理异常的格式 ~~~~~~~~~~~~~~
try:
    #尝试执行可能出现异常的代码
except 异常类型:
    #异常出现时执行的代码
else:
    #异常未出现时执行的代码
'''

#前六小节：复习内容引导词
print('勇士，欢迎回到程序世界！')

guide = ['恭喜你来到  第八关  ',
         '在之前的闯关任务中，你已获得：',
         '**********************    超大刀  六  项技能    **********************',
         '分别是：',
         '~~~~~~   注释——不运行的内容  ~~~~~~~~~~~~~~~~~~~~~',
         '~~~~~~  连接程序世界技能1  输入、输出函数：input()、print()',
         '~~~~~~  数据类型   整数类型 int、浮点数类型 float 、布尔类型 bool 、字符串类型 str ',
         '~~~~~~  变量通过“=”与数据进行绑定，变量名由字母、数字、下划线_组成，不能以数字开头，不能跟int、float等关键字重名',
         '~~~~~~  类型转换函数int()、float()、str()',
         '~~~~~~   数据运算  ~~~~~~~~~~~~~~~~~~~~',
         msg_data,
         '',
         '**********************    法杖   三   项魔法技能    **********************',
         '分别是：',
         '~~~~~~~~~~~~~~~~~~~~    管理支线任务的交警 if    ~~~~~~~~~~~~~~~~~~~~',
         '\t单分支：if、\t双分支：if-else、\t三分支：if-elif-else',
         '~~~~~~~~~~~~~~~~~~~~    条件循环守卫 while    ~~~~~~~~~~~~~~~~~~~~',
         msg_while1,
         '判断条件，满足则执行循环内容，内容执行后，再判断条件，',
         '不满足条件退出循环',
         '',
         '~~~~~~~~~~~~~~~~~~~~    序列循环鸡排哥 for    ~~~~~~~~~~~~~~~~~~~~',
         msg_for1,
         '每次循环，循环控制变量依次绑定序列中的内容',
         '',
         '**********************  链蛇软剑  三项技能  **********************',
         msg_range,
         msg_list,
         msg_dict,
         '**********************  炼器炉  **********************',
         msg_f,
         '**********************  拂尘  **********************',
         msg_try]

#从引导词列表中逐句打印引导词
showMsg_list(guide,1)
time.sleep(2)

for i in range(5):
    time.sleep(0.5)
    print('咻~~~~~~',end='')
print()
print()

print_sleep('**********************  解锁新道具：葫芦  **********************',2)
input('勇士！你可以直接按下Enter键开启第八关任务，修炼新道具了。')

#模拟加载画面
for i in range(50):
    time.sleep(0.1)
    print('*',end='')
print()

#语法讲解

#引入
gramList_intro = [
    '勇士！修炼到这里，你已经能读懂上百行的程序了！',
    '且这些程序可以实现的功能也越来越多，',
    '可处理的数据也越来越多。',
    '这些数据在程序运行时，保存在变量当中。',
    '而程序运行结束后，变量当中保存的数据将全部清空。',
    '\n如果希望程序结束后，重要数据仍保持，则需要将数据保存到文件中。',
    '比如游戏玩家ID、游戏进度、游戏胜负的数据等都需要保存到文件中。',
    '这样程序再次启动时，可直接读取文件中的数据。'
    ]
showMsg_list(gramList_intro,2.5)
test('程序运行结束后，变量中存储的数据是否还在(yes/no)？','no','葫芦装载值+1')

gramList_csv = [
    '勇士，在新手阶段，我们从简单的纯文本文件的读写开始',
    '\n~~~~~~~~~~~~~~~~~~~~  CSV文件  ~~~~~~~~~~~~~~~~~~~~',
    'CSV（Comma-Separated Values）文件：英文逗号分隔值的纯文本文件',
    '\n----------------  CSV文件核心规则  ----------------',
    '不同列数据，用英文逗号隔开',
    '不同行数据，用换行隔开',
    '没有字体、颜色、格式，只存纯数据',
    '\n----------------  CSV 格式预览 ----------------\n姓名,排名,兵器,封号\n宋江,1,锟铻剑,呼保义\n卢俊义,2,麒麟黄金枪,玉麒麟\n吴用,3,七星坛羽扇,智多星\n',
    ]
showMsg_list(gramList_csv,2.5)
test('使用英文逗号分隔值的纯文本文件，是什么类型的文件(大写字母)？','CSV','葫芦装载值+1')

gramList_csvOpen = [
    '勇士，CSV文件材料有了。',
    '接下来，你将轻松get在程序中读写文件的技能。',
    '第一步，我们需要使用open()函数打开文件',
    'open(file,mode,encoding......)',
    'open()函数参数列表：\n1.file\t\t文件路径/文件名称\n2.mode\t\t文件打开模式：\n\t"r"读取模式、"w"覆盖写入模式、"a"在文件末尾追加写入模式\n3.encoding\t编码方式:目前使用utf-8-sig格式，该格式可以使用excel或记事本打开CSV文件',
    ]
showMsg_list(gramList_csvOpen,2.5)
test('在程序中，如果需要在某个CSV文件的末尾添加数据，那么在打开该文件时，使用什么模式打开呢？','a','葫芦装载值+1')

gramList_csvVar = [
    '第二步，使用with ...  as ... 关键字将打开的文件保存在文件对象中，',
    'with open() as 文件对象:',
    '例：\nwith open("heros.csv", "r", encoding="utf-8-sig") as csvFile:'
    ]
showMsg_list(gramList_csvVar,2.5)
test('在上一行程序中，打开的是哪一个文件呢？','heros.csv','葫芦装载值+1')
test('在上一行程序中，打开的文件存放在程序的哪个文件对象中呢？','csvFile','葫芦装载值+1')

gramList_csvRead = [
    '第三步，导入csv模块，使用csv模块中的函数从文件对象中获取    读取对象    中。',
    '''
import csv    #导入CSV模块
with open("heros.csv", "r", encoding="utf-8-sig") as csvFile:    #使用读取模式打开heros.csv文件
    reader = csv.reader(csvFile)     #获取读取对象
    ''',
    '第四步，在程序中按行处理文件中的数据',
    '''
import csv    #导入CSV模块
with open("heros.csv", "r", encoding="utf-8-sig") as csvFile:    #使用读取模式打开heros.csv文件
    reader = csv.reader(csvFile)     #获取读取对象
    for row in reader:    #遍历读取对象，依次获取文件每一行的信息
        print(row)
    ''',    
    ]
showMsg_list(gramList_csvRead,2.5)
test('在读取文件的第四步中，使用什么循环结构遍历读取对象？','for','葫芦装载值+1')

gramList_csvWrite = [
    '以上是读取文件内容的四个步骤，',
    '写入文件同样也是四个步骤，'
    '第一步，使用open()函数打开文件'
    '\t不同的是，读取模式改为"w"或"a"',
    '第二步，使用with ...  as ... 关键字将打开的文件保存在文件对象中，'
    'with open("heros.csv", "a", encoding="utf-8-sig") as csvFile:'
    '第三步，导入csv模块，使用csv模块中的函数从文件对象中获取     写入对象    中。',
    '''
import csv    #导入CSV模块
with open("heros.csv", "a", encoding="utf-8-sig") as csvFile:    #使用  末尾追加写入模式  打开heros.csv文件
    writer = csv.writer(csvFile)     #获取写入对象
    ''',
    '第四步，将数据写入文件中。'
    '''
import csv    #导入CSV模块
with open("heros.csv", "a", encoding="utf-8-sig") as csvFile:    #使用  末尾追加写入模式  打开heros.csv文件
    writer = csv.writer(csvFile)     #获取写入对象
    writer.writerow(newHeroList)    #写入一行列表
    writer.writerows(newHerosList)    #写入多行列表
    '''
    ]
showMsg_list(gramList_csvWrite,2.5)
test('打开文件后的操作（读取/写入）需要在with模块下缩进(行前空4格)处理，yes/no ?','yes','葫芦装载值+1')

#知识点分割
print_sleep('********************************************************************',2)
print_sleep('恭喜！葫芦装载值已加满！',1)
print_sleep('接下来，你可以选择向公主殿下提问，或完成exercise08，再完成task08！',1)
