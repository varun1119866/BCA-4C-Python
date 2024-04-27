def break_example():
    print("Break Example:")
    # Iterating through numbers from 1 to 10
    for i in range(1, 11):
        print(i, end=" ")
        if i == 5:
            print("\nEncountered 5, breaking loop...")
            break
    print("\nLoop ended.\n")

def continue_example():
    print("Continue Example:")
   
    for i in range(1, 11):
        if i % 2 == 0:
            print("Skipping", i)
            continue
        print(i, end=" ")
    print("\nLoop ended.")

def main():
    break_example()
    continue_example()

if __name__ == "__main__":
    main()
