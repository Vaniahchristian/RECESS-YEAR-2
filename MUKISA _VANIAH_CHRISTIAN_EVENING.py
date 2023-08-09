
# Syntax error
x = 10000

if x > 5000:
    print("You are eligible to purchase a premium product")

# Exception
age = 21
try:
    average = age / 0
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Average:", average)

# Other Exception error type of error
name = "Christian"
age = 21
desc = name + " is " + str(age) + " years old."

# Try and except to handle exceptions and errors
name = "Christian"
age = 21
try:
    desc = name + " is " + str(age) + " years old."
except TypeError:
    print("Error: cannot concatenate str and int")

# Program to handle multiple errors with one
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    except ValueError:
        print("Error: Invalid value")
    else:
        print("Result:", result)

divide_numbers(6, 2)
divide_numbers(6, 0)
divide_numbers(6, "2")

# Using else clause with try-except
def calculate_sum(a, b):
    try:
        result = a + b
    except TypeError:
        print("Error: Invalid operands for addition")
    else:
        print("Sum:", result)

calculate_sum(2, 3)
calculate_sum("2", "3")

# Using finally keyword in try and except
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Finally block executed")

# File handling in Python
# Example 1: Reading a file line by line
file = open('sample.txt', 'r')
for line in file:
    print(line)
file.close()

# Example 2: Reading the entire file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# Example 3: Reading only a specific number of characters
file = open("sample.txt", "r")
content = file.read(10)
print(content)
file.close()

# Writing in a file using the write() function
# Example 1
file = open('output.txt', 'w')
file.write("This is the first line.")
file.write(" This is the second line.")
file.close()

# Example 2: Appending content to a file
file = open("output.txt", "a")
file.write("\nThis line is appended.")
file.close()

# Open and read the file after appending
file = open("output.txt", "r")
content = file.read()
print(content)
file.close()

# Deleting a File
import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    print("The file does not exist")

# Deleting a Folder
import os
if os.path.exists("my_folder"):
    os.rmdir("my_folder")
else:
    print("The folder does not exist")
