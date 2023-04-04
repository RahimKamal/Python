"""
What is Tuples ?
 Tuple is identify by () Round Braces, it's also a list like array,
 we can'nt edit and change the value & the elements in Tuple. 
"""
# Make your Own Calculator.


Val1=int(input("Enter Value 1"))
Val2=int(input("Enter Value 2"))
Operator=input("Enter Operator")

if Operator== "+": 
    Value=Val1+Val2
    print(Value, "Answer")
elif Operator == "-": 
    Value= Val1-Val2
    print(Value, "Answer")
elif Operator == "*": 
    Value= Val1*Val2
    print(Value, "Answer")
elif Operator == "/": 
    Value= Val1/Val2
    print(Value, "Answer")        
else:
    print("Please Enter correct Value")

Cleaniest_Cities= ["Karachi", "Islamabad", "Lahore", "Quetta"]
 
Value= input("Enter City Name")
for Cleanest_City in Cleaniest_Cities:
       if Value == Cleanest_City:
         print("Shahab is in cleanest city")
else:
    print("Shahab is not in a Cleanest city") 

Value= input("Enter Value")
if Value== "Islamabad":
    print("Shahab is in a Cleanest City")
elif Value== "Lahore":
    print("Shahab is in a Cleanest City")
elif Value== "Quetta":
    print("Shahab is in a Cleanest City")
else: 
    print("Shahab Is in a Dirtest City")    


        
