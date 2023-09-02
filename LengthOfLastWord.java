// https://leetcode.com/problems/length-of-last-word/
class Solution {
    public int lengthOfLastWord(String s) {
        int lastCharIndex = s.length(), sLen = s.length();
        boolean firstChar = false;
        for (int i = sLen-1; i>=0; i--) {
            char c = s.charAt(i);
            if (c != ' ') {
                firstChar = true;
                lastCharIndex = i;
            }
            while(firstChar) {
                i--;
                if (i < 0) return lastCharIndex - i;;
                c = s.charAt(i);
                if (c == ' ') {
                    return lastCharIndex - i;
                }
            }
        }
        return sLen;
    }
}