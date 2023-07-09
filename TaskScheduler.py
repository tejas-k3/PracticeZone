# https://leetcode.com/problems/task-scheduler/description/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        # max frequency ie alphabet
        fMax = max(frequencies)
        # count the most frequent tasks
        nMax = frequencies.count(fMax)
        return max(len(tasks), (fMax - 1) * (n + 1) + nMax)

# GREEDY SOL BELOW
"""
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        frequencies.sort()
        # max frequency
        fMax = frequencies.pop()
        idleTime = (fMax - 1) * n
        while frequencies and idleTime > 0:
            idleTime -= min(fMax - 1, frequencies.pop())
        idleTime = max(0, idleTime)
        return idleTime + len(tasks)
"""