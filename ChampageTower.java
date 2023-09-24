// https://leetcode.com/problems/champagne-tower/
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        if (poured == 0) {
            return 0;
        }
        double[] cup_level = new double[101];
        cup_level[0] = poured;
        for (int row = 0; row < query_row; row++) {
            for (int col = row; col >= 0; col--) {
                if (cup_level[col] > 1) {
                    // if current glass holds more than 1 cup of content
                    // we need to split the surplus with the left and right glass below.
                    double spill = (cup_level[col] - 1) / 2;
                    cup_level[col+1] += spill;
                    cup_level[col] = spill;
                } else {
                    // No spill
                    cup_level[col] = 0;
                }
            }
        }

        return Math.min(1, cup_level[query_glass]);
    }
}