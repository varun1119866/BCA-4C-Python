# Input the size of the list
size = int(input("Enter the size of the list: "))

# Initialize an empty list
my_list = []

# Input elements for the list
print("Enter", size, "elements:")
for _ in range(size):
    element = int(input())
    my_list.append(element)

# Display the list before sorting
print("List before sorting:", my_list)

# Sort the list in ascending order
my_list.sort()

# Display the list after sorting
print("List after sorting:", my_list)
