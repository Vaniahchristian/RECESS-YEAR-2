import math

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine has started.")
    
    def stop_engine(self):
        print("Engine has stopped.")

    def car_details(self):
        print(f"Make : {self.make}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_cicumference(self): return  2 *math.pi * self.radius

    def calcuate_area(self): return math.pi *self.radius**2


circle = Circle(12)
print("Circumference: ",round(circle.calculate_cicumference(),4))
print("Area: ", round(circle.calcuate_area(),4))

class Employee:
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.15

emp1 = Employee(150000)
print(emp1.calculate_bonus())
emp2 = Employee(230000)
print(emp2.calculate_bonus())

    
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money on your account!") 
        
 
 EXERCISE  
#converting from celcius to fahrenheit in degrees
 
class Temperature:
    def __init__(self, celcius):
        self.__celcius = celcius
    
    def get_celcius(self):
        return self.__celcius
    
    def set_celcius(self, new_temp):
        self.__celcius = new_temp
    
    def get_farenheit(self):
        return (self.__celcius * 9/5) +32

temp = Temperature(32)
print("Farenheit: ",temp.get_farenheit())
