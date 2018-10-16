#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#实现增删改查

#先手动插入数据
# with open('info.txt','w') as f:
#     str='''zhangsan 1000
# lisi 12000
# yanger 13000
# daha 8000
#     '''
#     f.write(str)

#查询
def select():
    with open('info.txt', 'r') as f:
        list=f.readlines()
        user_choice = input("请输入你要查询的员工姓名：")
        #print(list)
        for line in list:
            #print(line.strip().split()[0])
            #空行
            if line == '\n':
                line = line.strip("\n")
            else:
                if user_choice == line.strip().split()[0]:
                    print(user_choice, "的工资是：", line.split()[1])

#增加
def add():
    with open('info.txt', 'a') as f:
        user_add = input("请输入要增加的员工姓名和工资（例如：Eric 100000）：")
        #f.seek(0,2)
        #f.write('\n'+user_add)
        f.write(user_add+'\n')
        print("增加成功")

#删除
def delete():
    user_del=input("请输入要删除的员工姓名：")
    with open('info.txt','r') as f1:
        list=f1.readlines()
    with open('info.txt','w') as f2:
        for l in list:
            #空行
            if l == '\n':
                l=l.strip('\n')
            else:
                if user_del != l.strip().split()[0]:
                    # print(l)
                    f2.write(l)


#更新
def update():
    user_update = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：").strip()
    with open('info.txt','r') as f1:
        list=f1.readlines()
    with open('info.txt','w') as f2:
        for l in list:
            # 空行
            if l == '\n':
                l = l.strip('\n')
            else:
                if user_update.split()[0] != l.strip().split()[0]:
                   # print(l)
                    f2.write(l)
                else:
                    f2.write(user_update+'\n')

while True:
    chioce = '''
       1.查询员工工资
       2.修改员工工资
       3.增加新员工记录
       4.删除员工
       5.退出
       '''
    print(chioce)
    user_choice=input('请输入你的选择：'+'\r\n')
    if user_choice.isdigit():  # 判断输入的是否数字类型
        if user_choice == '1':
            select()  # 查询
        elif user_choice == '2':
            update()  # 修改
        elif user_choice == '3':
            add()  # 添加
        elif user_choice == '4':
            delete()  # 删除
        elif user_choice == '5':
            exit()  # 退出
        else:
            print("请输入正确的选项")
    else:
        print("请输入正确的选项")