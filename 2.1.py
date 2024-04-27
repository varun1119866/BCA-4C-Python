def demonstrate_slicing(string):
    print("Original String:", string)

   
    print("Slice 1:", string[2:6])

  
    print("Slice 2:", string[:6])

   
    print("Slice 3:", string[3:])

    
    print("Slice 4:", string[-4:])

    
    print("Slice 5:", string[::2])

    print("Slice 6:", string[::-1])


def main():
    string = input("Enter a string: ")
    demonstrate_slicing(string)

if __name__ == "__main__":
    main()
