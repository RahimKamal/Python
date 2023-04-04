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
elif not re.search("[0-9]", Password):
       print("Your Password Should Contain at least One digit")
else:
    ("Password is too Strong")        


Weight=float(input("Enter Weight"))
Height=float(input("Enter Height"))

BMI= Weight/Height**2
if BMI<18.5:
     message= "Underweight"

elif BMI<25:
     message="Normal Weight"
elif BMI<30:
     message="Over Weight"
else:
     message= "Obese"
print(f"Your BMI is {BMI}, which is considered {message}.")


# Rock-Paper-Scissors Game: Write a program that simulates a game of Rock-Paper-Scissors.
#  The user should be prompted to enter their choice and the program should randomly
#  generate a choice for the computer. 
# The program should then display the winner based on the rules of the game.