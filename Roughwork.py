# ROUGH WORK FILE

# # om = 560
# # tm = 600
# # p = om  / tm
# # p= p*100
# # print( f"{p} %") # String Interpolation

# # r= 15 % 2
# # print(r)

# Student_name=input("Enter Student Name")
# Class_Name= int(input("Enter Class No"))
# Urdu_Marks= int(input("ENter Urdu Marks"))
# Maths_Marks= int(input("ENter Math Marks"))
# Science_Marks= int(input("ENter Science Marks"))
# English_Marks= int(input("ENter English Marks"))
# Computer_Marks= int(input("ENter Computer Marks"))
# Obtained_Marks=(Urdu_Marks+Maths_Marks+Science_Marks+English_Marks+Computer_Marks)
# Total_Marks= 500
# Percentage=(Obtained_Marks/Total_Marks*100)
# print("Student Name:", Student_name)
# print("Class:", Class_Name)
# print("Marks")
# print("Urdu:", Urdu_Marks) 
# print("Math:", Maths_Marks) 
# print("Science:", Science_Marks) 
# print("English:", English_Marks) 
# print("Computer:", Computer_Marks) 
# print("Obtained Marks:", Obtained_Marks , ", Total Marks:", Total_Marks)
# print( "Percentage:", f"{Percentage}%") #str Interpolation Applied
# if Percentage>= 90 and Percentage<=100:
#     print("Grade: A++")
# elif Percentage>= 80 and Percentage<90:
#     print("Grade: A+")
# elif Percentage>= 70 and Percentage<80:
#     print("Grade: A")
# elif Percentage>= 60 and Percentage<70:
#     print("Grade: B")
# elif Percentage>= 50 and Percentage<60:
#     print("Grade: C")

# elif Percentage>= 40 and Percentage<50:
#     print("Grade: D")
# else:
#     print("You are Failed")

# a= 25
# b=50
# c= b%a
# # print(c)

# Num= int(input("Enter Number"))
# if Num % 2 ==0:
#     print(Num,"Number is Even")
# else:
#     print(Num, "Number is Odd")  


# CLass_room= ["Ali", "Abdullah", "Haris", "Wasay", "Rahim Daddy"]
# print(len(CLass_room))
# Shahab= "SHAHAB HAS BEEN BORROWED 4 MILLION RUPEES FROM ME"
# Shahab= Shahab.lower()
# # print(Shahab)     

# import sys

# print("Python Version")
# print(sys.version)
# print("Version Info")
# print(sys.version_info)


# import datetime
# now=datetime.datetime.now()
# print("Date & Time")
# print(now.strftime("%d/%m/%y   %H:%M:%S"))


# First_Name= input("Enter First Name")
# Last_name= input("Enter Last Name")
# Full_name= First_Name+Last_name
# print(Full_name)
# print(Full_name[::-1])


# import math
# radius=float(input("EnterThe are of the circle"))
# area= math.pi*radius**2
# print("The are of the circle is", area)

# Student_Name= input("Enter Student Name")
# Class= int(input('Enter Class No'))
# English_Marks=int(input("Enter English Marks"))
# Math_Marks=int(input("Enter Maths Marks"))
# Urdu_Marks=int(input("Enter Urdu Marks"))
# Science_Marks=int(input("Enter Science Marks"))
# Computer_Marks=int(input("Enter Computer Marks"))

# obtained_marks= (English_Marks+Math_Marks+Urdu_Marks+Science_Marks+Computer_Marks)
# Total_marks= 1000
# Percentage= obtained_marks/Total_marks*100
# print(Student_Name)
# print(Class)
# print("Marks:")
# print("Englis:", English_Marks)
# print('Maths:', Math_Marks)
# print("Urdu:", Urdu_Marks)
# print("Computer", Computer_Marks)
# print("Science", Science_Marks)
# print(obtained_marks, Total_marks)

# if Percentage>= 90 and Percentage<100:
#     print("Grade:A++")
# if Percentage>= 80 and Percentage<90:
#     print("Grade:A+")
# if Percentage>= 70 and Percentage<80:
#     print("Grade:A")
# if Percentage>= 60 and Percentage<70:
#     print("Grade:B")
# if Percentage>= 50 and Percentage<60:
#     print("Grade:C")
# if Percentage>= 40 and Percentage<50:
#     print("Grade:D")
# else:
#     print("You are Failed")    


# arr=["Ali", "Abdullah", "Wasay", "Shayan", 10000,500000, 100000]

# arr.append("Rahim Daddy")
# print(arr)
# arr.insert(3,"My Son")
# print(arr)
# del arr[3]
# print(arr)

# a=["Absullah", "Ali", 5000,1000]
# total=0
# for items in a:
#     if isinstance(items,(int, float)):
#         total=+ items
# print("The sum of all Numeric values", a) 

list=[10,15,20,25,50,100,1000,10000,25000,650000,80,]

Number=int(input("Enter Number"))

if Number%2==0:
        print(Number,"This Number Is even")

else:
     print(Number, "This Number is Odd")

# for num in list:
#     if num<100:
#         print(list) 


list=[10,20,30,40,50,100]

for num in list:
       if num<50:
              print(num)