# https://leetcode.com/problems/redundant-connection/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.alreadyConnected = defaultdict(list)
        for edge in edges:
            self.visited = defaultdict(bool)
            u, v = edge[0], edge[1]
            if self.isAlreadyConnected(u, v):
                return edge
            self.alreadyConnected[u].append(v)
            self.alreadyConnected[v].append(u)
    def isAlreadyConnected(self, u, v):
        if u == v:
            return True
        for xAdjacent in self.alreadyConnected[u]:
            if not self.visited[xAdjacent]:
                self.visited[xAdjacent] = True
                if self.isAlreadyConnected(xAdjacent, v):
                    return True
        return False