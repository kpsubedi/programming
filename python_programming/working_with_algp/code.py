
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
