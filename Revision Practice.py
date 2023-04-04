import sys
print("Python Version")
print(sys.version)
print("Version Info")
print(sys.version_info)

import datetime
now=datetime.datetime.now()
print("Date & Time")
print(now.strftime("%d/%m/%Y,  %H:%M:%S"))

# What is radius of the circle?

import math 
radius=float(input("Enter the area of the circle"))
area= math.pi*radius**2
print("The area of the circle is:", area)

# how to write your name in reverse order

first_name= "Rahim"
last_name= " Ahmed"
full_name= first_name + last_name
print(full_name)
print(full_name [::-1])

#write your name in input terms
first_name= input("Enter your Name")
last_name= input("Enter Your Name")
full_name= last_name + first_name
print(full_name)
print (full_name[::-1])

import sys
print("Print Python Version")
print(sys.version)
print("Version Info")
print(sys.version_info)

import datetime
now=datetime.datetime.now()
print("Date & Time")
print(now.strftime("%d/%m/%y  %H:%M:%S"))

first_name= input("Enter Your Name")
last_name= input("Enter Your Name")
full_name= last_name + first_name
print(full_name [::-1])
print(full_name)

import math

radius=float(input("EnterThe are of the circle"))
area= math.pi*radius**2
print("The are of the circle is:", area)

# if Statement
shahab= 5 
shahab_ki_bachi= 4

if shahab + shahab_ki_bachi== 9 :
        print("They have family")
else :
        print("They don't have family")        


shahab=55
muneeb=99
tehreem=105
Rahim=100
if shahab>= Rahim:
        print("Shahab has Better wealth")
if muneeb >= Rahim :
           print("Muneeb has good Wealth")
if tehreem>= Rahim:
       print("Tehreem Has Good wealth")
else :
    print("Rahim Has Bigger wealth then others")

# elif statement means multiple if statement

per= int(input("Enter Percentage"))
if per>= 90:
        print("A++")
elif per>= 80 and per <90 :
        print("A+")
elif per>=  70 and per <80:
        print("A")
elif per>= 60 and per< 70:
        print("B")
elif per>= 50 and per< 60:
        print ("You are Failed")                     


import sys
print("Pyhton Version")
print(sys.version)
print("Version Info")
print(sys.version_info)

import datetime
now=datetime.datetime.now()
print("Date & Time")
print(now.strftime("%d/%m/%y %H:%M,%S"))


import math
radius=float(input("Enter the are of the circle"))
area=math.pi*radius**2
print("The area of the Circle is:", area)


first_name=input("ENter Your name")
last_name=input("Enter Your name")
Full_name=(last_name + first_name)
print(Full_name)
print(Full_name [::-1])

per=int(input("Enter Percentage%"))
if per>= 90 and per<=100:
        print("A++")
elif per>= 80 and per<90:
        print("A+")
elif per>= 70 and per< 80:
        print("A")
elif per>= 60 and per<70:
        print("B")
elif per>=50 and per<60:
        print("C")
elif per>= 40 and per<50:
        print("D")
else:
       print("You are Failure") 


arr=["Ali", "Abdullah", "Osama", "MySon", "Wasay"]
arr.append("Rahim Daddy")
print(arr)
arr1= arr+["Sarkar, Muneeb"]
print(arr1)
arr1.inset(2, "Betee")
print(arr1)
del arr1[3]
print(arr1)

"""
Temperature converter: Create a program 
that converts temperatures from Fahrenheit to Celsius and vice versa.
 Use if statements to determine which conversion formula to use based 
 on the input temperature scale?
"""
# Short Key of Degree Sign: ALtr + 0176 "°"

Temperature= float(input("ENterTemperature"))
Scale= input("Enter Scale(Fahrenheit °F or Celsisu °C)")
if Scale == "°F":
    Convert_Temperature = (Temperature -32)*5/9
    print(f"{Temperature}°F = {Convert_Temperature}°C")
elif Scale == "°C":
    Convert_Temperature = (Temperature*9/5)+32
    print(f"{Temperature}°C = {Convert_Temperature}°F")    
else:
    print("Temperature Scale is Invalid")




