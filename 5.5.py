def list_functions_demo():
    
    my_list = [3, 1, 4, 1, 5, 9]

   
    print("Length of the list:", len(my_list))

    print("Maximum value in the list:", max(my_list))

  
    print("Minimum value in the list:", min(my_list))

   
    print("Sum of all elements in the list:", sum(my_list))

    sorted_list = sorted(my_list)
    print("Sorted list:", sorted_list)

  
    my_list.reverse()
    print("Reversed list:", my_list)

def main():
    list_functions_demo()

if __name__ == "__main__":
    main()
