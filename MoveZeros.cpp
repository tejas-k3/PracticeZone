/* https://leetcode.com/problems/move-zeroes/
Approach -
In-place swapping of elements is done by checking
for 0 value element and next non-zero element with a loop
and after swapping the indexs are incremented.
*/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
     for(int i=0,j=1;i<=j;)
        {
         if(i+1>=nums.size())
             return;
            if(nums[i]==0)
            {
                j=i+1;
                while(nums[j]==0)
                {
                    j++;
                    if(j>=nums.size())
                        return;
                }
                swap(nums[i], nums[j]);
            }
                j++;
                i++;
                if(i>=nums.size()-1||j>=nums.size())
                        return;
        }
        return;  
    }
};