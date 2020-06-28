### python生成可执行文件——pyinstaller
（1）将xxxx.py复制到C:\Users\Zhaowei\AppData\Local\Programs\Python\Python37\Scripts\pyinstaller-develop文件夹里  
（2）cmd先cd到上述文件夹，再输入python pyinstaller.py -F xxxx.py  
（3）打开.\pyinstaller-develop\xxxx\dist\xxxx.exe，运行即可  

### 安装外部库

pip安装
控制面板\系统和安全\系统\高级系统设置\环境变量\系统变量\Path，双击，加入pip.exe所在路径
即可使用cmd->pip install ...  

setup.py安装
控制面板\系统和安全\系统\高级系统设置\环境变量\系统变量\Path，双击，加入python37的路径
打开setup.py文件夹，shift+右键->powershell->python setup.py install