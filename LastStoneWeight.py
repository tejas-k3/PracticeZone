# https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Doing negative because minHeap!
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)
        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0