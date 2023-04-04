#concatenation and interpolation
a= ("Hi")
b= (" Shahab,")
c= (" greeting")
d= ("!") 
print(a +b +c  +d  + ":kese ho")
greeting= "hello shahab"
haalawaal= " kese ho"
f= ":6"
print(greeting+haalawaal+f)
"""
in concatenation you can merdge int and float with str,
 if you want to add number with stringh you have to add "" with that
 """
a= "  name: Rahim,"
b= "  Age: 22,"
c= "  Gender: Male,"
d= "  Any Aulaad: haan 4."
print(a+b+c+d)

a=2**3
print(a)
#when you use double** between any number it will get the power value
#print("haha" * 8) 
#x=int(input("65"))
#y=20
#z= x + y
#print(z)
"""
yeh
hai multi line 
comments section when you have to use a long note
for reminder you have use commas like this
"""
x= input("type anumber")
y=15


#how to get Python version info

x=int(input("enter the value"))
y=15

z= x + y
print(z)

import sys
print("Python version")
print(sys.version)
print("Version info")
print(sys.version_info)

print(sys.version.split()[0])

import datetime
now= datetime.datetime.now()
print("Date and Time")
print(now.strftime("%y-%m-%d  %H:%M:%S"))
"""
in python cap (M) presents: MInutes
in python Small (m) presents: Month
in python Small (d) presents: day
it is very imp when your coding for date and time
"""

import sys
print("Python Version")
print(sys.version)
print("Version Info")
print(sys.version_info)

import math
radius=float(input("Enter the area of the Circle"))
area= math.pi*radius**2
print("The area of the circle is:", area)
