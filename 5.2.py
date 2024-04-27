def print_with_indexes(my_list):
    for i, elem in enumerate(my_list):
        print("Element:", elem)
        print("Positive Index:", i)
        print("Negative Index:", i - len(my_list))
        print()

def main():
    my_list = ['q', 'w', 'e', 'r', 't', 'y']
    print("Printing elements of the list along with their indexes:")
    print_with_indexes(my_list)

if __name__ == "__main__":
    main()
