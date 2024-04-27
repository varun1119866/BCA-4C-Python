def demonstrate_string_functions(string):
    print("Original String:", string)

    
    print("Length of the string:", len(string))

    
    print("Uppercase:", string.upper())

   
    print("Lowercase:", string.lower())

   
    print("Capitalized:", string.capitalize())

    
    substring = input("Enter a substring to count: ")
    print("Count of substring '{}':".format(substring), string.count(substring))

    substring = input("Enter a substring to find index: ")
    print("Index of substring '{}':".format(substring), string.find(substring))

    
    old_substring = input("Enter a substring to replace: ")
    new_substring = input("Enter a new substring: ")
    print("Replaced string:", string.replace(old_substring, new_substring))

    prefix = input("Enter a prefix to check: ")
    print("Starts with '{}':".format(prefix), string.startswith(prefix))

   
    suffix = input("Enter a suffix to check: ")
    print("Ends with '{}':".format(suffix), string.endswith(suffix))

def main():
    string = input("Enter a string: ")
    demonstrate_string_functions(string)

if __name__ == "__main__":
    main()
