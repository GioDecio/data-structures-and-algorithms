class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_tree(self):
        # Print the tree in a pre-order traversal
        print(self.value, end=' ')
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

def construct_tree(preorder, inorder):

    if not preorder or not inorder:
        return None
    
    root = Node(preorder[0])
    root_idx = inorder.index(root.value)
    root.left = construct_tree(preorder[1:root_idx+1], inorder[:root_idx])
    root.right = construct_tree(preorder[root_idx+1:], inorder[root_idx+1:])

    return root


preorder = [3,9,1,2,20,15,7]
inorder = [1,9,2,3,15,20,7]

root = construct_tree(preorder, inorder)
root.print_tree()