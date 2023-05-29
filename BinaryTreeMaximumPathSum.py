# https://leetcode.com/problems/binary-tree-maximum-path-sum
# Wont work for all negative values
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float('inf')
        # post order traversal of subtree rooted at `node`
        def gainFromSubtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath
            if not node:
                return 0
            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            gainFromLeft = max(gainFromSubtree(node.left), 0)
            # add the gain / path sum from right subtree. 0 if negative
            gainFromRight = max(gainFromSubtree(node.right), 0)
            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)
            # return the max sum for a path starting at the root of subtree
            return max(
                gainFromLeft + node.val,
                gainFromRight + node.val
            )
        gainFromSubtree(root)
        return maxPath