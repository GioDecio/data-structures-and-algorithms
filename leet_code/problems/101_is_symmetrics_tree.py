def isSymmetric(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    if not root:
        return True

    if root and not root.left and not root.right:
        return True

    def checker(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val == right.val:
            return True
        else:
            checker(left.left, right.left)
            checker(right.left, right.right)

    return self.isSymmetric(root.left) and self.isSymmetric(root.right)
