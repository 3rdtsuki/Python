import re
# pattern：正则表达式，string：字符串，flags：可选标志
re.match(pattern, string, flags=0)：从字符串的起始位置匹配一个正则表达式，返回首尾下标
re.search(pattern, string, flags=0)：从前向后匹配正则表达式，并返回第一个正确位置

exp:
>>>re.search('a*b+',"dddabbb")
<re.Match object; span=(3, 7), match='abbb'>
