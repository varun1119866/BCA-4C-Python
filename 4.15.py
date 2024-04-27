def create_sorted_list(size):
    
    my_list = []
    print("Enter", size, "numbers:")
    for i in range(size):
        num = int(input("Enter number {}: ".format(i + 1)))
        my_list.append(num)
    
    
    sorted_list = sorted(my_list)
    
    return my_list, sorted_list

def main():
    size = int(input("Enter the size of the list: "))
    
 
    original_list, sorted_list = create_sorted_list(size)
    
    
    print("\nOriginal list before sorting:", original_list)
    print("Sorted list in ascending order:", sorted_list)

if __name__ == "__main__":
    main()
