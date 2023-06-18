// https://leetcode.com/problems/decode-ways/
// 1D DP Recursive sol
class Solution {
    Map<Integer, Integer> memo = new HashMap<>();
    public int numDecodings(String s) {
        return recursiveWithMemo(0, s);
    }
    private int recursiveWithMemo(int index, String str) {
        // Have we already seen this substring?
        if (memo.containsKey(index)) {
            return memo.get(index);
        }
        // If you reach the end of the string
        // Return 1 for success.
        if (index == str.length()) {
            return 1;
        }
        // If the string starts with a zero, it can't be decoded
        if (str.charAt(index) == '0') {
            return 0;
        }
        if (index == str.length() - 1) {
            return 1;
        }
        int ans = recursiveWithMemo(index + 1, str);
        if (Integer.parseInt(str.substring(index, index + 2)) <= 26) {
             ans += recursiveWithMemo(index + 2, str);
         }
        memo.put(index, ans);
        return ans;
    }
}