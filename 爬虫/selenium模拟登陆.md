```python
from selenium import webdriver
from selenium.webdriver.common.by import By #用于指定 HTML 文件中 DOM 标签元素
from selenium.webdriver.support.ui import WebDriverWait #等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC #指定等待网页加载结束条件

broswer = webdriver.Chrome()
url="http://eamis.nankai.edu.cn"
broswer.get(url)
WebDriverWait(broswer, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'chrome')))

user = broswer.find_element_by_xpath('//*[@id="username"]')
pwd = broswer.find_element_by_xpath('//*[@id="password"]')

user.click()
user.send_keys('******')
pwd.click()
pwd.send_keys('******')

login = broswer.find_element_by_xpath('//*[@id="loginForm"]/table[2]/tbody/tr[6]/td/input').click()
myScore=broswer.find_element_by_xpath('//*[@id="menu_panel"]/ul/li[1]/ul/div/li[10]/a').click()



```
