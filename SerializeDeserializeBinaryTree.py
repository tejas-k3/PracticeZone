# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q, res = collections.deque([root]), []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
                
        return ' '.join(res)  

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == '#':
            return
        vals = iter(data.split())
        root = TreeNode(int(next(vals)))
        q = collections.deque([root])
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                l, r = next(vals), next(vals)
                node.left = None if l == '#' else TreeNode(int(l))
                if node.left:
                    q.append(node.left)
                node.right = None if r == '#' else TreeNode(int(r))
                if node.right:
                    q.append(node.right)
        return root 

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))