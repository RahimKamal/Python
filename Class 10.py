# What is Function?

# Pre define Function 
"""
input()
print()
append.
datetime
sys
math
"""
# User Define Function

# In function you have to add def before applying the Function

# For Example

def addition():
    Num_1=56
    Num_2=56
    Total=Num_1+Num_2
    print(Total)

#  in the Function it will not give you the output with calling the function
#  For Example

# Positional Argument
addition()
# Now it will give you the Output

def addition(a,b):   #when you write any value in this round braces it will be called Parameter
    
    Total=a+b
    print(Total)

addition(100,200)  #when you write any value in this round braces it will be called Argument



# Now it will give you the Output

def addition(a,b):   #when you write any value in this round braces it will be called Parameter
    Total=a+b
    print(Total)
a=40
b=45
addition(a,b)  #when you write any value in this round braces it will be called Argument

def full_name(First_Name,Last_name):

   Complete_Name=First_Name+Last_name
   print(Complete_Name)

full_name("Rahim","Daddy")

full_name(First_Name="Rahim",Last_name="Daddy")
# when you define key it is called keywords argument