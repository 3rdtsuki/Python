import pandas as pd
import numpy as np
# 生成一个五行四列的表格，列表头，行表头
data = pd.DataFrame(np.arange(20).reshape((5, 4)), columns=list('ABCD'), index=['a', 'b', 'c', 'd', 'e'])
data.drop('A',axis=1,inplace=True)    # 删除名为A的，列，原表格改变
print(data)

# 将pd格式的表格舍弃表头，转为np数组
np_data=np.array(data)
np_data=np_data.reshape(-1,1)   # 将一维数组转换为只有一列的二维数组，-1代表机器自己算有多少行
print(np_data)
