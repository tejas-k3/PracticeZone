// https://leetcode.com/problems/permutations/
/*
Approach -
Backtracking solution, start from 0, and represent the depth of the search
track what items are  in the partial solution from the set of n the current
partial solution collect all the valide solutions
*/

import java.util.*;

class Solution {
    public void backtrack(int n, ArrayList<Integer> nums, List<List<Integer>> output, int first) {
      if (first == n)
        output.add(new ArrayList<Integer>(nums));
      for (int i = first; i < n; i++) {
        // place i-th integer first in the current permutation
        Collections.swap(nums, first, i);
        backtrack(n, nums, output, first + 1);
        // backtrack
        Collections.swap(nums, first, i);
      }
    }
  
    public List<List<Integer>> permute(int[] nums) {
      List<List<Integer>> output = new LinkedList();
      ArrayList<Integer> nums_lst = new ArrayList<Integer>();
      for (int num : nums)
        nums_lst.add(num);
  
      int n = nums.length;
      backtrack(n, nums_lst, output, 0);
      return output;
    }
  }