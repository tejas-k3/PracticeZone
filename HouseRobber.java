// https://leetcode.com/problems/house-robber/
/*
Approach -
DP Problem, solved using memoization, initiate array with -1 value of size max (100 as per que)
Iterate through the array from left to right and keep taking max value of 2 options using recursive call
with valueHouse(i+1) OR valueHouse(i+2) + currentValue, return the final max Value.
*/
import java.util.Arrays;
class Solution {
    private int[] memo;
    public int rob(int[] nums) {
        this.memo = new int[100];        
        Arrays.fill(this.memo, -1);
        return this.robFrom(0, nums);
    }
    
    private int robFrom(int i, int[] nums) {
        if (i >= nums.length) {
            return 0;
        }
        if (this.memo[i] > -1) {
            return this.memo[i];
        }
        int ans = Math.max(this.robFrom(i + 1, nums), this.robFrom(i + 2, nums) + nums[i]);
        this.memo[i] = ans;
        return ans;
    }
}