# https://leetcode.com/problems/parallel-courses-iii
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        @cache
        def dfs(node):
            if not graph[node]:
                return time[node]
            
            ans = 0
            for neighbor in graph[node]:
                ans = max(ans, dfs(neighbor))

            return time[node] + ans
        
        graph = defaultdict(list)
        for (x, y) in relations:
            graph[x - 1].append(y - 1)
        
        ans = 0
        for node in range(n):
            ans = max(ans, dfs(node))

        return ans