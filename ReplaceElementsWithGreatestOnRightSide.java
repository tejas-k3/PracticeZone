// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side
class Solution {
    public int[] replaceElements(int[] arr) {
        int temp = -1, temp2 ;
        for(int i = arr.length-1; i>=0; i--) {
            temp2 = arr[i];
            arr[i] = temp;
            if (temp2 > temp) temp = temp2;
        }
    return arr;
    }
}