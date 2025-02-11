"""
Given a binary search tree, find the kth smallest element in the tree. 
For example, if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.
The solution to this problem usually involves traversing the tree in-order (left, root, right) and 
keeping track of the number of nodes visited until you find the kth smallest element. 
There are two main approaches to doing this:

Iterative approach using a stack: This approach involves maintaining a stack of nodes that still need to be visited, 
starting with the leftmost node. At each step, you pop a node off the stack, decrement the kth smallest counter, 
and check whether you have found the kth smallest element. 
If you have not, you continue traversing the tree by moving to the right child of the current node.

Recursive approach: This approach involves recursively traversing the tree in-order and keeping track of the number of 
nodes visited until you find the kth smallest element. 
You can use a helper function that takes a node and a value of k as input, 
and recursively calls itself on the left and right children of the node until it finds the kth smallest element.

Both of these approaches have their own advantages and disadvantages, 
and the best approach to use may depend on the specific problem constraints and the interviewer's preferences.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # WRITE KTH_SMALLEST METHOD HERE #
    def kth_smallest(self, value):
        if self.root==None or value <=0:
            return None 
        results = []
        def _find_kth(node):
            if len(results) >= value:  # Early stopping condition
                return
            if node.left:
                _find_kth(node.left)
            results.append(node.value)
            if node.right:
                _find_kth(node.right)
        _find_kth(self.root)
        if value > len(results):
            return None
        return results[value-1]

            
            
            

bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(8))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """