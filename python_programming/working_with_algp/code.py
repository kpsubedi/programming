
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
# Divide and Conquer Algo
##############################
# MergeSort Implementation

def copy_merge_sort(A):
    """MergeSort of A and return a new collection"""
    if len(A) < 2:
        return A
    mid = len(A)//2
    left = copy_merge_sort(A[:mid])
    right = copy_merge_sort(A[mid:])
    
    i = j = 0
    B = []

    while len(B) < len(A):
        if j >= len(right) or (i < mid and left[i] < right[j]):
            B.append(left[i])
            i = i + 1
        elif j < len(right):
            B.append(right[j])
            j = j + 1
     

    return B   


def merge_sort(A):
    """Merge Sort A in Place"""
    copy = list(A)
    merge_sort_array(copy, A, 0, len(A))


def merge_sort_array(A, result, start, end):
    """Mergesort array in memory with given range"""
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start+1]:
            result[start], result[start+1] = result[start+1], result[start]
        return

    mid = (end + start)//2
    merge_sort_array(result, A, start, mid)
    merge_sort_array(result, A, mid, end)

    # merge is now ready. Merge from A back into result
    i = start
    j = mid
    idx = start
    while idx < end:
        if j >= end or (i < mid and A[i] < A[j]):
            result[idx] = A[i]
            i = i + 1
        else:
           result[idx] = A[j]
           j = j + 1
        idx = idx + 1
#####
#### NUMPY #################
### $ pip3.6 install numpy #
############################
>>> m = random_matrix(2)
>>> m
array([[ 0.87785047,  0.24979643],
       [ 0.27465185,  0.05808083]])
>>> m.dot(m)
array([[ 0.8392285 ,  0.2337923 ],
       [ 0.25705527,  0.07198043]])
>>> numpy.identity(6)
array([[ 1.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  1.]])
>>> 
# Mathematical Algorithms
from time import time

def exponent(x, n):
    """Returns the value of x raised nth power"""
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2:
        return x * exponent(x*x, (n-1)//2)
    return exponent(x*x, n//2)

def exponent_mod(x, n, m):
    """Returns the value of x raised nth power"""
    if n == 0:
        return 1
    if n == 1:
        return x % m
    if n % 2:
        return x * exponent_mod(x*x % m, (n-1)//2, m) % m
    return exponent_mod(x*x, n//2, m) % m


def compare_trials(trials):
    """Compare performance on a number of runs"""
    base = 999
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent(base, t)
        timeR = timeR + (time() - now)

        now = time()
        check2 = base ** t
        #for i in range(t):
        #    check2 = check2 * base
        timeN = timeN + (time() - now)

        if check1 != check2:
            raise Exception ("Invalid Result")
    return (timeR, timeN)


def compare_trials_mod(trials):
    """Compare performance on a number of runs"""
    base = 999
    mod = 17
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent_mod(base, t, mod)
        timeR = timeR + (time() - now)

        now = time()
        check2 = pow(base, t, mod)
        #for i in range(t):
        #    check2 = check2 * base
        timeN = timeN + (time() - now)

        if check1 != check2:
            raise Exception ("Invalid Result")
    return (timeR, timeN)

def trial_table():
    """Output table of results for comparison"""
    trial = 2
    while trial <= 2048:
        #result = compare_trials(trial)
        result = compare_trials_mod(trial)
        print("%d\t%f\t%f" %(trial, result[0], result[1]))
        trial = trial * 2
        
import numpy
import random

def random_matrix(n):
    """Return a random nxn Matrix"""
    r = []
    for i in range(n):
        r.append([random.random() for i in range(n)])
    base = numpy.array(r).reshape(n,n)
    return base

def exponent_mat(x, n):
    """Returns the value of x raised nth power"""
    if n == 0:
        return numpy.identity(len(x))
    if n == 1:
        return x
    if n % 2:
        return x.dot(exponent_mat (x.dot(x), (n-1)//2))
    return exponent_mat(x.dot(x), n//2)

def compare_trials_mod_mat(trials, size):
    """Compare performance on a number of runs"""
    base = random_matrix(size)
    mod = 17
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent_mat(base, t)
        timeR = timeR + (time() - now)

        now = time()
        check2 = numpy.identity(len(base))
        for i in range(t):
            check2 = check2.dot(base)
        timeN = timeN + (time() - now)

    return (timeR, timeN)

def trial_table_mat():
    """Output table of results for comparison"""
    trial = 2
    size = 33
    while trial <= 512: 
        result = compare_trials_mod_mat(trial, size)
        print("%d\t%f\t%f" %(trial, result[0], result[1]))
        trial = trial * 2
##################
# Mathematical Algorithms
from time import time
def exponent(x, n):
    """Returns the value of x raised nth power"""
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2:
        return x * exponent(x*x, (n-1)//2)
    return exponent(x*x, n//2)
def exponent_nore(x, n):
    """Non-recursive implementation of exponentiation"""
    if n == 0:
        return 1
    if n == 1:
        return x
    val = 1
    while n > 0:
        if n % 2:
            val = val * x
            n = n -1
        n = n // 2
        if n > 0:
            x = x * x
    return val

def compare_trials_nonr(trials):
    """Compare performance on a number of runs"""
    base = 999
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent(base, t)
        timeR = timeR + (time() - now)

        now = time()
        check2 = exponent_nore(base, t)
        timeN = timeN + (time() - now)

        if check1 != check2:
            raise Exception ("Invalid Result")
    return (timeR, timeN)

def trial_table_nonr():
    """Output table of results for comparing nonr vs recursive"""
    trial = 2
    while trial <= 2048:
        result = compare_trials_nonr(trial)
        print("%d\t%f\t%f" %(trial, result[0], result[1]))
        trial = trial * 2
        

        
def exponent_mod(x, n, m):
    """Returns the value of x raised nth power"""
    if n == 0:
        return 1
    if n == 1:
        return x % m
    if n % 2:
        return x * exponent_mod(x*x % m, (n-1)//2, m) % m
    return exponent_mod(x*x, n//2, m) % m


def compare_trials(trials):
    """Compare performance on a number of runs"""
    base = 999
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent(base, t)
        timeR = timeR + (time() - now)

        now = time()
        check2 = base ** t
        #for i in range(t):
        #    check2 = check2 * base
        timeN = timeN + (time() - now)

        if check1 != check2:
            raise Exception ("Invalid Result")
    return (timeR, timeN)


def compare_trials_mod(trials):
    """Compare performance on a number of runs"""
    base = 999
    mod = 17
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent_mod(base, t, mod)
        timeR = timeR + (time() - now)

        now = time()
        check2 = pow(base, t, mod)
        #for i in range(t):
        #    check2 = check2 * base
        timeN = timeN + (time() - now)

        if check1 != check2:
            raise Exception ("Invalid Result")
    return (timeR, timeN)

def trial_table():
    """Output table of results for comparison"""
    trial = 2
    while trial <= 2048:
        #result = compare_trials(trial)
        result = compare_trials_mod(trial)
        print("%d\t%f\t%f" %(trial, result[0], result[1]))
        trial = trial * 2
        
import numpy
import random

def random_matrix(n):
    """Return a random nxn Matrix"""
    r = []
    for i in range(n):
        r.append([random.random() for i in range(n)])
    base = numpy.array(r).reshape(n,n)
    return base

def exponent_mat(x, n):
    """Returns the value of x raised nth power"""
    if n == 0:
        return numpy.identity(len(x))
    if n == 1:
        return x
    if n % 2:
        return x.dot(exponent_mat (x.dot(x), (n-1)//2))
    return exponent_mat(x.dot(x), n//2)

def compare_trials_mod_mat(trials, size):
    """Compare performance on a number of runs"""
    base = random_matrix(size)
    mod = 17
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent_mat(base, t)
        timeR = timeR + (time() - now)

        now = time()
        check2 = numpy.identity(len(base))
        for i in range(t):
            check2 = check2.dot(base)
        timeN = timeN + (time() - now)

    return (timeR, timeN)

def trial_table_mat():
    """Output table of results for comparison"""
    trial = 2
    size = 33
    while trial <= 512: 
        result = compare_trials_mod_mat(trial, size)
        print("%d\t%f\t%f" %(trial, result[0], result[1]))
        trial = trial * 2
#####################
# Mathematical Algorihtms Project

import random

large_prime = 622288097498926496141095869268883999563096063592498055290461


def is_prime(n, k=5):
    """Probabiliatically check whether number is prime"""
    
    for i in range(k):
        a = random.randint(1, n-1)
        val = pow(a, n-1, n)
        if val != 1:
            return False
    return True
###########################
## Peg Solitorie Problem ##
###########################
# Brute-force Algorithm
def initial(n, skip):
    """Construct triangle solitaire game with n*(n+1)/2 holes each filled with
    a peg except for a specific omitted value"""
    
    board = {}

    for c in range(0, 2*n, 2):
        d = 0
        for r in range((2*n-c)//2):
            board[(c+d,r)] = True
            d = d + 1
    if skip in board:        
        board[skip] = False        
    return board    

def solve(board, path):
    """Solve board and updates path to reflect sequence of moves"""
    
    if len(path) == len(board) - 2:
        return True
    for move in moves(board):
        path.append(move)
        make_move(board, move)

        if solve(board, path):
            return True
        undo_move(board, move)
        del path[-1]
    return False    
# note each is a delta (c, r)
directions = [ [+4, 0], [-4, 0], [+2, +2], [+2, -2], [-2, +2], [-2, -2]]
# move is a triple [ hole, deltac, deltar]
def moves(board):
    """Returns possible moves given board state"""
    m = []
    for hole in board:
        if board[hole]:
            for deltac, deltar in directions:
                mid = (hole[0] + deltac//2, hole[1] + deltar//2)
                end = (hole[0] + deltac, hole[1] + deltar)
                if mid in board and board[mid] and end in board and not board[end]:
                    m.append([hole, deltac, deltar])
                
    return m

def make_move(board, move):
    """Execute move on a board"""
    hole, deltac, deltar = move
    mid = (hole[0] + deltac//2, hole[1] + deltar//2)
    end = (hole[0] + deltac, hole[1] + deltar)
    board[hole] = False
    board[mid] = False
    board[end] = True
    
def undo_move(board, move):
    """Execute move on a board"""
    hole, deltac, deltar = move
    mid = (hole[0] + deltac//2, hole[1] + deltar//2)
    end = (hole[0] + deltac, hole[1] + deltar)
    board[end] = False
    board[mid] = True
    board[hole] = True    

def solve_specific(board):
    """Solve board and return path of moves"""
    path = []
    solve(board, path)
    for move in path:
        print(move)
        
###################
##
###################
>>> import math
>>> math.factorial(9)
362880
>>> math.factorial(16)
20922789888000
>>> 
####
# Magic Square Construction

board = []
used = []
magic_sum = [0]

def initialize(n):
    """Initila Board Setup"""
    del board[0:len(board)]
    del used[0:len(used)]
    for r in range(n):
        board.append([0 for c in range(n)])
    for d in range(n*n+1):
        used.append(False)
    magic_sum[0] = n*(n*n+1)//2

def output():
    """Output Board"""
    for row in board:
        for val in row:
            print("{:2d}".format(val)),
        print

def is_valid(n):
    """Determine if board is valid"""
    sum_d1 = sum_d2 = 0
    for i in range(n):
        sum_r = sum_c = 0
        sum_d1 = sum_d1 + board[i][i]
        sum_d2 = sum_d2 + board[i][n-i-1]

        for j in range(n):
            sum_r = sum_r + board[i][j]
            sum_c = sum_c + board[j][i]

        if sum_r != magic_sum[0] or sum_c != magic_sum[0]:
            return False
    return sum_d1 == magic_sum[0] and sum_d2 == magic_sum[0]

def solve(n, step=0):
    """Complete given step in magic squre board"""
    if step == n**2:
        return is_valid(n)
    for val in range(1, n**2+1):
        if not used[val]:
            used[val] = True
            board[step//n][step%n] = val
            if solve(n, step+1):
                return True
            board[step//n][step%n] = 0
            used[val] = False
    return False        
# Use this existing solution for 3x3 and it works great. Use for 4x4 and
# it takes several minutes to come back with the solution. This brute
# force technique is trying 16! = 20,922,789,888,000 possible solutions.
# This roughly is 5,765, 760 times more work than solving the 3x3. Can we
# find a way to do better? YES!
# Instead of blindly pursuing each recursive step, you can validate partial
# results before moving forward.
# Revise as shown:

def valid_upto(n, step):
    """Determine if valid so far"""
    for r in range(n):
        if step == (r+1)*n-1:
            return sum(board[r]) == magic_sum[0]
    for c in range(n):
        if step == n*(n-1)+c:
            total = 0
            for r in range(n):
                total = total + board[r][c]
            return total == magic_sum[0]
    return True

def solve_it(n, step=0):
    """Complete given step in magic square board"""
    if step == n**2:
        return is_valid(n)
    for val in range(1,n**2+1):
        if not used[val]:
            used[val] = True
            board[step//n][step%n] = val
            if valid_upto(n,step) and solve_it(n, step+1):
                return True
            board[step//n][step%n] = 0
            used[val] = False
    return False

# Note that this won't work for 5x5 since that is even more computationally
# expensive!
# KD-tree Implementation
max_value = 2147483647
min_value = -2147483648

HORIZONTAL = 0
VERTICAL   = 1

X_ = 0
Y_ = 1

class Region:
    """Represents region in Cartesian space"""
    def __init__(self, xmin, ymin, xmax, ymax):
        """Creates region from (xmin, ymin) to (xmax, ymax)"""
        self.x_min = xmin
        self.y_min = ymin
        self.x_max = xmax
        self.y_max = ymax

    def copy(self):
        """Return copy of region"""
        return Region(self.x_min, self.y_min, self.x_max, self.y_max)

# default maximum region
max_region = Region(min_value, min_value, max_value, max_value)

    
class KDNode:

    def __init__(self, pt, orient, region = max_region):
        """Create empty KDNode"""
        self.point = pt
        self.orient = orient
        self.above = None
        self.below = None
        self.region = region

    def create_child(self, pt, below):
        """Create child node (either above or below) given node with pt"""
        r = self.region.copy()
        if self.orient == VERTICAL:
            if below:
                r.x_max = self.point[X_]
            else:
                r.x_min = self.point[X_]
        else:
            if below:
                r.y_max = self.point[Y_]
            else:
                r.y_min = self.point[Y_]
        return KDNode(pt, 1-self.orient, r)        
            
    def is_below(self, pt):
        """Is point below current node"""
        if self.orient == VERTICAL:
            return pt[X_] < self.point[X_]
        return pt[Y_] < self.point[Y_]
    
        
        
            
    def add(self, pt):
        """Add point to the KDNode tree rooted at this node"""
        if self.point == pt:
            return
        if self.is_below(pt):
            if self.below:
                self.below.add(pt)
            else:
                self.below = self.create_child(pt, True)
        else:
            if self.above:
                self.above.add(pt)
            else:
                self.above = self.create_child(pt, False)
                
                
                
        
class KDTree:

    def __init__(self):
        """Create empty KD Tree"""
        self.root = None

    def add(self, pt):
        """Add Point to KD-tree"""

        if self.root:
            self.root.add(pt)
        else:
            self.root = KDNode(pt, VERTICAL)
            
 ####
