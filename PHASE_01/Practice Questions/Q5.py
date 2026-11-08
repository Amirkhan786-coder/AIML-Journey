print("----Strings----")

text = "Hello, World!"
print(text)

print("Length of the string:", len(text))
print("Uppercase:", text.upper())             
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Count of 'o':", text.count('o'))
print("Index of 'World':", text.index('World'))
print("Replace 'World' with 'Python':", text.replace('World', 'Python'))
print("Split the string:", text.split(','))
print("Check if string starts with 'Hello':", text.startswith('Hello'))
print("Check if string ends with 'World!':", text.endswith('World!'))
print("Check if string is alphanumeric:", text.isalnum())
print("Check if string is alphabetic:", text.isalpha())
print("Check if string is numeric:", text.isnumeric())
print("Check if string is whitespace:", text.isspace())
print("Check if string is title case:", text.istitle())
print("Check if string is uppercase:", text.isupper())
print("Check if string is lowercase:", text.islower())
print("Check if string is printable:", text.isprintable())
print("Check if string is decimal:", text.isdecimal())
print("Check if string is digit:", text.isdigit())



print("----String Indexing----")
print("Character at index 0:", text[0])
print("Character at index 7:", text[7])
print("Substring from index 0 to 5:", text[0:5])
print("Substring from index 7 to 12:", text[7:12])

print("----String Slicing----")
print("Substring from index 0 to 5:", text[0:5])
print("Substring from index 7 to 12:", text[7:12])
print("Substring from index 0 to 12 with step 2:", text[0:12:2])
print("Substring from index 12 to 0 with step -1:", text[12:0:-1])
print("Substring from index 12 to 0 with step -2:", text[12:0:-2])
print("Substring from index 0 to 12 with step 3:", text[0:12:3])

print("----String Formatting----")
name = "Amir"
age = 20
print("Hello, my name is {} and I am {} years old.".format(name, age))
print("Hello, my name is {0} and I am {1} years old.".
format(name, age))
print("Hello, my name is {name} and I am {age} years old.".
format(name=name, age=age)) 
print(f"Hello, my name is {name} and I am {age} years old.")            
print("Hello, my name is %s and I am %d years old." % (name, age))


print("----String Concatenation----")
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenated string:", result)
print("Concatenated string using join():", " ".join([str1, str2]))
print("Concatenated string using f-string:", f"{str1} {str2}")
print("Concatenated string using format():", "{} {}".format(str1, str2))
print("Concatenated string using % operator:", "%s %s" % (str1, str2))
print("Concatenated string using += operator:", end=" ")
str1 += " " + str2
print(str1)

print("----String Repetition----")
str1 = "\nHello"
print("Repeated string:", str1 * 3)

print("----String Membership----")
str1 = "Hello, World!"
print("Is 'Hello' in str1?", 'Hello' in str1)
print("Is 'Python' not in str1?", 'Python' not in str1)
print("Is 'World' in str1?", 'World' in str1)
print("Is 'Java' not in str1?", 'Java' not in str1)


print("----String Escape Sequences----")
print("New Line:\nHello")
print("Tab:\tHello")
print("Backslash:\\Hello")
print("Single Quote:\'Hello\'")
print("Double Quote:\"Hello\"")
print("Carriage Return:\rHello")
print("Form Feed:\fHello")
print("Vertical Tab:\vHello")
print("Bell:\aHello")
print("Backspace:\bHello")
print("Octal Value:\101Hello")
print("Hexadecimal Value:\x41Hello")
print("Unicode Value:\u0041Hello")
print("Raw String: r\"Hello\\nWorld\"")

print("----String Methods----")
text = "Hello, World!"
print("Original string:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Count of 'o':", text.count('o'))
print("Index of 'World':", text.index('World')) 
print("Replace 'World' with 'Python':", text.replace('World', 'Python'))
print("Split the string:", text.split(','))
print("Check if string starts with 'Hello':", text.startswith('Hello'))
print("Check if string ends with 'World!':", text.endswith('World!'))


print("----String Immutability----")
text = "Hello, World!"
print("Original string:", text)
print("ID of original string:", id(text))
text = text.upper()
print("Modified string:", text)
print("ID of modified string:", id(text))


print("----String Iteration----")
text = "Hello"
for char in text:
    print(char) 


