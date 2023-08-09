#Running Python Scripts
print("I love Python")

#VARIABLES
name= "Mukisa Vaniah Christian"
age= 23
language= "Python"

print("I am "+ name+" and I am "+ str(age)+" years old. I love "+ language+".")
'''
Multiline commment
recess is fun
'''
#PEP8: Python script guidelines

#DATA STRUCTURES
'''
Sequence types
List enclosed with square brackets [] represented in order collections
Tuples Enclosed in Parentheses () range often used for iterations
Mapping types
Dictionary is enclosed in is enclosed with with curly braces{} containing key-value pairs
'''
#List
Names_List=['Mukisa ', "Vaniah", 'Christian', "Apollo", 'Malomo']
print(Names_List)   #['Mukisa', 'Vaniah', 'Christian', 'Apollo', 'Malomo']
print(type(Names_List)) #<class 'list'>

#Tuple
Names_Tuple=("Vaniah", "Jerry", 'Philip')
print(Names_Tuple)
print(Names_Tuple[0])

Name= "Jack"
New_Tuple= Names_Tuple +(Name,) #Concatenation of Tuples
print(New_Tuple)

#Dictionary
My_Dict={"Mukisa": 6, "Vaniah": 3, "Christian":5, "Ng":2}
print(My_Dict)
print(My_Dict["Mukisa"])

'''
Set Types
{Apple, Mango, Banana} Unordered Collection type

None Types: None represents Absence of a value
'''
gender_sex= True
print(gender_sex)
