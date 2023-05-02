import sys
print("Python version")
print(sys.version)
print("Version Info")
print(sys.version_info)


import datetime

now=datetime.datetime.now()
print("date & Time")
print(now.strftime("%d/%m/%y, %H:%M:%S"))


First_Name=input("Enter First name")
Last_Name= input("Enter Last name")
Full_Name=Last_Name+First_Name
print(Full_Name)
print(Full_Name[::-1])

Amount=["Abdullah", "Ali", 25000, 35000, 100000]

total=0
for num in Amount:
    if isinstance(num,(int, float)):
      total+= num
print("The Sum Of the Amount is:", total)     

import math
radius=float(input("ENter The area of the circle"))
area=math.pi*radius**2

print("The area of the circle is:", area)

list=[1,2,3,4,5,56,100,1000,50,50000]

for num in list:
   if num<100:
      print(num)

Numbers=int(input("Enter Number"))
if Numbers%2==0:
   print("This Number is even:", Numbers)
else:
   print("This Number is Odd:", Numbers)   


Student_name=input("Enter Student Name")
Class=int(input("Enter Class No"))
English_Marks=int(input("Enter English Marks"))
Urdu_Marks=int(input("Enter Urdu Marks"))
Maths_Marks=int(input("Enter Maths Marks"))
Computer_Marks=int(input("Enter Computer Marks"))
Science_Marks=int(input("Enter Science Marks"))
Obtained_Marks=(English_Marks+Urdu_Marks+Maths_Marks+Computer_Marks+Science_Marks)
Total_Marks=500
Percentage=Obtained_Marks/Total_Marks*100

print(Student_name)
print(Class)
print("Marks:")
print(English_Marks)
print(Urdu_Marks)
print(Maths_Marks)
print(Computer_Marks)
print(Science_Marks)
print(Obtained_Marks, Total_Marks)
print( f"{Percentage}%")

if Percentage>=90 and Percentage<100:
   print("Grade: A++")
elif Percentage>=80 and Percentage<90:
   print("Grade: A+")
elif Percentage>=70 and Percentage<80:
   print("Grade: A")
elif Percentage>=60 and Percentage<70:
   print("Grade: B")
elif Percentage>=50 and Percentage<60:
   print("Grade: C")
elif Percentage>=40 and Percentage<50:
   print("Grade: D")   
else:
   print("You are Failed")
   

