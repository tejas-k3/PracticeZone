# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        answer = []
        for left_count in range(n):
            for left_string in self.generateParenthesis(left_count):
                for right_string in self.generateParenthesis(n - 1 - left_count):
                    answer.append("(" + left_string + ")" + right_string)
        
        return answer

"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return generator("", n)

def generator(stringVal, limit):
    openCount = stringVal.count('(')
    closeCount = stringVal.count(')')
    results = []
    if not limit:
        if openCount == closeCount:
            results.append(stringVal)
            # return stringVal
        elif openCount > closeCount:
            results.extend(generator(stringVal + ')', limit))
    if openCount == closeCount and limit:
        results.extend(generator(stringVal + '(', limit-1))
    elif openCount > closeCount and limit:
        results.extend(generator(stringVal + '(', limit-1))
        results.extend(generator(stringVal + ')', limit))
    return results
"""