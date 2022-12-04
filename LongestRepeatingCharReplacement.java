// https://leetcode.com/problems/longest-repeating-character-replacement/
/*
Approach -
end-start+1 = size of the current window, maxCount = largest count of a unique char in the current window
When end-start+1-maxCount == 0, then then the window is filled with only one character
When end-start+1-maxCount > 0, then we have characters in the window that are not the char that occurs the most.
end-start+1-maxCount is equal to exactly the # of characters that are NOTnot the char that occurs the most in that window.
We are allowed to have at most k replacements in the window, so when end-start+1-maxCount > k, 
then there are more characters in the window than we can replace, and we need to shrink the window.
*/
class Solution {
     public int characterReplacement(String s, int k) {
        int len = s.length();
        int[] count = new int[26];
        int start = 0, maxCount = 0, maxLength = 0;
        for (int end = 0; end < len; end++) {
            maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
            if (end - start + 1 - maxCount > k) {
                count[s.charAt(start) - 'A']--;
                start++;
            }
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}