'''
新手训练任务六：

1.模拟单杯奶茶销售过程
    1)展示奶茶店的所有奶茶与价格（奶茶店菜单展示）
    2)自定义函数：点奶茶
        参数：奶茶名字，
        询问奶茶的甜度与温度
    3)自定义函数：计算总价

   请结合前面所得技能
   删除以下程序里的序号“【1】、【2】、【3】、【4】”，填写正确代码，让程序正常运行
'''

import time

#菜单列表：列表中每个元素是一个奶茶字典，封装每种奶茶的序号、姓名、价格。
#        后续每个奶茶字典可加入原材料、制作过程等信息。
milkTeaList = [
    {"order":"01","name":"幽兰拿铁","price":18},
    {"order":"02","name":"声声乌龙","price":16},
    {"order":"03","name":"桂 花 弄","price":15},
    {"order":"04","name":"筝筝纸鸢","price":16},
    {"order":"05","name":"烟火易冷","price":17},
    {"order":"06","name":"素颜锡兰","price":14},
    {"order":"07","name":"抹茶菩提","price":18},
    {"order":"08","name":"凤栖绿桂","price":15},
    {"order":"09","name":"浮云沉香","price":16},
    {"order":"10","name":"三 季 虫","price":19},
    {"order":"11","name":"蔓越阑珊","price":17},
    {"order":"12","name":"少 年 时","price":15},
    {"order":"13","name":"不 知 冬","price":16},
    {"order":"14","name":"书 生 气","price":14},
    {"order":"15","name":"桃 花 坞","price":17},
    {"order":"16","name":"琉璃沁雪","price":16},
    {"order":"17","name":"点 绛 唇","price":18},
    {"order":"18","name":"浣 溪 沙","price":15},
    {"order":"19","name":"醉 仙 翁","price":19},
    {"order":"20","name":"清 风 引","price":14}
]

#展示产品
print('''欢迎光临木子奶茶店，我们有：
''')

for milkTea in milkTeaList:
    #展示格式：1.幽兰拿铁      ￥18
    print(milkTea['order']+"."+milkTea['name']+"\t￥"+str(milkTea['price']))

