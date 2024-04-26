def find_char(char, string):
  for i in range(len(string)):
      if string[i] == char:
          return i
  return -1
print("Name: Dhruv \nRoll No: 2210997071\n")
user_string = input("Enter a string: ")
user_char = input("Enter a character to search: ")
result = find_char(user_char, user_string)

if result != -1:
  print("The character",user_char,"is present at index",result,".")
else:
  print("The character",user_char,"is not present in the string.")


  