柱状图
```python
import matplotlib.pyplot as plt
import numpy as np
a=[i for i in range(2009,2019)]
b=[1902,2103,2641,2957,3262,3611,4000,4440,5001,5539]
plt.bar(a,b)####柱状图
plt.xticks(a)
for i in range(10):
    plt.text(a[i]-0.35,b[i]+80,b[i])#在柱状图上添加数据（依据坐标）
plt.rcParams['font.sans-serif'] = ['SimHei']#防止中文乱码
#plt.xlabel('年')
plt.ylabel('国内游客人次/百万')
plt.show()

a2=[i for i in range(2009,2020)]
b2=[0.3,0.36,0.42,1.12,1.81,2.22,2.6,2.94,3.25,3.65,3.85]
plt.bar(a2,b2)
plt.xticks(a2)
for i in range(11):
    plt.text(a2[i] - 0.35, b2[i]+0.075 , b2[i])
plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.xlabel('年')
plt.title('2009-2019年中国在线旅游用户规模')
plt.ylabel('人数/亿')
plt.show()
```
折线图
```python
a2=[i for i in range(2009,2019)]
b2=[0.3,0.36,0.42,1.12,1.81,2.22,2.6,2.94,3.25,3.65]
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()#对称的双y轴
ax1.plot(a,b)#####折线图
ax1.set_ylabel('国内游客人次/百万')
ax2.plot(a2,b2,c='red')
ax2.set_ylabel('人数/亿')
plt.xticks(a2)
plt.show()
```