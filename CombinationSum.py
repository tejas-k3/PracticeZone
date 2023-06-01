# https://leetcode.com/problems/combination-sum/
# Backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def recursiveHelper(currentTarget, startIndex, combination):
            if currentTarget == 0:
                result.append(combination[:])
                return
            if currentTarget < 0 or currentTarget - candidates[startIndex] < 0:
                return
            for i in range(startIndex, len(candidates)):
                combination.append(candidates[i])
                recursiveHelper(currentTarget-candidates[i], i, combination)
                combination.pop()
        recursiveHelper(target, 0, [])
        return result