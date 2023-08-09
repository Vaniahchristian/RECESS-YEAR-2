# Control flow
x = input("What is your age?\n")
x = int(x)

# Using ifs
if x < 18:
    print("You are underage.")
elif x >= 18 and x < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

x < 18, print("You are under age")
x >= 18 and x < 65, print("You are an adult")
print("You are a senior citizen.")

# For loops

cars = ["Audi", "Toyota", "Honda", "Mercedes", "BMW"]

for car in cars:
    #print(f"{car} is a car type.")
    pass

fruits = ["Apple", "Mango", "Pineapple", "Guava"]
while len(fruits) != 0:
    print(f"{fruits[0]} is a car type.")
    fruits.pop(0)


# Break and continue
arr = [1,2,3,4,5,6,7]
count = 0
while count < len(arr):
    if count == 4:
        count += 1
        continue
    elif count == 7:
        break
    print(f"The number is {arr[count]}.")
    count += 1

# Catching exceptions
try:
    x = int(input("What is your age? \n"))
except Exception as err:
    print(f"A {err.__class__.__name__} has occured.")
finally: 
    print("Finished catching error.")

# Dictionaries

# Write a program to ask a student about their mental health.
#Prompt students on a scale of 1 to 10 to rate their mental health.
dic = {
    "happy":"Yay, glad to hear that?",
    "sad":"Can i hug you please?",
    "angry": "Please stay Calm.",
    "scared":"Be brave please."
}

mental_health = {
    1:"Very very bad",
    2:"Very bad",
    3:"Fairly very bad",
    4:"Fairly bad",
    5:"Fair",
    6:"Fairly good",
    7:"Fairly very good",
    8:"Very good",
    9:"Fairly very good",
    10:"Excellent!"
}




feeling = input("On a scale of 1 to 10, how are you feeling today?\n")
for x  in mental_health:
    if(int(feeling) == x):
        print(mental_health[k])
        
 #END OF MORNING SESSION
 # DICTINARIES
 # example
student = {
    "name": "Christian",
    "age": 21,
    "program": "BSSE",
    "gpa": 4.5
}
# Accessing dictionary values
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Program:", student["program"])
print("Student GPA:", student["gpa"])

# Modifying dictionary values
student["gpa"] = 4.6
print("Updated GPA:", student["gpa"])

# Adding a new key-value pair
student["year"] = "YR3"
print("Student Year:", student["year"])

#EXERCISE
# Get all values in the dictionary
values_list = list(student.values())
print("values in the dictionary are:", values_list)

# Check if a key exists
if "age" in student:
    print("The 'age' key exists in the dictionary.")

if "year" in student:
    print("The 'year' key exists in the dictionary.")
else:
    print("The 'year' key does not exist in the dictionary.")

# Update items using the update() method
student.update({"program": "BIST", "gpa": 4.8})
print(student)

# Removing a key-value pair
del student["program"]
print("Updated Dictionary:", student)


# Loop through the dictionary
for key, value in student.items():
    print(key, ":", value)
    

# DATA TYPES
a = 6  # int
b = 4.555  # float
c = 7j  # complex

# type conversion (EXERCISE)
# int to float
x = float(a)
print(type(x))

# float to complex
z = complex(b)
print(type(z))

# complex to float
r = float(c)


#STRINGS
#declare a string
name = "Christian"
print(name)

#single line string
x= "me"

'''exercise
use the len() method for length
use a for loop
an example in slicing in strings
'''
print (len(x))

for y in x:
    print(y)
    
# Slicing example in strings

text = "Hello, World!"

# Slicing a string
slice1 = text[0:5]  # Slice from index 0 to 4 (exclusive)
slice2 = text[7:]   # Slice from index 7 to the end
slice3 = text[:5]   # Slice from the beginning to index 4 (exclusive)
slice4 = text[::2]  # Slice with a step size of 2

# Print the slices
print("Slice 1:", slice1)
print("Slice 2:", slice2)
print("Slice 3:", slice3)
print("Slice 4:", slice4)

#multiline strings
quote = '''i am going to work
this Friday'''
 
 #as arrays
Lname = "Christian"
for x in Lname:
      print(x)
      
      
#exercise
#how to modify a string
a="afternoon" 
# print(a.upper)
# print(a.lower)

#remove whitespace
b = "after noon"
print(b.strip())
 
#string concatenation
fruit1 = "jackfruit"
fruit2 = "orange"
print (fruit1 + fruit2)

#formating strings
name = "kityo"
age = 28
profession = "Baker"

# Using positional arguments
message = "My name is {}. I'm {} years old and I work as an {}.".format(name, age, profession)
print(message)

# Using indexed arguments
message = "My name is {0}. I'm {1} years old and I work as an {2}.".format(name, age, profession)
print(message)

# Using named arguments
message = "My name is {name}. I'm {age} years old and I work as an {profession}.".format(name=name, age=age, profession=profession)
print(message)

# Using f-strings (Python 3.6+)
message = f"My name is {name}. I'm {age} years old and I work as an {profession}."
print(message)


#booleans evaluate to true or false
#use conditions to show boolean values

number = 8


if number  == 0:
    print("The number is true.")
else:
    print("The number is false.")

 
    