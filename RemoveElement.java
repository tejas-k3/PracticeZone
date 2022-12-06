/* https://leetcode.com/problems/remove-element/description/
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
Approach -
Iterate through the array and if value is present, replace it with next element 
condition says the relative order of the elements may be changed. Return final
length of resultant array.

 */
class Solution {
    public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
}