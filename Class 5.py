#elif statement means multiple if statement

per= int(input("Enter Percentage%"))
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

a=11
b=10
c=15
d=15
e=18
f=10
g=50
h=0
if a==b or e==f and c==d :
        g=h
        print(g)
elif a==b: 
        g=h
        print(g)        
else:
        e=f
        print(e) 
"""
# '  Array: is the list of the elements in one bracket
# '  Index is the sequences no the elements which are in the square bracket of array.
# ' For Example: ["Ali", "Abdullah", "Haris", False, 25, 65, 100]
# ' Index Number:[  0        1          2      3     4   5   6 ]

"""
arr= ["Abdullah", "Ali", "Osama","Haris", "Zaid"]
print(arr[1])
arr.append("Umer")
print(arr)

arr1= arr+["Raheem, Muneeb"]
print(arr1)

# when you want to insert any value or element in the place of any array number
# you have to do arr1.insert(2, "Don Bhai")

arr1.insert(2, "my son")
print(arr1)
#  if you want to change the value of any array
# for Example
arr1[3]= "Asad"

print(arr1)

arr1[5]="Nach meri bulbul tujhe paisa milega"
print(arr1)

# when you want specific output from the list of array the use this code 
arr2=arr1[2:7] #7 means it will use 6 because it takes starting number till second last number 
print(arr2)
 #if you want to get ouput only limited list from the array then use thois code
arr3=arr1[:6]
print(arr3)
#when you wanna delete any array from the list
del arr1[3]
print(arr1)

#Nested if statement
num= 18
if num<0:
    print("Number is Negative")
elif num>0:
    if num<=10:
        print("Num is Between 1-10")
    elif num >10 and num<=20:
       print("Number is betweek 11-20")   
    else:
       print("Num is Greater Than 20")

else:
    print("Number Is Zero")
       
