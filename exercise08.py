'''
第八课练习：
     CSV文件读写

    1.导入csv模块，以便读取CSV文件
    2.使用open()函数打开文件 获取文件对象
    3.从文件对象中获取 读取对象/写入对象
    4.按行读取文件/按行写入文件

    环节一：读取108将信息文件 08heros.csv，打印每个人的姓名与封号
    环节二：追加第109人信息
     
'''
import csv

# ======================
# 环节一：读取108将信息文件 08heros.csv，打印每个人的姓名与封号
#               1.使用 r-读取模式 打开08heros.csv文件，讲文件信息保存在 文件对象f 当中，
#               2.从文件对象f 中 获取读取对象，
#               3.遍历读取对象，打印所需的英雄信息
# ======================
with open("08heros.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        print('姓名：',row[0],'\t封号：',row[3])
        
print("✅ 所有英雄封号打印完毕！")
    
# ======================
# 环节二：追加第109人信息
#               1.使用 a-追加写入模式 打开08heros.csv文件，讲文件信息保存在 文件对象f 当中，
#               2.从文件对象f 中 获取写入对象，
#               3.讲109人信息写入文件的最后一行
# ======================
new_hero = ["李二狗","109","魔法杖","艾莎公主"]
with open("08heros.csv", "a", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_hero)

print("✅ 李二狗已追加到最后一行！")
