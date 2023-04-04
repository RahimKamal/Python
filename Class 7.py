First_Name= ["Abdullah","Ali", "Osama", "Wasay", "Nasar", "Nazir"]
Last_Name= [ "Wajiod","Rex", "Alx","Fiona Allison"]
Full_Name=[]

# append will plus each name from First Name with from last Name
for a_First_name in First_Name:
    for a_Last_name in Last_Name:
        Full_Name.append(a_First_name+ "" +a_Last_name)
        # print(Full_Name)

# How to change Case of any Statement?
Shahab= "SHAHAB HAS BEEN BORROWED 4 MILLION RUPEES FROM ME"
Shahab= Shahab.lower()
print(Shahab)        

Muneeb= " muneeb has chicknot bachi"
Muneeb=Muneeb.upper()
print(Muneeb)

Tehreem= "HAS NO WEALTH"
print(Tehreem.lower())

Wasay= "has small head"
print(Wasay.title())

#Dictionary

a= ("Name:Shahab , Age: 22,  Sex: Twice a Day")
print(a)

Customer_01599= {"Name": "Shahab",
                 " Age" : "22",
                 " Gender": "Apki Marzi",
                 "Baap Ki Age" : "23"}
# print(Customer_01599)

print(Customer_01599["Name"])
print(Customer_01599)
# how to add new key with the value?
Customer_01599["Baap Ka Naam"]= "Rahim Daddy"
print(Customer_01599)

#How to Delete any key?
del Customer_01599["Baap Ki Age"]
print(Customer_01599)

#How to Know only Keys?
for each_value in Customer_01599.keys():
    print(each_value)
#How to Know only Values?

for each_value in Customer_01599.values():
    print(each_value)    