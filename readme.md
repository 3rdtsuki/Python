#### Python基本语法

##### 按行标准输入

```python
x,y,z=map(int,input().split())
```

##### 列表的更新

```python
a=[1,2,3]
a.append(4)
a.pop(2) # pop掉下标为2的元素。作为队列就是pop(0)
```

##### 初始化二维数组

四行五列

```python
[[0]*5 for i in range(4)]
```

##### zip

```python
```



##### enumerate：索引-对象对

```python
a=['hello','happy','world']
for i,item in enumerate(a):
    print(i,item)
```

##### dict

```python
dic={}
dic[1]=2
k in dic # 是否有键
dic.keys()
dic.values()
dic.items()
```

在字典中查值比在数组中快

##### defaultdict

```python
from collections import defaultdict
dic=defaultdict(list) # 建立一个{a:[]}型的字典
```

##### 二分查找bisect

bisect_left(list,key)：若存在，返回第一次出现的下标；若不存在，返回应该在的位置

```python
import bisect
pos=bisect.bisect_left(a,6)
```

##### lambda表达式

二维数组按第一维排序

```python
a.sort(key = lambda x:x[0])
```

------



#### pip镜像

```sh
阿里云：pip install ... -i https://mirrors.aliyun.com/pypi/simple
清华：pip install ... -i https://pypi.tuna.tsinghua.edu.cn/simple
中科大：pip install ... -i https://pypi.mirrors.ustc.edu.cn/simple
```

从源代码安装库

```sh
python setup.py install
```



#### 读文件

读txt

```python
def read_from_txt(path):
    with open(path, 'r', encoding="utf-8", newline="") as fp:
        items = []
        reader = fp.readlines()
        for line in reader:
            line=line.strip()
            items.append(line)  # 除去换行
        return items
```

读csv：

```python
import csv
def read_from_csv(path):
    items=[]
    csv.field_size_limit(500 * 1024 * 1024)
    with open(path,'r',encoding="utf-8",newline="")as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            items.append(line)
    return items	# items是一个二维数组，每句话是一个list
```

#### 写文件

存入txt：**使用fp.write()比csv快得多**

```python
def write_into_txt(path,lines):
    with open(path,'w',encoding="utf-8",newline="")as fp:
        for line in lines:
            fp.write(line+'\n')
```

存入csv：注意必须加中括号，否则输出每个字符间都有逗号

```python
import csv
def write_into_csv(path,table,attrs):
    with open(path,'w',encoding="utf-8",newline="")as fp:
        writer = csv.writer(fp)
        writer.writerow([attrs])  # 属性列名
        writer.writerows([table])
```

存入xls表格中：

```python
import pandas as pd
def write_into_excel(path,items): # items是二维数组
    df=pd.DataFrame(items)
    df.to_excel(path)
```



#### 生成可执行文件

（0）`pip install pyinstaller`

（1）将`xxxx.py`复制到`Python38\Scripts\xxxx`文件夹里

（2）cmd先cd到上述文件夹，`pyinstaller -F xxxx.py`

（3）打开.\xxxx\dist\xxxx.exe，运行即可



#### 正则表达式

Regular Expression

re.sub：用于替换字符串中的匹配项

re.compile用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

re.findall：在字符串中找到正则表达式所匹配的所有子串，并返回一个列表

```python
import re
# .*?代表任意字符
# 找标签之间的内容
s='<li><a href="/paper/2021/hash/000c076c390a4c357313fca29e390ece-Abstract.html">Beyond Value-Function Gaps: Improved Instance-Dependent Regret Bounds for Episodic Reinforcement Learning</a> <i>Christoph Dann, Teodor Vanislavov Marinov, Mehryar Mohri, Julian Zimmert</i></li>'
titles=re.findall('<a href\=.*?>(.*?)</a>',s)
authors=re.findall('<i>(.*?)</i>',s)
print(titles)
print(authors)
```

要删除text里面所有形如<123>的字符串

```python
path="./ee.txt"
with open(path)as f:
    text=f.read()
    h=re.compile('<[0-9]+>')
    text=h.sub('',text)
    print(text)
```

#### 随机数

```python
import random
print(random.randint(0,9))
```



#### matplotlib作图

##### 折线图

```python
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False	# 避免中文乱码
def make_plot(x,y1,y2):
    plt.plot(x,y1,marker='^',label='前缀索引')
    plt.plot(x,y2,marker='.',label='片段索引')
    plt.xlabel('分区数')
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(32))# 刻度
    plt.ylabel('运行时间/ms')
    plt.legend()    # 图例
    plt.show()
x=[32,64,96,128]
y1=[11639,11394,12872,14946]
y2=[20663,19947,21813,22821]
make_plot(x,y1,y2)
```



