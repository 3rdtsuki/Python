存数据：

```python
存入xls表格中：
import pandas as pd
def write_into_excel(path,items): # items是二维数组
    df=pd.DataFrame(items)
    df.to_excel(path)
    
存入txt或csv中:
    （1）csv函数csv.writer(fp)
    （2）直接写fp.write(str)
import csv
def write_into_csv(path,items,attrs):
    with open(path,'w',encoding="utf-8",newline="")as fp:
        writer = csv.writer(fp)
        writer.writerow(attrs)  # 属性列名
        writer.writerows(items)
```

读数据：输入文本，输出list，每个元素为一句话

```python
读excel：
table=pd.read_excel(path) #DataFrame类型
table=table[0].values.tolist()	# DataFrame转为list！！！

读csv：
def read_from_csv(path):
    items=[]
    csv.field_size_limit(500 * 1024 * 1024)
    with open(path,'r',encoding="utf-8",newline="")as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            items.append(line)
    return items	# items是一个二维数组，每句话是一个list

读txt：
with open(path,'r',encoding="utf-8",newline="")as fp:
    items=[]
    reader=fp.readlines() # readlines大法
    for line in reader:
        items.append(line.strip())	# 除去换行，很重要！
    return items    # 返回一维数组list

with open(output,'a',encoding='utf-8')as fp:
    for i in range(len(table)):
        gen=jieba.cut(table[i])
        fp.write(' '.join(gen))
        fp.write('\n')	# 最后输出要换行
```

读入DataFrame类型的sentences，转为list，并结巴分词，写入文件

```python
table=pd.read_excel(path) #DataFrame类型
table=table[0].values.tolist()	# DataFrame转为list！！！

with open(output_path,'a',encoding='utf-8')as fp:
    for i in range(len(sentences)):
        gen=jieba.cut(sentences[i])	# jieba.cut(str)生成的是generator类型
        fp.write(' '.join(gen))	# join可以生成str类型
```


### python生成可执行文件——pyinstaller
（0）pip install pyinstaller

（1）将xxxx.py复制到C:\Users\Mika\AppData\Local\Programs\Python\Python38\Scripts\xxxx文件夹里

（2）cmd先cd到上述文件夹，再输入pyinstaller -F xxxx.py

（3）打开.\xxxx\dist\xxxx.exe，运行即可

### 安装外部库

pip安装
控制面板\系统和安全\系统\高级系统设置\环境变量\系统变量\Path，双击，加入pip.exe所在路径
即可使用cmd->pip install ...  
```python
镜像：
阿里云：pip install ... -i https://mirrors.aliyun.com/pypi/simple
清华：pip install ... -i https://pypi.tuna.tsinghua.edu.cn/simple
中科大：pip install ... -i https://pypi.mirrors.ustc.edu.cn/simple
```
setup.py安装
控制面板\系统和安全\系统\高级系统设置\环境变量\系统变量\Path，双击，加入python37的路径
打开setup.py文件夹，shift+右键->powershell->python setup.py install
