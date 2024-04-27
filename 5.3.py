def list_methods_demo():
   
    my_list = [3, 1, 4, 1, 5, 9]

   
    print("Original list:", my_list)
    my_list.append(2)
    print("List after appending 2:", my_list)

  
    my_list.insert(2, 6)
    print("List after inserting 6 at index 2:", my_list)

   
    my_list.remove(1)
    print("List after removing the first occurrence of 1:", my_list)

   
    popped_element = my_list.pop()
    print("Popped element from the list:", popped_element)
    print("List after popping the last element:", my_list)

 
    index_of_4 = my_list.index(4)
    print("Index of 4:", index_of_4)

  
    count_of_1 = my_list.count(1)
    print("Count of 1:", count_of_1)

    my_list.sort()
    print("Sorted list:", my_list)

  
    my_list.reverse()
    print("Reversed list:", my_list)

   
    my_list.clear()
    print("List after clearing:", my_list)

def main():
    list_methods_demo()

if __name__ == "__main__":
    main()
