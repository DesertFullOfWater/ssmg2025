'''
本程序为木子编程系列课第二课示例程序
主要引导大家学习：
1.基本数据
2.数据类型转换
3.变量的基本用法
帮助同学们对编程打下基础
'''
import time

'''
#第二小节：复习内容引导词
guide = ['勇士，欢迎回到程序世界！',
         '恭喜你完成新手村第一个任务',
         '你已获得注释技能与连接程序世界的技能',
         '这两个技能使用方法如下：',
         '注释技能1：使用一对三引号，对在三引号中间的内容进行注释',
         '注释技能2：使用“#”对该符号后面的单行内容进行注释',
         '注意：被注释的内容将不会被运行，',
         '            故注释的作用一般是对程序进行解释',
         '            暂不需要执行的代码也可使用注释将其屏蔽',
         '连接程序世界技能1：使用输入输出函数',
         '输入函数：input()，括号内为提示内容',
         '输出函数：print()，括号内为需要输出的内容',
         '接下来即将解锁新手训练营第二关：《数据与变量》']

#从引导词列表中逐句打印引导词
for guideStr in guide:
    time.sleep(2)
    print(guideStr)

#模拟加载画面
for i in range(50):
    time.sleep(0.1)
    print('*',end='')
time.sleep(0.1)
print()

input('请输入任意键，开启第二关')

print()
#知识讲解
graList = ['勇士！程序世界充满数据的交流',
           '这些繁杂的数据大致分为：基本数据类型、组合数据类型',
           '其中最常见的基本数据类型是：',
           '        整数类型int、浮点数类型float、布尔类型bool',
           '最常见的组合数据类型有：',
           '        字符串str、列表list、字典dict',
           '我们先从简单的开始。']
for graStr in graList:
    time.sleep(2)
    print(graStr)

for i in range(50):
    time.sleep(0.1)
    print('*',end='')
time.sleep(0.1)
print()

#介绍基本数据类型
graList = ['整数类型为又称int型，可表示数据：正/负整数、0。',
           '浮点数类型为又称float型，可表示数据：带小数的数。',
           '布尔类型为又称bool型，可表示数据：True/Flase。',
           '布尔类型的数据用于比较运算与逻辑运算，我们会在下一关详细了解。',
           '以上，我们来小试牛刀一下吧！'
           ]

for graStr in graList:
    time.sleep(2)
    print(graStr)

for i in range(50):
    time.sleep(0.1)
    print('*',end='')
time.sleep(0.1)
print()

#基本数据类型小测
print('请问   0   在程序中是什么数据类型呢？',end='')
test1 = input('请输入你的答案，用英文表示')
while test1 != 'int':
    print('很遗憾，回答错误！')
    test1 = input('请结合前面的内容或呼叫公主殿下，继续作答！')
print('回答正确！小刀锋利程度+1。')
print()

print('请问   -5   在程序中是什么数据类型呢？',end='')
test2 = input('请输入你的答案，用英文表示')
while test2 != 'int':
    print('很遗憾，回答错误！')
    test2 = input('请结合前面的内容或呼叫公主殿下，继续作答！')
print('回答正确！小刀锋利程度+1。')
print()

print('请问  3.1415926  在程序中是什么数据类型呢？',end='')
test3 = input('请输入你的答案，用英文表示')
while test3 != 'float':
    print('很遗憾，回答错误！')
    test3 = input('请结合前面的内容或呼叫公主殿下，继续作答！')
print('回答正确！小刀锋利程度+1。')
print()

print('请问  True  在程序中是什么数据类型呢？',end='')
test4 = input('请输入你的答案，用英文表示')
while test4 != 'bool':
    print('很遗憾，回答错误！')
    test4 = input('请结合前面的内容或呼叫公主殿下，继续作答！')
print('回答正确！小刀锋利程度+1。')
print()

'''
#介绍字符串
graList = ['恭喜勇士掌握三种基本数据类型的名称',
           '接下来，本关难度升级',
           '组合数据类型中，最常见的是：字符串类型str',
           '在Pyhon派中，组合数据类型都被其特殊的符号包裹住',
           '你可以理解为使用特殊的符号来防止其中的数据泄漏',
           '而字符串类型str使用一对引号来包裹数据',
           '可以是单引号、双引号、三引号',
           '三种引号均可使用，注意前后一致、成对出现即可！',
           '比如',
           "'这是一个字符串1'",
           '"这是一个字符串2"'
           ]

for graStr in graList:
    time.sleep(0.1)
    print(graStr)

msg = '''      咏鹅
 [唐]骆宾王
鹅，鹅，鹅，
曲项向天歌。
白毛浮绿水，
红掌拨清波。
'''
print(msg)
print('在程序中还可以使用三引号包裹多行的字符串')

for i in range(50):
    time.sleep(0.1)
    print('*',end='')
time.sleep(0.1)
print()
