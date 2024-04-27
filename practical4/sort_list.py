size = int(input("Enter the size of the list: "))
my_list = []

print("Enter", size, "elements:")
for _ in range(size):
    my_list.append(int(input()))

print("List before sorting:", my_list)
my_list.sort()
print("List after sorting:", my_list)
