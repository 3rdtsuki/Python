import random
import csv
import linecache
import time
path=r'C:\Users\Mika\Desktop\记单词.txt'
with open(path,'r+',encoding="utf-8",newline="")as fp:
    while True:
        num = input("1.增加单词\n2.随机抽取\n3.删除单词\n请选择服务内容（输入x退出）：")
        num=int(num)
        if num==1:
            word=input("请输入单词：")
            mean=input("请输入含义：")
            fp.write(word+","+mean+'\n')
            print("添加 %s 成功！\n"%word)
        elif num==2:
            length=len(fp.readlines())-1 # 最后有个换行
            while True:
                i=random.randint(0,length)
                text=linecache.getline(path,i)
                word,mean=text.split(',')
                print(word)
                ans=input()
                print(mean)
                if ans=='x':
                    break
        else:
            print("再见！")
            break
