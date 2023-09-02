// https://leetcode.com/problems/is-subsequence
class Solution {
    public boolean isSubsequence(String s, String t) {
        int sLen = s.length(), tLen = t.length();
        if (sLen > tLen) return false;
        for(int i=0, j=0;i<sLen;)
        {
            if (j == tLen && i != sLen) return false;
            if(s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        return true;
    }
}