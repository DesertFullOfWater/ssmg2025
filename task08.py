'''
训练任务八：

模拟奶茶销售过程
    1)从奶茶菜单文件中读取奶茶信息，展示奶茶店的所有奶茶与价格（奶茶店菜单展示）
    2)自定义函数：点奶茶 milkTea_order()
        参数：奶茶序号，
        询问奶茶的甜度与温度
    3)自定义函数：计算总价 milkTea_order_sumPrice()
    4)自定义函数：展示订单信息与总价showOrderList()

    5)用户输入奶茶序号开始点奶茶；
      奶茶序号可能无法转换为整数类型，在菜单列表中不能查找对应奶茶信息
      使用异常处理机制，以保证程序正常运行
    6)运行一次程序可以点多杯奶茶，每点一杯奶茶，将当前奶茶信息加入已点奶茶列表
    7)展示已点奶茶列表，让用户确认信息，并计算奶茶总价
    8)将此次奶茶的订单存入订单文件中。
    
   请结合前面所得技能。
   删除以下程序里的序号“【1】、【2】、【3】、【4】、【5】、【6】”，填写正确代码，让程序正常运行
'''

import time
import csv

#展示产品
print('''欢迎光临木子奶茶店，我们有：
''')

milkTeaList = []
# 读取奶茶菜单文件 奶茶菜单.csv，打印奶茶菜单
with open("08奶茶菜单.csv","r",encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        milkTeaList.append(row)
        print(row[0]+".  "+row[1]+"\t￥"+row[2])
  
'''
*****点奶茶函数：milkTea_order()
********参数：奶茶序号
********功能：询问用户奶茶甜度、温度，将甜、温度存入已点奶茶字典
******返回值：奶茶信息字典
'''
def milkTea_order(_no):
    #根据序号，从奶茶列表中获取当前奶茶字典信息
    milkTea = milkTeaList[int(_no)-1]
    #与用户确认奶茶姓名
    print('您好！一杯',milkTea[1])
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #展示奶茶糖分分类
    print('我们有：',end='')
    #奶茶糖分分类列表
    sugarList = ['全糖','七分','五分','三分','无糖']
    for i in range(len(sugarList)):
        print(str(i+1)+'.'+sugarList[i]+'  ',end='')
    # miklTeaSugarNo 绑定用户输入的当前奶茶的糖分序号 
    miklTeaSugarNo = input('请问您需要几分糖(输入序号)？')
    # 将当前奶茶的糖分信息，存入奶茶字典中
    milkTea.append(sugarList[int(miklTeaSugarNo)-1])
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #展示奶茶温度分类
    print('我们有：',end='')
    #奶茶糖分分类列表
    temList = ['加冰','少冰','去冰','常温','热']
    for i in range(len(temList)):
        print(str(i+1)+'.'+temList[i]+'  ',end='')
    # miklTeaTemNo 绑定用户输入的当前奶茶的糖分序号 
    miklTeaTemNo = input('请问您需要什么温度(输入序号)？')
    # 将当前奶茶的糖分信息，存入奶茶字典中
    milkTea.append(temList[int(miklTeaTemNo)-1])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')#分隔标记
    return milkTea

'''
***计算已点奶茶总价函数：milkTea_order_sumPrice()
*************参数：已点奶茶列表
*************功能：计算奶茶总价
***********返回值：已点奶茶总价
'''
def milkTea_order_sumPrice(orderList):
    #奶茶订单总价sumPrice 原始数据为0
    sumPrice = 0
    for order in orderList:
        sumPrice += int(order[2])
    #将奶茶总价返回
    return sumPrice

'''
***显示已点奶茶信息信息函数：showOrderList
*******************参数：已点奶茶列表
*******************功能：按照固定格式显示已点奶茶信息
*****************返回值：True 表示函数运行成功
'''
def showOrderList(orderList):
    for order in orderList:
        print(order[1]+'\t'+order[3]+'\t'+order[4]+'\t￥'+order[2])
    print('共计：'+str(len(orderList))+'杯，总价：￥'+str(milkTea_order_sumPrice(orderList)))
    return True
    
#创建已点奶茶空列表 milkTeaOrderList ：用于存放用户已点的奶茶
milkTeaOrderList = []

#开始点奶茶
milkTeaNo = input('请问小主需要喝点什么?(输入产品序号)')
#如果奶茶序号不为空，则可以正常点单；
while milkTeaNo!='':
    try:
        int(milkTeaNo)
    except ValueError:
        print('不好意思，您所需的产品，小店暂时没有！')
    else:
        #完成点一杯奶茶的操作
        milkTea = milkTea_order(milkTeaNo)
        #将这个奶茶信息，存入已点奶茶列表
        milkTeaOrderList.append(milkTea)
    #询问客户是否需要其他奶茶
    milkTeaNo = input('请问小主还需要喝点什么(输入产品序号，直接回车表示不再需要其他产品)?')
    
#显示已点奶茶信息，与客户确认    
showOrderList(milkTeaOrderList)

with open("奶茶订单.csv","a",encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(milkTeaOrderList)
print('订单已完成')
