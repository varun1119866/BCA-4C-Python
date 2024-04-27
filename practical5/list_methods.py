# Creating a list
my_list = [10, 20, 30, 40, 50]

# Append method
my_list.append(60)
print("List after append:", my_list)

# Extend method
my_list.extend([70, 80, 90])
print("List after extend:", my_list)

# Insert method
my_list.insert(2, 15)
print("List after insert:", my_list)

# Remove method
my_list.remove(20)
print("List after remove:", my_list)

# Pop method
popped_element = my_list.pop(3)
print("Popped element:", popped_element)
print("List after pop:", my_list)

# Clear method
my_list.clear()
print("List after clear:", my_list)
