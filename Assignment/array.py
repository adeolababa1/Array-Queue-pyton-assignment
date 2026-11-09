
# Array Operations in Python

numbers = [40, 10, 30, 20, 50]

# A. Search
print("A. SEARCH")
search_value = 30

if search_value in numbers:
    print(search_value, "was found in the array")
else:
    print(search_value, "was not found")

# B. Sort
print("\nB. SORT")
numbers.sort()
print("Sorted array:", numbers)

# C. List
print("\nC. LIST")
print("Elements in the array:", numbers)

# D. Traverse
print("\nD. TRAVERSE")
for item in numbers:
    print(item)

# E. Insert
print("\nE. INSERT")
numbers.insert(2, 25)
print("Array after insertion:", numbers)
