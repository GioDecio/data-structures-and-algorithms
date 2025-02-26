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

def construct_tree(postorder, inorder):

    if not postorder or not inorder:
        return None
    
    root = Node(postorder[-1])
    root_idx = inorder.index(root.value)
    root.left = construct_tree(postorder[:root_idx], inorder[:root_idx])
    root.right = construct_tree(postorder[root_idx:-1], inorder[root_idx+1:])

    return root


postorder = [1,2,9,15,7,20,3]
inorder = [1,9,2,3,15,20,7]

root = construct_tree(postorder, inorder)
root.print_tree()