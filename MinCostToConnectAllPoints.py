# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        adj = { i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 -x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        # Prim's
        res = 0
        visit = set()
        minHeap = [[0, 0]] # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            res+=cost
            for neiCOst, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCOst, nei])
        return res