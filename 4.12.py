def cube_of_even_numbers():
    even_numbers = [2 * i for i in range(1, 11)]  
    cubes = [num ** 3 for num in even_numbers]   
    return cubes

def main():
    cubes = cube_of_even_numbers()
    print("Cube of the first 10 even numbers:")
    for i, cube in enumerate(cubes, 1):
        print("Cube of", 2 * i, "is:", cube)

if __name__ == "__main__":
    main()
