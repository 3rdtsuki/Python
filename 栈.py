python的栈通过list来实现，栈顶即stack[-1]，入栈append，出栈pop
用return not stack判断是否为空，非空return False（not stack=栈为空），或者直接return len(stack)==0

leetcode 20.有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        pair={')':'(',']':'[','}':'{'}
        for i in s:
            if i=='{' or i=='[' or i=='(':
                stack.append(i)
            elif len(stack)==0 or pair[i]!=stack[-1]:
                return False
            else:
                stack.pop()
        return not stack
