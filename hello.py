'''
本程序为木子程序系列课第一课示例程序
主要引导大家学习：
1.代码运行方式
2.注释的规范使用
3.输入输出函数的基本用法
帮助同学们建立对于编程的兴趣

'''

import time

#一、引导
time.sleep(0.5)
print('********************************三穗民高2025级同学，你好! *********************************')

#第一小节：程序介绍引导词
guide = ['欢迎来到程序世界！',
         '程序世界门派众多，功法丰富，变幻莫测。',
         '接下来，我们将学习Pyhon派的入门规则',
         '如：程序语句、程序结构、数据类型转换、变量、函数、表达式、运算符。',
         '在学习过程中，',
         '程序中满篇的英文可能让你头晕脑涨，',
         '程序中奇怪的符号可能让你找不着北，',
         '但是……',
         '熟能生巧，百炼成钢',
         '请大家跟随莎姐（艾莎公主）的节奏，勤加练习。',
         '你一定会发现程序世界的奇妙的！']

#从引导词列表中逐句打印引导词
for guideStr in guide:
    time.sleep(1.2)
    print(guideStr)

#询问学生是否愿意接受程序的挑战
time.sleep(1)
YoN = input('你准备好迎接编程世界的挑战了吗？（Yes/No）')

#判断学生的挑战意愿，并输出对应鼓励话语
if YoN == "Yes" or YoN == "yes" or YoN == 'YES':
    time.sleep(0.5)
    print('真不愧是三穗民高的勇士啊！')
else:
    time.sleep(0.5)
    print('深吸一口气，大胆往前冲，你可是打败三穗50%少年的勇士呢！')
    time.sleep(1)
    print('所以……')
    time.sleep(1)
    print('小小基础编程，你肯定可以轻松拿下的。')

time.sleep(1)
print('话不多说，任务即将开启，请准备')

#模拟游戏正式开始的加载画面
for i in range(25):
    time.sleep(0.1)
    print('*',end='')
    
time.sleep(0.1)
print('挑战程序世界',end='')

for i in range(25):
    time.sleep(0.1)
    print('*',end='')
time.sleep(0.1)
print()

#通过连接程序世界的方式，讲解输入输出函数
print('第一关：《连接程序世界》')
time.sleep(1)
print('欢迎进入新手村')
time.sleep(1)
print('新手训练营第一关：《连接程序世界》')

#模拟加载画面
for i in range(50):
    time.sleep(0.1)
    print('*',end='')
time.sleep(0.1)
print()

#知识讲解
time.sleep(1)
userName = input('这位勇士，请问阁下如何称呼？')
time.sleep(1)
print(userName,'你好！')
time.sleep(1.2)
print('程序世界的基本规则是：数据交换')
time.sleep(1.2)
print('也就是说你给应用程序数据，应用程序给你结果')
time.sleep(1.2)
print('中间的运算过程被应用程序所控制')
time.sleep(1.2)
print('与程序世界产生数据交换最简单的方法就是在程序中使用输入输出函数')
time.sleep(1.2)
print('接下来，请听系统讲解吧！')

input()
input('您听懂了吗？')
print('接下来，你可以选择向系统提问，也可打开新手第一个任务进行训练。')

#预告下一个任务
input()
print('恭喜你完成新手第一个任务')
time.sleep(1.2)
print('下一个任务预告：数据类型与变量')
time.sleep(1.2)
print(userName,'你有信心吗？')

isbe = input()
if isbe == "有":
    time.sleep(0.5)
    print('很好！我们下次见')
else:
    time.sleep(0.5)
    print('没关系，系统会非常耐心解答你的疑惑的')
    time.sleep(1)
    print('加油！我们下次见')
