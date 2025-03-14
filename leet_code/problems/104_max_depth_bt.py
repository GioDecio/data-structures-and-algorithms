"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        max_depth = max(l_depth, r_depth) + 1

        return max_depth
