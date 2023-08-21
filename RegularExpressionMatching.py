"""
TOP-DOWN VARIATION
"""
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dfs(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    firstMatch = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dfs(i, j+2) or firstMatch and dfs(i+1, j)
                    else:
                        ans = firstMatch and dfs(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dfs(0, 0)

"""
BOTTOM-UP VARIATION
"""
class Solution(object):
    def isMatch(self, text, pattern):
        dfs = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dfs[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                firstMatch = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dfs[i][j] = dfs[i][j+2] or firstMatch and dfs[i+1][j]
                else:
                    dfs[i][j] = firstMatch and dfs[i+1][j+1]

        return dfs[0][0]