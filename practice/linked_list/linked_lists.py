# A node is a pointer and a value, you can think of it as a dictionary
# So you can think of a LL as a nested dict
from functools import wraps

def print_list_after(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print("\nList after", func.__name__ + ":")
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
        print(f"Return value from {func.__name__}: {result}")  # Add this line to debug
        return result
    return wrapper

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    @print_list_after
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    @print_list_after
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    @print_list_after
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head= new_node
        self.length += 1
        return True
    

    @print_list_after
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -=1
        if self.length == 0:
            self.tail = None
        temp.next = None
        return temp

    @print_list_after
    def get(self, index):
        if index >= self.length or index < 0 :
            return None
        temp = self.head  
        for _ in range(index):
            temp = temp.next
        return temp.value
            






    
linked_list = LinkedList(1)
linked_list.append(5)
linked_list.append([1,2,3,4,6])
linked_list.prepend(40)
linked_list.pop()
linked_list.pop_first()
linked_list.get(20)
