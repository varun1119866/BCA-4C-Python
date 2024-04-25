# Built-in functions of strings

text = "Hello, World!"

# Length of the string
print("Length of the string:", len(text))

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Count occurrences of a substring
substring = "l"
print("Occurrences of 'l':", text.count(substring))

# Check if the string starts with a specific substring
substring = "Hello"
print("Starts with 'Hello':", text.startswith(substring))

# Check if the string ends with a specific substring
substring = "World!"
print("Ends with 'World!':", text.endswith(substring))

# Find the index of a substring
substring = "World"
print("Index of 'World':", text.find(substring))

# Replace a substring with another string
old_substring = "World"
new_substring = "Python"
new_text = text.replace(old_substring, new_substring)
print("After replacement:", new_text)
