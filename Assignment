print("twinkle, twinkle, little star,")
print("       how i wonder whatyou are!")
print("             up above the world so high,")
print("             like a diamond in the sky.")
print ("twinkle, twinkle, little star,")
print ("       how i wonder whatyou are.")

#How to get vesion info
import sys
print("Python version")
print(sys.version)
print("Version info")
print(sys.version_info)

print(sys.version.split()[0])

#How to write Current Date and Time
import datetime
now= datetime.datetime.now()
print("Date and Time")
print(now.strftime("%d/%m/%y, %H:%M:%S"))


#write a python program which accepts the radius of a circle from user & compute area

# import math
# radius= float(input("Enter the area of the circle"))
# area=math.pi*radius**2
# print("The area of circle is:", area)

import math
radius=float(input("Enter the area of the Circle"))
area= math.pi*radius**2
print("The area of the circle is:", area)


# Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.

# first_name=Raheem 
# last_name= Kamal

# print("Name:" "last_name + first_name")

a = 32
b= 36
c= a + b
print(c)


first_name= input("Enter your first Name")
last_name= input("Enter your Last Name")
# full_name= last_name + "" + first_name
full_name= last_name + first_name
# there are two way of writting your name in reverse order 
print(full_name)
print(full_name[::-1])


# Write a python program which takes two inputs from user and print them addition
company_1= input("Enter comapany name")
company_2= input("ENtercompany name")
both_company_name= company_1 + company_2
print(both_company_name)

Student_name=input("Enter Student Name")
Class_Name= int(input("Enter Class No"))
Urdu_Marks= int(input("ENter Urdu Marks"))
Maths_Marks= int(input("ENter Math Marks"))
Science_Marks= int(input("ENter Science Marks"))
English_Marks= int(input("ENter English Marks"))
Computer_Marks= int(input("ENter Computer Marks"))
Obtained_Marks=(Urdu_Marks+Maths_Marks+Science_Marks+English_Marks+Computer_Marks)
Total_Marks= 500
Percentage=(Obtained_Marks/Total_Marks*100)
print("Student Name:", Student_name)
print("Class:", Class_Name)
print("Marks")
print("Urdu:", Urdu_Marks) 
print("Math:", Maths_Marks) 
print("Science:", Science_Marks) 
print("English:", English_Marks) 
print("Computer:", Computer_Marks) 
print("Obtained Marks:", Obtained_Marks , ", Total Marks:", Total_Marks)
print( "Percentage:", f"{Percentage}%") #str Interpolation Applied
if Percentage>= 90 and Percentage<=100:
    print("Grade: A++")
elif Percentage>= 80 and Percentage<90:
    print("Grade: A+")
elif Percentage>= 70 and Percentage<80:
    print("Grade: A")
elif Percentage>= 60 and Percentage<70:
    print("Grade: B")
elif Percentage>= 50 and Percentage<60:
    print("Grade: C")

elif Percentage>= 40 and Percentage<50:
    print("Grade: D")
else:
    print("You are Failed")

"""
 Write a program which take input from user and identify that the given
 number is even or odd?
"""
Num= int(input("Enter Number"))
if Num % 2 ==0:
    print(Num,"Number is Even")
else:
    print(Num, "Number is Odd")    

# How to gotta know the length of the list?

CLass_room= ["Ali", "Abdullah", "Haris", "Wasay", "Rahim Daddy"]
print(len(CLass_room))

#Write a Python program to sum all the numeric items in a list?

Cash_Amount=[100000, 200000, 800000, 1500000]
print(sum(Cash_Amount))

# if you the list which includes the non-numeric elements the what will you do?

Cash= ["Hello", "Ali", "Abdullah",56000, 25000, 98000]
# we have to make total=0 to refining(iterate) the Numeric Values.

total=0
    #we use 'for' to iterate(Refining) the data
for item in Cash:  
# we use isinstance to specify the data 
    if isinstance(item, (int, float)):
        #add item to the total sum
     total+= item 
print("The Sum Of All MNumeric Items in the list", total)

# How to get the Largest number from the list?
Numbers= [100, 500, 2000, 10, 2500, 00]
# we are making value of largest(variable) and are putting the value of any smallest value
largest= Numbers[3]
#for is using to looping all the value in list
for num in Numbers:
    if num> largest:
        largest=num
print("The Largest Number of the list:", largest)

#  Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.


for num in a:
    if num<5:
        print(num)

import re
Password=input("EnterPassword")

if len(Password)<8:
    print(" Your Password should be contain 8 Characters")
elif not re.search("[a-z]", Password):
    print("Your Password should contain at least one lower case letter ")
elif not re.search("[A-Z]", Password):
    print("Your Password should contain at least one Upper case letter")    
elif not re.search("[!,<,@,#,$,%]", Password):
    print("Your Password Should Contain at Least One Special Character")
else:
    ("Password is too Strong")        

        

