#BEGINNING OF THE EVENING SESSION 

#EXERCISE 1
# 1.Output the 2nd item (index 1) from the list
names = ["John", "Emily", "Michael", "Sophia", "David"]
print(names[1])  

#2. Change the value of the first item (index 0) to "Robert"
names = ["John", "Emily", "Michael", "Sophia", "David"]
names[0] = "Robert"  
print(names)


# 3.Add "Daniel" as the sixth item to the list
names = ["John", "Emily", "Michael", "Sophia", "David"]
names.append("Daniel")  
print(names)


# 4.Insert "Bathel" at index 2 in the lis
names = ["John", "Emily", "Michael", "Sophia", "David"]
names.insert(2, "Bathel")  # Insert "Bathel" at index 2 in the list
print(names)

# 5.Remove the item at index 3 from the list
names = ["John", "Emily", "Bathel", "Michael", "Sophia", "David"]
del names[3]  
print(names)

#6. Output the last item using negative indexing
names = ["John", "Emily", "Bathel", "Sophia", "David"]
print(names[-1])  


# 7.Output a sublist containing items from index 2 to index 4
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:5])  

# 8.Create a copy of the original list
countries = ["USA", "Canada", "France", "Germany", "Japan"]
countries_copy = countries.copy()  
print(countries_copy)


#9.To loop through a list of countries
countries = ["USA", "Canada", "France", "Germany", "Japan"]
for country in countries:  # Iterate over each item in the list
    print(country)  # Output each country name


#10.To sort a list of animal names in ascending and descending order:
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]
ascending_order = sorted(animals)  # Sort the list in ascending order
descending_order = sorted(animals, reverse=True)  # Sort the list in descending order
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)


#11.To output animal names that contain the letter 'a':
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]
a_names = [name for name in animals if 'a' in name]  # Filter names that contain the letter 'a'
print(a_names)  # Output the filtered list


#12.Here's an example of two lists: first_names and last_names. We will join these lists together to create a new list called full_names.
first_names = ["John", "Emily", "Michael", "Sophia", "David"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Davis"]

# Joining the two lists
full_names = []
for first, last in zip(first_names, last_names):
    full_names.append(first + " " + last)

# Alternatively, you can achieve the same result using a list comprehension:
# full_names = [first + " " + last for first, last in zip(first_names, last_names)]

# Print the full names
for name in full_names:
    print(name)



#Exercise2 (Tuples)


#1.To output your favorite phone brand from the tuple
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[1]  # Access the second item (index 1)
print(favorite_phone_brand)

#2.To print the second last item using negative indexing:
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]  # Access the second last item using negative indexing
print(second_last_item)

#3.To update "iphone" to "itel" in the tuple:
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)  # Convert the tuple to a list
x[x.index("iphone")] = "itel"  # Find the index of "iphone" and update it to "itel"
x = tuple(x)  # Convert the list back to a tuple
print(x)

#4.To add "Huawei" to the tuple:
x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)  # Concatenate the tuple with a new tuple containing "Huawei"
print(x)

#5.To loop through the tuple:
x = ("samsung", "iphone", "tecno", "redmi")
for item in x:  # Iterate over each item in the tuple
    print(item)


#6.To remove the first item from the tuple:
x = ("samsung", "iphone", "tecno", "redmi")
x = x[1:]  # Slice the tuple starting from index 1 to the end
print(x)

#7.To create a tuple of cities in Uganda using the tuple constructor:
cities = tuple(("Kampala", "Entebbe", "Jinja", "Mbarara"))
print(cities)

#8.To unpack the tuple:
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x  # Unpack the tuple into individual variables
print(brand1, brand2, brand3, brand4)

#9.To print the 2nd, 3rd, and 4th cities using a range of indexes:
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara")
print(cities[1:4])  # Output a slice from index 1 to index 3 (exclusive)


#10.To join two tuples containing first names and second names:
first_names = ("John", "Emily", "Michael", "Sophia", "David")
last_names = ("Smith", "Johnson", "Williams", "Brown", "Davis")
full_names = first_names + last_names  # Concatenate the two tuples
print(full_names)


#11.To create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
multiplied_colors = colors * 3  # Multiply the tuple by 3
print(multiplied_colors)

#12.To return the number of times 8 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)


#exercise 3 (Sets)

#1.To create a set of 3 favorite beverages using the set() constructor:
beverages = set(["coffee", "tea", "juice"])
print(beverages)

#2.To add 2 more items to the beverages set using the add() method:
beverages.add("water")  # Add "water" to the set
beverages.add("soda")   # Add "soda" to the set
print(beverages)

#3.To check if "microwave" is present in the given set:
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

#4.To remove "kettle" from the set:
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")  # Remove "kettle" from the set
print(mySet)

