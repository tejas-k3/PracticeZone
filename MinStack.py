""" https://leetcode.com/problems/min-stack/description/
Appraoch - 
Used list :)
"""

class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
