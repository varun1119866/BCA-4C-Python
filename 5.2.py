# Define the list
my_list = ['q', 'w', 'e', 'r', 't', 'y']

# Print elements of the list along with their indexes
print("Elements of the list along with their indexes:")
for i in range(len(my_list)):
    print("Element:", my_list[i])
    print("Positive Index:", i)
    print("Negative Index:", i - len(my_list))
    print()  # Add a blank line for separation
