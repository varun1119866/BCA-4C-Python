def while_with_else():
    count = 0
    while count < 5:
        print("Count:", count)
        count += 1
    else:
        print("The while loop completed without encountering a break statement.")


def while_with_break():
    count = 0
    while count < 5:
        print("Count:", count)
        if count == 3:
            print("Encountered 3, breaking loop...")
            break
        count += 1
    else:
        print("The while loop completed without encountering a break statement.")

def main():
    print("Using else with while loop:")
    while_with_else()
    print("\nUsing else with while loop and break statement:")
    while_with_break()

if __name__ == "__main__":
    main()
