"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
Approach -
Iterate through the list pushing it in a stack. For any opeartor,
pop last 2 values from stack and push the resulted value.
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        
        for i in tokens:
            if i == '+':
                val =(int(stack.pop()) + int(stack.pop()))
                stack.append(val)
            elif i == '-':
                t = int(stack.pop())
                v = int(stack.pop())
                val =(v - t)
                stack.append(val)
            elif i == '/':
                t = int(stack.pop())
                v = int(stack.pop())
                val =int(v/t)
                stack.append(val)
            elif i == '*':
                val =(int(stack.pop()) * int(stack.pop()))
                stack.append(val)
            else :
                stack.append(i)
        
        return int(stack.pop())