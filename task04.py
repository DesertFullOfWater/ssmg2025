'''
新手训练任务四：

1.计算奶茶总价
   奶茶店开业大酬宾，每杯奶茶，仅售5元，超过5杯再打8折。
   每输入一杯奶茶名，奶茶杯数增加1，且总价增加5元
   请结合前面所得技能
   删除以下程序里的序号“【1】、【2】、【3】”，填写正确代码，让程序正常运行

'''


print('欢迎光临艾莎公主奶茶店！')
print('本店开业大酬宾，奶茶全场5元，多买多赚哦！')

naichaPrice = 0     #naichaPrice为奶茶的总价
count = 0                  #count为奶茶数量
naichaName = input('请问你想喝点什么？')        #naichaName 为奶茶的名字

【1】 naichaName!='':
    count +=1
    naichaPrice += 5
    naichaName = input('请问您还想喝点什么？（输入回车键表示不需要其他奶茶了。）')

if count>=5:
    print('您好！谢谢您的光顾，总价：',naichaPrice,'元')
    print('您买了',【2】,'杯，我再给您打个八折，您付：', naichaPrice*0.8 ,'元即可')
【3】:
    print('您好！你的奶茶总计：',naichaPrice,'元！')