##### 双柱图

```python
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

x = numpy.array([0.6,0.7,0.8])
y = [16065,11102,15019]
y1 = [22061,21010,19474]

bar_width = 0.02 # 柱宽

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(0.1))  # 刻度
plt.bar(x-0.01, y, bar_width, align="center", color="c", label="前缀索引", alpha=0.5)
plt.bar(x+0.01, y1, bar_width, color="b", align="center", label="片段索引", alpha=0.5)

plt.xlabel('相似度阈值')
plt.ylabel('运行时间/ms')

plt.legend()

plt.show()
```

##### 散点图

```python
# 二维散点图
def make_scatter_plot():
    x1=[1,2,3]
    y1=[1,2,3]
    x2=[4,5,6]
    y2=[6,5,4]
    plt.scatter(x1, y1, c='blue', alpha=0.4, label='类别A')
    plt.scatter(x2, y2,  c='red', alpha=0.4, label='类别B')
    plt.show()

# 绘制三维散点图，vec：每个元素都是[x,y,z]
def make_scatter_plot(vec, label, title):
    fig = plt.figure()
    ax = Axes3D(fig)

    n = len(X)
    color_list = ['blue', 'red', 'green']
    for i in range(n):
        # 共有三类label，所以x,y,z都分成三类
        x, y, z = [[], [], []], [[], [], []], [[], [], []]
        x[label[i]].append(vec[i][0])
        y[label[i]].append(vec[i][1])
        z[label[i]].append(vec[i][2])
        plt.scatter(x[label[i]], y[label[i]], z[label[i]], c=color_list[label[i]], label='类别' + str(label[i]))

    ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
    ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})

    ax.set_title(title)
    plt.show()
```

##### 生成图像

```python
import matplotlib.pyplot as plt
import numpy as np

path=r'D:\pic\fbk.jpg'
image=plt.imread(path)
print(image.shape)
plt.imshow(image)
plt.show()

# 自己构建np二维数组，plt生成图片
image=np.arange(36).reshape(6,6)
plt.imshow(image)
plt.show()
```





#### 日语乱码解析

```python
path=r'D:\Mika_Applications\otome_domain\オトメドメイン視点変更パッチ（ＤＬ版）\readme_1_02.txt'

with open(path,'r',encoding='gbk')as f:
	text=f.readlines()
	for line in text:
		real_text=line.encode('gbk').decode('shift-jis')
		print(real_text)
```

#### DataFrame

csv转为dataframe

```python
import pandas as pd
csv_path=r''
df=pd.read_csv(csv_path)

# 打印Info列的前五行
print(df['Info'][:5])

# 遍历df的每一行
for i,line in df.iterrows():
    print(line)
    
# 将该列元素从字符型转为数值型
df['Info'] = pd.to_numeric(df['Info'], errors='raise')

# 要想修改df数据，需要使用df[col,row]才不会报错
df[1,0]=1
```

df写csv

```python
df.to_csv(output_path)
```



```python
a=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
a.iloc[0:2]#第0,1行
a.iloc[:,-1]#最后一列
a.iloc[:, 0:-1]#除了最后一列的所有列

a=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(a)
a[2,:]# 其实就是a[2][:]，输出第二行所有列
np.vstack(([1,1,1],a))#在a前面加一行[1,1,1]

# 快速计算方差，超级快！
mse = np.linalg.norm(np.dot(X, theta) - y) ** 2 / n
```

#### 数字转换

```python
ord('a')# 字符转asc
chr(65)# asc转字符
int("1010",2)# 二进制转十进制
bin(133).zfill(8)# 将133转为二进制，并补前0使得补足8位
hex
```

#### numpy

```python
import numpy as np
a=[1,2,3,4]
a=np.array(a)	# 转为array
a=a.tolist()	# 转为list
a=np.arange(20).reshape(4,5) # 生成一个4x5的矩阵，元素为0-19
```

将多个矩阵打包成npz

```python
a=np.arange(20).reshape(4,5)
b=np.arange(36).reshape(6,6)
# 每个属性是矩阵的名字
np.savez('dataset.npz',
         x_train=a,
         y_train=b)
data=np.load('dataset.npz')
print(data['x_train'])
print(data['y_train'])
```





#### tqdm进度条

```python
from tqdm import tqdm
for batch in tqdm(range(train_batch_num)):
```

#### 多项式展开计算

```python
from sympy import symbols, expand

x, y = symbols('x y')
f = (x + 1) ** 2
print(expand(f))
```
