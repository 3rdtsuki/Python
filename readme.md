```python
镜像：
阿里云：pip install ... -i https://mirrors.aliyun.com/pypi/simple
清华：pip install ... -i https://pypi.tuna.tsinghua.edu.cn/simple
中科大：pip install ... -i https://pypi.mirrors.ustc.edu.cn/simple
```

#### 读文件

读txt

```python
读txt：
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



#### 按行标准输入

```python
x,y,z=map(int,input().split())
# 例如
```

#### 
