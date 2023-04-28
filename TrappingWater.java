/* https://leetcode.com/problems/trapping-rain-water
 *  Approach : First, we need to find the highest bar in the elevation map. This will be the maximum height of any water that can be trapped. We can use a loop to find the maximum height.
 * Next, we need to iterate over each level from 1 to the maximum height, and calculate the amount of water that can be trapped at that level. We can use another loop for this
 * Inside the loop, we initialize two pointers left and right at the beginning and end of the elevation map, respectively. We also initialize two variables leftMax and rightMax to track the maximum height of bars seen so far from the left and right sides, respectively. We then use a while loop to iterate over the elevation map until left and right meet.
 * At each iteration of the loop, we check if the height of the bar at the current left or right position is less than or equal to the current level. If it is, we update the corresponding leftMax or rightMax variable with the maximum height seen so far.
 * If the height of the bar at the current left position is greater than the current level, and the height of the bar at the current right position is also greater than the current level, we have found a container that can hold water. We calculate the amount of water that can be held in the container as the difference between the minimum of leftMax and rightMax (i.e., the height of the container walls) and the current level. We add this value to the totalWater variable, and break out of the loop since we have found the maximum amount of water that can be held at the current level.
 */
class Solution {
    public int trap(int[] height) {
    int n = height.length;
    if (n == 0) {
        return 0;
    }

    int[] leftMax = new int[n];
    int[] rightMax = new int[n];

    leftMax[0] = height[0];
    for (int i = 1; i < n; i++) {
        leftMax[i] = Math.max(leftMax[i - 1], height[i]);
    }

    rightMax[n - 1] = height[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        rightMax[i] = Math.max(rightMax[i + 1], height[i]);
    }

    int trappedWater = 0;
    for (int i = 0; i < n; i++) {
        int minHeight = Math.min(leftMax[i], rightMax[i]);
        trappedWater += minHeight - height[i];
    }

    return trappedWater;
    }
}