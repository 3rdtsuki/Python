GUI：图形用户界面（Graphical User Interface）

```python
text=Text(width,height) #文本框
btn=Button(text="名称",command=函数) #按钮
mygui.wm_attributes('-topmost',1)#窗口置顶
```



```python
# 简易的字数统计程序
from tkinter import *
mygui=Tk(className="かぐらなな")
mygui.geometry('1000x800')
text=Text(width=60,height=40)
text.pack()
answer=Text(width=6,height=4)
answer.pack()

def showAns():#字数统计
    answer.delete(1.0, "end")
    contents = text.get(1.0, "end")
    answer.insert("insert",len(contents)-1)
    
btn=Button(text="submit",command=showAns)#command表示点击后发生的事件
btn.pack()

mainloop()

```

```python
# 简易的背单词软件
from tkinter import *
import tkinter.font as tkFont#字体库
import xlrd
def excel(path):
  excel=xlrd.open_workbook(path)
  table=excel.sheets()[1]
  a=[]
  for i in range(0,table.ncols):
    a.append(table.col_values(i))
  return a

vocabulary_table=excel(r'C:\Users\Zhaowei\Desktop\背单词.xls')
print(vocabulary_table)
mygui=Tk(className="かぐらなな",)
mygui.geometry('800x500')

ft_eng = tkFont.Font(family='Calibri', size=18, weight=tkFont.BOLD)#字体设置语句必须写在Tk()的后面
ft_chi = tkFont.Font(family='Calibri', size=18)

text=Text(width=20,height=4,font=ft_eng)
text.pack()

answer=Text(width=20,height=4,font=ft_chi)
answer.pack()

cnt=[0]
def jpp():#########因为python没有引用，所以如果想要函数修改实参必须通过列表
    cnt[0]+=1

def next(i):
    text.delete(1.0, "end")
    answer.delete(1.0, "end")
    text.insert("insert",vocabulary_table[i][cnt[0]])
    answer.insert("insert",vocabulary_table[i+1][cnt[0]])
    jpp()

btn=Button(text="submit",command=lambda:next(0))#lambda:可以让command的函数传参
btn.pack()

mainloop()
```

