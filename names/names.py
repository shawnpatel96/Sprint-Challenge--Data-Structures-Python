import time
from binarySearchTree import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

bst= BinarySearchTree(None)
for name in names_1:
    if bst.value == None:
        bst.value = name
    else:
        bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)    

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


start_time_2 = time.time()

duplicates_2 = []
# by defintion set only allows unique elements 
seen = set()
names = names_1 + names_2
for name in names:
    if name not in seen:
        seen.add(name)
    else:
        duplicates_2.append(name)

end_time_2 = time.time()
print (f"{len(duplicates_2)} duplicates:\n\n{', '.join(duplicates_2)}\n\n")
print (f"runtime: {end_time_2 - start_time_2} seconds")