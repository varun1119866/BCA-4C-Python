print("NAME : YUVRAJ SINGH \n ROLL NO : 2201997282")
# Define the list
my_list = ['q', 'w', 'e', 'r', 't', 'y']

# Iterate over the elements of the list
for i, elem in enumerate(my_list):
    # Print the element and its positive and negative indexes
    print("Element", elem, "at positive index ",i ,"and negative index ",-len(my_list) + i)
