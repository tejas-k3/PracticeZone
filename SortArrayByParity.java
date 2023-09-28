// https://leetcode.com/problems/sort-array-by-parity
class Solution {
    public int[] sortArrayByParity(int[] nums) {
        for (int i = 0, j = 0; j < nums.length; j++)
            if (nums[j] % 2 == 0) {
                int tmp = nums[i];
                nums[i++] = nums[j];
                nums[j] = tmp;;
            }
        return nums;
    }
}