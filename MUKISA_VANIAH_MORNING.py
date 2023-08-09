


#START OF MORNING SESSION 


'''#Basic  operators and expressions 
Arithmetic operators
Addition +
Multiplication ×
Subtraction -
Division ÷
Modulus %
Expontiate **

Comparison operators
== equal
<= less or equal to
>= greater or equal to
!= or !== not equal to
< less than
> greater than

Logical operators
Logical AND 'and'
Logical OR 'or'
Logical NOT 'not'

Assignment operators 
Assign value: =
Add value: +
Add and assign: +=
Subtract and assign: -=
Multiply and assign: ×=
Divide and assign: ÷=
Modulus and assign: %=
Expontiate and assign: **=

Membership operators
In: 'in' checks if a value exists in  sequence.
not in: checks if a value doesn't exist in a sequence 

Identity operators 
is: checks if two values are the same 
is not: checks if two values are not the same.
'''
'''#Examples
#Addition
x= 48+ 50
print(x)

#Subtraction 
y= 48- 50
print(y)

#Multiplication 
z= 4* 5
print(z)

#Modulus
a= 48%3
print(a)

#Division 
b= 48/3
print(b)

#Divide
c= 48//3
print(c)

#Expontiate
d= 4**2
print(d)'''

'''#Examples of comparison operators
a= 56
b=21

#greater than
if a>b: 
    print(f"{a} is greater than {b}")
    print(a>b)
    
    

#less than
if a<b: 
    print(f"{a} is less than {b}")
    print(a<b)
    

#greater than or equal to
if a>=b: 
    print(f"{a} is greater than or equal to {b}")
    print(a>=b)

#less than or equal to
if a<=b: 
    print(f"{a} is less than or equal to {b}")
    print(a<=b)

#equal to
if a==b: 
    print(f"{a} is equal to {b}")
    print(a==b)

 
#not equals to
if a!=b: 
    print(f"{a} is not equal thing {b}")
    print(a!=b)
'''

#Examples with logical operators

# operator 'and'
a= True
b= False

if a and b:
    print (a and b)
    
    
    
    
#'or' operator
if a or b:
    print(a or b)
    
    
#'not' operator
print(not b)
print(not a)

# Assignment operators
a= 3
b=2
b+=a
print(b)

b=2
b-=a
print(b)

b=2
b/=a
print(b)

b=2
b%=a
print(b)

b=2
b*=a
print(b)

#Identity operators
x= 10
y= 10

print(x is y)
print(x is not y)
print(x==y)
print(x!=y)
print(x<y)
print(x<=y)

#list
# is not operator

z= [1,2,3,4,5,6,7]
x= [1,2,3,4,5,6,7]

print (z is x)
#list
# is not operator

z= [1,2,3,4,5,6,7]
x= [1,2,3,4,5,6,7]

print (z is x)
    
    
    


#Examples with logical operators

# operator 'and'
a= True
b= False

if a and b:
    print (a and b)
    
    
 #MEMBERSHIP OPERATORS
print("MEMBERSHIP OPERATORS")

x = [1,2,3,4,5,6]

print( 2 in x)

print(10 in x)
   
  #BITWISE OPERATORS
print("BITWISE OPERATORS")
a = 10
b = 11

print( a & b)

print(a | b)

print(a ^ b)

print(~a)

print(~b)

print(a << b)

print(a >> b)  
    






#simple Calculator assignment


import tkinter
from tkinter import *
from tkinter import messagebox

# setting the initial values of some variables
var = ""
A = 0
operator = ""

# defining the function for Button 1
def button_1_is_Clicked():
    global var
    var = var + "1"
    the_data.set(var)

# defining the function for Button 2
def button_2_is_Clicked():
    global var
    var = var + "2"
    the_data.set(var)

# defining the function for Button 3
def button_3_is_Clicked():
    global var
    var = var + "3"
    the_data.set(var)

# defining the function for Button 4
def button_4_is_Clicked():
    global var
    var = var + "4"
    the_data.set(var)

# defining the function for Button 5
def button_5_is_Clicked():
    global var
    var = var + "5"
    the_data.set(var)

# defining the function for Button 6
def button_6_is_Clicked():
    global var
    var = var + "6"
    the_data.set(var)

