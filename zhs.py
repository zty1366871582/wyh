import csv
import time
import sys
csv.field_size_limit(500*1024*1024)
print("1:手机号查询 2:姓名查询 3:学号查询 ")
print("4:学校名称(全称)查询 5:qq邮箱查询 6:专业查询")
index =int(input("请选择查询方式\n"))
if index == 1:
    phone= input('请输入手机号:\n')
    with open('200w智慧树.csv','r',newline='',encoding='utf8')as f:
        read=csv.reader(f)
        for i in read:
            if i[0] == phone :
                print(i)
elif index ==2:
    name= input('请输入姓名:\n')
    with open('200w智慧树.csv','r',newline='',encoding='utf8')as f:
        read=csv.reader(f)
        for i in read:
            try:
                if name in i[1]:
                    print(i)
            except:
                continue
elif index ==3:
    stunum= input('请输入学号:\n')
    with open('200w智慧树.csv','r',newline='',encoding='utf8')as f:
        read=csv.reader(f)
        for i in read:
            try:
                if i[3] == stunum :
                    print(i)
            except:
                continue
elif index ==4:
    college= input('请输入学校名称:\n')
    with open('200w智慧树.csv','r',newline='',encoding='utf8')as f:
        read=csv.reader(f)
        for i in read:
            try:
                if college in i[5]:
                    print(i)
            except:
                continue
elif index ==5:
    qmail= input('请输入qq邮箱:\n')
    with open('200w智慧树.csv','r',newline='',encoding='utf8')as f:
        read=csv.reader(f)
        for i in read:
            #print(i)
            #time.sleep(3)
            if i[2] == qmail :
                print(i)
elif index ==6:
    pro= input('请输入专业名称:\n')
    with open('200w智慧树.csv','r',newline='',encoding='utf8')as f:
        read=csv.reader(f)
        for i in read:
            try:
                if pro in i[4]:
                    print(i)
            except:
                continue
else:
    print("输入错误请重试")
print("查询完成")
