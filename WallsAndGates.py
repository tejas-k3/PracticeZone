# https://www.lintcode.com/problem/663/
class Solution:
    def wallsAndGates(self, rooms):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
        
        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or room[r][c]==-1):
                return
            visit.add((r,c))
            q.append([r,c])
    
        for r in range(ROWS):
            for c in range(COLS):
                if room[r][c]==0:
                    q.append([r, c])
                    visit.add((r, c))
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c]= distance
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist+=1