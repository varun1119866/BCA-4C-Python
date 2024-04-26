# Define a list
my_list = [3, 7, 1, 4, 2]

# Display the original list
print("Original list:", my_list)

# Append an element to the list
my_list.append(5)
print("List after appending 5:", my_list)

# Remove an element from the list
my_list.remove(7)
print("List after removing 7:", my_list)

# Insert an element at a specific position
my_list.insert(2, 10)
print("List after inserting 10 at index 2:", my_list)

# Sort the list
my_list.sort()
print("Sorted list:", my_list)

# Reverse the list
my_list.reverse()
print("Reversed list:", my_list)

# Get the length of the list
print("Length of the list:", len(my_list))

# Find the index of an element
index = my_list.index(4)
print("Index of 4:", index)

# Count the occurrences of an element
count = my_list.count(4)
print("Count of 4:", count)

# Remove the last element from the list and return it
last_element = my_list.pop()
print("Last element removed from the list:", last_element)
print("List after removing the last element:", my_list)
