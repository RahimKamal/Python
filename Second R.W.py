# Cash=["Absullah", "Ali", 5000, 1000, 100000]

# total=0

# for item in Cash:
#    if isinstance(item, (int, float)):
#       total+= item
# print("The sum of all Numeric values", total) 

# Cash= ["Hello", "Ali", "Abdullah",56000, 25000, 98000]
# # we have to make total=0 to refining(iterate) the Numeric Values.

# total=0
#     #we use 'for' to iterate(Refining) the data
# for item in Cash:  
# # we use isinstance to specify the data 
#     if isinstance(item, (int, float)):
#         #add item to the total sum
#      total+= item 
# print("The Sum Of All MNumeric Items in the list", total)        


# # import sys
# # print("Python Version")
# # print(sys.version)
# print("Version Info")
# print(sys.version_info)

# import datetime
# now=datetime.datetime.now()
# print("date & Time")
# print(now.strftime( "%d/%m/%Y, %H:%M:%S"))

# FIrst_name= input("Enter Your Name")
# Last_name= input("Enter Your Name")
# Full_name= Last_name+FIrst_name
# print(Full_name)
# print(Full_name[::-1])

Student_name= input("Enter Student name")
Class=input("Enter Class no")
English_Marks=int(input("Enter English Marks"))
Urdu_Marks=int(input("Enter Urdu Marks"))
Maths_Marks=int(input("Enter Maths Marks"))
Islamiat_Marks=int(input("Enter Islamiat Marks"))
Computer_Marks=int(input("Enter Computer Marks"))
obtained_Marks=(English_Marks+Urdu_Marks+Maths_Marks+Islamiat_Marks+Computer_Marks)
Total_Marks=500
Percentage=(obtained_Marks/Total_Marks*100)
Percentage=(obtained_Marks/Total_Marks*100)


if Percentage>= 90 and Percentage<=100:
    print("Grade: A++")

elif Percentage>= 80 and Percentage<=90:
    print("Grade: A++")
elif Percentage>= 70 and Percentage<=80:
    print("Grade: A++")
elif Percentage>= 60 and Percentage<=70:
    print("Grade: A++")
elif Percentage>= 50 and Percentage<=60:
    print("Grade: A++")
elif Percentage>= 40 and Percentage<=50:
    print("Grade: A++")                    
else:
    print("You are Failed")
print("Mark Sheet")
print("Student Name:", Student_name)
print("Class:",Class)
print("Marks")
print("English:",English_Marks)
print("Urdu",Urdu_Marks)
print("Maths:",Maths_Marks)
print("Islamiat:",Islamiat_Marks)
print("Computer:",Computer_Marks)

print(obtained_Marks, Total_Marks)
print( f"{Percentage} %")

import math
radius=float(input("Enter the area of the circle"))
Area= math.pi*radius**2
print("The are of The Circle is:", Area)

Array=["Ali", "Abdullah", "Zaid", "Shahab", "<My Son", "Apka Daddy"]
print(Array)
Array.append("Ajaao Haveli Pr")

print(Array)
Array.insert(2, "Chowk Me daddyy")
print(Array)
Array[4]="Mera Beta"



Calculation=["Ali","Abdullah", "Saim", "Rahim", 1000,1500,3000,2500]
total=0
for item in Calculation:
    if isinstance(item, (int, float)):
        total+=item
print("The Sum of all Numeric",Calculation)

List=[10,20,30,40,50,100,1500,15000]
for num in List:
    if num%2==0:
        print(num)
        
        