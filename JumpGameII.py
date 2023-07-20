# https://leetcode.com/problems/jump-game-ii
# Bottom-Up DP
# O(nm) where n = len(nums) = max # of jumps and m = max(nums) = max jump size
# At each jump, jump to the index that gives us the farthest possible next jump
# This works because even if the optimal next jump isn't the farthest, it will be 
# contained in range(farthest) Optimal jump will always be at an index less than or equal to the 
# farthest possible jump dp[i+1] = max_i(nums[j]+j for j in range(dp[i]+1))
def jump0(self, nums: List[int]) -> int:
    if len(nums) == 1: return 0
    dp = [0]
    for i in range(len(nums)):
        dp.append(max((nums[j]+j for j in range(dp[i]+1))))
        if dp[i+1] >= len(nums)-1:
            break
    return len(dp) - 1

# Now the algorithm is O(n) time and O(1) space
def jump(self, nums: List[int]) -> int:
    if len(nums) == 1: return 0
    last = next = 0
    count = 1
    for i in range(len(nums)):
        temp = next
        next = max(nums[j]+j for j in range(last, next+1))
        if next >= len(nums)-1:
            break
        count += 1
        last = temp
    return count