# defining the function for Button 7
def button_7_is_Clicked():
    global var
    var = var + "7"
    the_data.set(var)

# defining the function for Button 8
def button_8_is_Clicked():
    global var
    var = var + "8"
    the_data.set(var)

# defining the function for Button 9
def button_9_is_Clicked():
    global var
    var = var + "9"
    the_data.set(var)

# defining the function for Button 0
def button_0_is_Clicked():
    global var
    var = var + "0"
    the_data.set(var)

# defining the function for Button +
def button_Add_is_Clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "+"
    var = var + "+"
    the_data.set(var)

# defining the function for Button -
def button_Sub_is_Clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "-"
    var = var + "-"
    the_data.set(var)

# defining the function for Button *
def button_Mul_is_Clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "*"
    var = var + "*"
    the_data.set(var)

# defining the function for Button /
def button_Div_is_Clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "/"
    var = var + "/"
    the_data.set(var)

# defining the function for Button =
def button_Equal_is_Clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "="
    var = var + "="
    the_data.set(var)

# defining the function for Button C
def button_C_is_Clicked():
    global A
    global var
    global operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)

# defining the function to display result
def res():
    global A
    global operator
    global var
    var2 = var
    if operator == "+":
        a = float((var2.split("+")[1]))
        x = A + a
        the_data.set(x)
        var = str(x)
    elif operator == "-":
        a = float((var2.split("-")[1]))
        x = A - a
        the_data.set(x)
        var = str(x)
    elif operator == "*":
        a = float((var2.split("*")[1]))
        x = A * a
        the_data.set(x)
        var = str(x)
    elif operator == "/":
        a = float((var2.split("/")[1]))
        if a == 0:
            messagebox.showerror("Division by 0 Not Allowed.")
            A = ""
            var = ""
            the_data.set(var)
        else:
            x = float(A / a)
            the_data.set(x)
            var = str(x)

# creating an object of the Tk() class
guiWindow = tkinter.Tk()
# setting the size of the window
guiWindow.geometry("320x500+400+400")
# disabling the resize option for better UI
guiWindow.resizable(0, 0)
# setting the title of the Calculator window
guiWindow.title("Mukisa_Vaniah Simple Calculator")

# creating a variable of type StringVar
the_data = StringVar()

# creating a text entry box for displaying the input and output
txtDisplay = Entry(guiWindow, font=('arial', 20, 'bold'), textvariable=the_data, bd=30, insertwidth=4, width=14, justify='right')
txtDisplay.grid(row=0, column=0, columnspan=4)

# creating buttons for the calculator
btn_1 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="1", command=button_1_is_Clicked)
btn_1.grid(row=1, column=0)

btn_2 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="2", command=button_2_is_Clicked)
btn_2.grid(row=1, column=1)

btn_3 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="3", command=button_3_is_Clicked)
btn_3.grid(row=1, column=2)

btn_4 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="4", command=button_4_is_Clicked)
btn_4.grid(row=2, column=0)

btn_5 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="5", command=button_5_is_Clicked)
btn_5.grid(row=2, column=1)

btn_6 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="6", command=button_6_is_Clicked)
btn_6.grid(row=2, column=2)

btn_7 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="7", command=button_7_is_Clicked)
btn_7.grid(row=3, column=0)

btn_8 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="8", command=button_8_is_Clicked)
btn_8.grid(row=3, column=1)

btn_9 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="9", command=button_9_is_Clicked)
btn_9.grid(row=3, column=2)

btn_0 = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="0", command=button_0_is_Clicked)
btn_0.grid(row=4, column=0)

btn_add = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="+", command=button_Add_is_Clicked)
btn_add.grid(row=1, column=3)

btn_sub = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="-", command=button_Sub_is_Clicked)
btn_sub.grid(row=2, column=3)

btn_mul = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="*", command=button_Mul_is_Clicked)
btn_mul.grid(row=3, column=3)

btn_div = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="/", command=button_Div_is_Clicked)
btn_div.grid(row=4, column=3)

btn_equal = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="=", command=button_Equal_is_Clicked)
btn_equal.grid(row=4, column=2)

btn_clear = Button(guiWindow, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text="C", command=button_C_is_Clicked)
btn_clear.grid(row=4, column=1)

# running the mainloop
guiWindow.mainloop()



#END OF MORNING SESSION









