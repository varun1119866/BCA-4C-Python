def main():
    
    my_list = [1, 2, 3, 4, 5]

    
    print("Original list:", my_list)

    
    print("First element:", my_list[0])
    print("Second element:", my_list[1])
    print("Last element:", my_list[-1])

    print("Sliced list:", my_list[1:4])

    
    my_list[2] = 10
    print("Modified list:", my_list)


    my_list.append(6)
    print("List after appending 6:", my_list)


    my_list.insert(2, 7)
    print("List after inserting 7 at index 2:", my_list)

    
    my_list.remove(4)
    print("List after removing 4:", my_list)


    last_element = my_list.pop()
    print("List after popping last element (", last_element, "):", my_list)

    
    index_of_3 = my_list.index(3)
    print("Index of 3:", index_of_3)

   
    count_of_5 = my_list.count(5)
    print("Count of 5:", count_of_5)

   
    my_list.reverse()
    print("Reversed list:", my_list)

    my_list.sort()
    print("Sorted list:", my_list)

if __name__ == "__main__":
    main()
