# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""
[0,1,2,3]
0 --- 1
 \
  \
   2
3
[0, 0, 0, 3]
[3, 1, 1, 1]
 res, n = 2,2
 par[2] = 0
 while 2!= 0:
    par[0]=par[0]
    0 = 0
"""

class Solution:
    def countComponents(n, edges):
        par = [i for i in range(n)]
        rank = [1]*n
        def find(n):
            res = n
            while res != par[res]:
                par[res]=par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                # Cant do union both are in same set
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2]+= rank[p1]
            else:
                par[p2] = p1
                rank[p1]+=rank[p1]
            return 1
        res = n
        for n1, n2 in edges:
            res-=union(n1, n2)
        return res