#5.To loop through the set:
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)

#6.To add elements from a list to a set:
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)  # Add elements from the list to the set
print(mySet)

#7.To join two sets containing ages and first names:
ages = {20, 25, 30}
first_names = {"John", "Emily", "Michael"}
joined_set = ages.union(first_names)  # Join the two sets
print(joined_set)


#Example 4(Strings)

#1.To concatenate an integer and a string:
num = 10
text = "Hello"
concatenated = str(num) + text  # Convert the integer to a string and concatenate
print(concatenated)

#2.To output the string without spaces at the beginning, in the middle, and at the end:
txt = " Hello, Uganda! "
stripped = txt.strip()  # Remove spaces at the beginning and the end
print(stripped)

#3.To convert the value of txt to uppercase:
txt = " Hello, Uganda! "
uppercase = txt.upper()  # Convert the string to uppercase
print(uppercase)

#4.To replace the character 'U' with 'V' in the string:
txt = " Hello, Uganda! "
replaced = txt.replace('U', 'V')  # Replace 'U' with 'V' in the string
print(replaced)

#5.To return a range of characters in the 2nd, 3rd, and 4th positions:
y = "I am proudly Ugandan"
range_of_characters = y[1:4]  # Get the characters from index 1 to 3 (exclusive)
print(range_of_characters)

#6.To correct the code that gives an error due to the presence of double quotes:
x = 'All "Data Scientists" are cool!'  # Correct the quotes by using single quotes
print(x)


#EXERCISE 4
 
 #1.Concatenating variables
 
num = 10
text = "Hello"

# Concatenate variables using the str() function to convert the integer to a string
result = text + " " + str(num)

# Print the result
print(result)


#2.Removing Spaces From a string
# Declare the string
txt = " Hello, Uganda! "

# Remove spaces using the strip() method
result = txt.strip()

# Print the result
print(result)


#3.Converting string to uppercase
# Declare the string
txt = "Hello, Uganda!"

# Convert the string to uppercase using the upper() method
result = txt.upper()

# Print the result
print(result)

#4.Replacing characters in a string
# Declare the string
txt = "Hello, Uganda!"

# Replace 'U' with 'V' using the replace() method
result = txt.replace('U', 'V')

# Print the result
print(result)

#5.Returning a range of characters
# Declare the string
y = "I am proudly Ugandan"

# Extract a range of characters using string slicing
result = y[1:5]  # Returns characters from the 2nd to 4th position (index starts at 0)

# Print the result
print(result)


 #6.fixing the error 
 # Corrected code with double quotes escaped using a backslash
x = "All \"Data Scientists\" are cool!"

# Print the corrected string
print(x)


#EXERCISE 5 

#1.printing the value of a specific key 
# Dictionary declaration
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of the "size" key
print(Shoes["size"])

#2.changing the value of a key in a dictionary 

# Change the value of the "brand" key to "Adidas"
Shoes["brand"] = "Adidas"

# Print the updated dictionary
print(Shoes)

#3.Adding a new key/value pair to a dictionary 

# Add a new key/value pair to the dictionary
Shoes["type"] = "sneakers"

# Print the updated dictionary
print(Shoes)

#4.Returning a list of keys in a dictionary 

# Get a list of all keys in the dictionary
keys_list = list(Shoes.keys())

# Print the list of keys
print(keys_list)

#5.Returning a list of values in the dictionary 
# Get a list of all values in the dictionary
values_list = list(Shoes.values())
print(values_list)

#6.checking if a key exists in the dictionary 

if "size" in Shoes:
    print("Key 'size' exists")
else:
    print("Key 'size' does not exist")
    
#7. Looping through a dictionary 

for key, value in Shoes.items():
    print(key, ":", value)

#8.Removing a key from a dictionary 
# Remove the key "color" from the dictionary
del Shoes["color"]

# Print the updated dictionary
print(Shoes)

#9.Emptying a dictionary 
# Clear all key-value pairs from the dictionary
Shoes.clear()

# Print the updated dictionary (empty)
print(Shoes)

#10.Making a copy of the dictionary 

# Original dictionary
original_dict = {"key1": "value1", "key2": "value2"}

# Make a copy of the dictionary using the copy() method
copied_dict = original_dict.copy()

# Print the original and copied dictionaries
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

#11.Nested Dictionaries 

nested_dict = {
    "outer_key1": {
        "inner_key1": "value1",
        "inner_key2": "value2"
    },
    "outer_key2": {
        "inner_key3": "value3",
        "inner_key4": "value4"
    }
}

# Accessing values in nested dictionaries
print(nested_dict["outer_key1"]["inner_key1"])  # Output: value1
print(nested_dict["outer_key2"]["inner_key4"])  # Output: value4

