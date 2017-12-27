
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
# Binary Search template file
#######################################
from time import time

def contains(collection, target):
    """" Determine whether collection contains target."""
    return target in collection

def bs_contains(ordered, target):
    """ Use binary array search to return index position of target in collection"""

    low = 0
    high = len(ordered) - 1
    while low <= high:
        mid = (low+high)/2
        if target == ordered[mid]:
            return mid
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -(low + 1)

def insert_in_place(ordered, target):
    """Inserts target into it proper location"""
    idx = bs_contains(ordered, target)
    if idx < 0:
        ordered.insert(-(idx+1), target)
        return
    ordered.append(idx, target)

def performance():
    """ Demonstrate execution performance of contains"""
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()
        # Code whose performance is to be evaluated
        #bs_contains(sorted, -1)
        insert_in_place(sorted, n+1)
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
        
        
        
####Binary Search Tree with remove node feature####
###################################################
# Binary Search Tree Implementation name of the file: bst_demo.py 
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
    def delete(self):
        """
        Remove value of self from BinaryTree. Works in conjunction
        with remove method in BinaryTree.
        """
        if self.left == self.right == None:
            return None
        if self.left == None:
            return self.right
        if self.right == None:
            return self.left
        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value
        return self    

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

    def remove(self, value):
        """Remove value from tree."""
        if self.root:
            self.root = self.remove_from_parent(self.root, value)
            
    def remove_from_parent(self, parent, value):
        """Remove value from tree rooted at parent"""
        if parent is None:
            return None
        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.remove_from_parent(parent.left, value)
        else:
            parent.right = self.remove_from_parent(parent.right, value)

        return parent    

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
############################################################
### Building Balanced Search Tree from sorted collection ###
############################################################
#!/usr/bin/env python3

from bst_demo import BinaryTree


def balanced_tree(ordered):
    """ Create balanced binary tree from ordered collection"""
    bt = BinaryTree()

    add_range(bt, ordered, 0, len(ordered)-1)
    return bt

def add_range(bt, ordered, low, high):
    """Add range to the bt in way that bt remains balanced"""
    if low <= high:
        mid = (low+high)//2
        bt.add(ordered[mid])
        add_range(bt, ordered, low, mid-1)
        add_range(bt, ordered, mid+1, high)
#####################################################
#!/usr/bin/env python3
import random
import time

def get_performance_sort():
    """Get performance"""
    scores = {}
    trial = 1
    while trial <= 16:
        numbers = [random.randint(1,9) for i in range(2**trial)]
        now = time.clock()
        numbers.sort()
        done = time.clock()
        scores[trial] = (done-now)
        trial = trial + 1
    for i in scores:
        print("%d\t%f" %(2**i,scores[i]))
        
     
def get_performance_sum():
    """Calculating """
    scores = {}
    trial = 1
    while trial <= 16:
        numbers = [random.randint(1,9) for i in range(2**trial)]
        now = time.clock()
        sum = 0
        for d in numbers:
            sum = sum + d
        done = time.clock()
        scores[trial] = (done-now)
        trial = trial + 1
    for i in scores:
        print("%d\t%f" %(2**i,scores[i]))
    
##############################
