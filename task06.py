'''
训练任务六：

模拟奶茶销售过程
    1)展示奶茶店的所有奶茶与价格（奶茶店菜单展示）
    2)自定义函数：点奶茶 milkTea_order()
        参数：奶茶序号，
        询问奶茶的甜度与温度
    3)自定义函数：计算总价 milkTea_order_sumPrice()
    4)自定义函数：展示订单信息与总价

    5)用户输入奶茶序号开始点奶茶
    6)运行一次程序可以点多杯奶茶，每点一杯奶茶，将奶茶字典加入已点奶茶列表
    7)展示已点奶茶列表，让用户确认信息，并计算奶茶总价
    
   请结合前面所得技能。
   删除以下程序里的序号“【1】、【2】、【3】、【4】、【5】、【6】”，填写正确代码，让程序正常运行
'''

import time

#菜单列表：列表中每个元素是一个奶茶字典，封装每种奶茶的序号、姓名、价格。
#        后续每个奶茶字典可加入原材料、制作过程等信息。
milkTeaList = [
    {"No.":"01","name":"幽兰拿铁","price":18},
    {"No.":"02","name":"声声乌龙","price":16},
    {"No.":"03","name":"桂 花 弄","price":15},
    {"No.":"04","name":"筝筝纸鸢","price":16},
    {"No.":"05","name":"烟火易冷","price":17},
    {"No.":"06","name":"素颜锡兰","price":14},
    {"No.":"07","name":"抹茶菩提","price":18},
    {"No.":"08","name":"凤栖绿桂","price":15},
    {"No.":"09","name":"浮云沉香","price":16},
    {"No.":"10","name":"三 季 虫","price":19},
    {"No.":"11","name":"蔓越阑珊","price":17},
    {"No.":"12","name":"少 年 时","price":15},
    {"No.":"13","name":"不 知 冬","price":16},
    {"No.":"14","name":"书 生 气","price":14},
    {"No.":"15","name":"桃 花 坞","price":17},
    {"No.":"16","name":"琉璃沁雪","price":16},
    {"No.":"17","name":"点 绛 唇","price":18},
    {"No.":"18","name":"浣 溪 沙","price":15},
    {"No.":"19","name":"醉 仙 翁","price":19},
    {"No.":"20","name":"清 风 引","price":14}
]

#展示产品
print('''欢迎光临木子奶茶店，我们有：
''')
#遍历菜单列表milkTeaList，依次取出奶茶字典 milkTea
for milkTea in milkTeaList:
    #展示格式：01.幽兰拿铁      ￥18
    #使用  字典名[key] 的方式，找到对应的 value 值，如：milkTea['name']获取奶茶名字
    print(milkTea['No.']+"."+【1】['name']+"\t￥"+str(milkTea['price']))

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
    print('您好！一杯',milkTea['name'])
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
    milkTea['sugar'] = sugarList[int(miklTeaSugarNo)-1]
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
    milkTea['tem'] = temList[int(miklTeaTemNo)-1]
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')#分隔标记
    return milkTea

'''
***计算已点奶茶总价函数：milkTea_order_sumPrice()
*************参数：已点奶茶列表
*************功能：计算奶茶总价
***********返回值：已点奶茶总价
'''
def 【2】(orderList):
    #奶茶订单总价sumPrice 原始数据为0
    sumPrice = 0
    for order in orderList:
        sumPrice += order['price']
    #将奶茶总价返回
    return 【3】

'''
***显示已点奶茶信息信息函数：showOrderList
*******************参数：已点奶茶列表
*******************功能：按照固定格式显示已点奶茶信息
*****************返回值：True 表示函数运行成功
'''
【4】 showOrderList(orderList):
    for order in orderList:
        print(order['name']+'\t'+order['sugar']+'\t'+order['tem']+'\t￥'+str(order['price']))
    print('共计：'+str(len(orderList))+'杯，总价：￥'+str(milkTea_order_sumPrice(orderList)))
    【5】 True
    
#创建已点奶茶空列表 milkTeaOrderList ：用于存放用户已点的奶茶
milkTeaOrderList = []

#开始点奶茶
milkTeaNo = input('请问小主需要喝点什么?')
#如果奶茶序号不为空，则可以正常点单；
while milkTeaNo!='':
    #完成点一杯奶茶的操作
    milkTea = milkTea_order(milkTeaNo)
    #将这个奶茶信息，存入已点奶茶列表
    milkTeaOrderList.append(milkTea)
    #询问客户是否需要其他奶茶
    milkTeaNo = input('请问小主还需要喝点什么(直接回车表示不再需要其他产品)?')
    
#显示已点奶茶信息，与客户确认    
showOrderList(【6】)
