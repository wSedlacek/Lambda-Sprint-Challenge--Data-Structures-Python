from typing import List, Optional, Union
import time
import os


start_time = time.time()
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


f = open(os.path.join(THIS_FOLDER, 'names_1.txt'), 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(os.path.join(THIS_FOLDER, './names_2.txt'), 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# O(n ** 2) (nested loop)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


class BinarySearchTree:
    def __init__(self, value: Union[int, str]):
        self.value = value
        self.left: Optional["BinarySearchTree"] = None
        self.right: Optional["BinarySearchTree"] = None

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    # O(log n), Binary Insert
    def insert(self, value: Union[int, str]):
        """Insert the given value into the tree"""

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # O(log n), Binary Search
    def contains(self, target: Union[int, str]):
        """Return True if the tree contains the value
        False if it does not"""
        if self.value == target:
            return True
        elif self.value < target and self.right:
            return self.right.contains(target)
        elif self.value >= target and self.left:
            return self.left.contains(target)
        else:
            return False


search_tree = BinarySearchTree(names_1[0])

# O(n log n), loop with binary insert
for i in range(1, len(names_1)):
    search_tree.insert(names_1[i])

# O(n log n), loop with binary search
for name_2 in names_2:
    if search_tree.contains(name_2):
        duplicates.append(name_2)


# Scaling: O(n log n)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# I believe O(n log n) is the fastest that can be accomplished, it runs in less then 1 second
# so I don't see a reason to go any faster.
