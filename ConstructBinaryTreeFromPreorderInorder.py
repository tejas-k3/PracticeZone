# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# This PROBLEM IS MEDIUM WTF! 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def arrayToTree(left, right):
            nonlocal preorderIndex
            if left > right: return None
            # select the preorderIndex element as the root and increment it
            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue)
            preorderIndex += 1
            # build left and right subtree excluding    
            # inorderIndexMap[rootValue] element because it's the root
            root.left = arrayToTree(left, inorderIndexMap[rootValue] - 1)
            root.right = arrayToTree(inorderIndexMap[rootValue] + 1, right)
            return root
        preorderIndex = 0
        # build a hashmap to store value -> its index relations
        inorderIndexMap = {}
        for index, value in enumerate(inorder):
            inorderIndexMap[value] = index
        return arrayToTree(0, len(preorder) - 1)