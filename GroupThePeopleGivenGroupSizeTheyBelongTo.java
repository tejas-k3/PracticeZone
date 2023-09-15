// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> ans = new ArrayList<>();
        Map<Integer, List<Integer>> szToGroup = new HashMap<>();
        for (int i = 0; i < groupSizes.length; i++) {
            if (!szToGroup.containsKey(groupSizes[i])) {
                szToGroup.put(groupSizes[i], new ArrayList<>());
            }
            List<Integer> group = szToGroup.get(groupSizes[i]);
            group.add(i);
            if (group.size() == groupSizes[i]) {
                ans.add(group);
                szToGroup.remove(groupSizes[i]);
            }
        }
        return ans;
    }
}