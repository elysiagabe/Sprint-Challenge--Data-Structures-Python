import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Turn names_1 into a binary search tree --> need to create/bring in class and import
# Instantiate instance of BSTNode
names_bst = BSTNode(names_1[0])

# Loop thru names_1 and append to BST instance
for name_1 in names_1[1:]:
    names_bst.insert(name_1)

# Check to see if any names from names_2 are in BST w/ "contains" method
for name_2 in names_2:
# if a dup is found, push to duplicates list
    if names_bst.contains(name_2):
        duplicates.append(name_2)
# ----------------> RUNTIME = 0.22 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

duplicates = list(set(names_1).intersection(set(names_2)))
# ----------------> RUNTIME = 0.017 seconds