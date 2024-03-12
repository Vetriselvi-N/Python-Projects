#import the random and math module
import random
import math
print("Welcome to the lucky number generator!\n")

fName = input("Enter your first name:")#get user input on their first name
lName = input("Enter your second name:")#get user input on their last name
age = int(input("Enter your age:"))#get user input on their age (remember to wrap it around an int())

x = len(fName)+len(lName)#set x equal to the absolute value of THE LENGTH of fName + THE LENGTH of lName
y = random.randint(1,100)#set y equal to a random integer between 1 and 100

luckyNum = math.ceil((x*y)/age)#set luckyNum equal to the ceiling of x + y + age

#add luckyNum after the string
print("Your lucky number is: " + str(luckyNum) )
