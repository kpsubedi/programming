
################################################
# Binary Search template file
from time import time

def contains(collection, target):
    """" Determine whether collection contains target."""
    return target in collection

def bs_contains(ordered, target):
    """ Use binary array search to determine if target is in collection"""

    low = 0
    high = len(ordered) - 1
    while low <= high:
        mid = (low+high)/2
        if target == ordered[mid]:
            return True
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False   
def performance():
    """ Demonstrate execution performance of contains"""
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()
        # Code whose performance is to be evaluated
        # contains(sorted, -1)
        bs_contains(sorted, -1)
        done = time()
        print(n, (done-now)*1000)
        n = n * 2

performance()
#######################################
####Binary Search Tree#################
# Binary Search Tree Implementation
class BinaryNode:

    def __init__(self, value = None):
        """Create binary node"""
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, val):
        """Adds a new node to the tree containing this value"""
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)


class BinaryTree:
    
    def __init__(self):
        "Create empty binary tree"""
        self.root = None

    def add(self, value):
        """Insert value into proper location in Binary tree"""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)        
    
    def contains(self, target):
        """Check whether BST contains target value"""
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False 

import random
from time import time

def performance():
    """Demonstrate execution performance"""
    n = 1024
    while n <= 65536:
        bt = BinaryTree()
        for i in range(n):
            bt.add(random.randint(1,n))
        now = time()
        bt.contains(random.randint(1,n))
        print ("%d, %f" % (n, (time() - now)*1000))
        n = n * 2
        
        
        
