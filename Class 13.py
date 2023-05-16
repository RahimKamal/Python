Elements= []

while True:

    print("Element in our list")
    for element in Elements:
        print("->" + element)

    print(" Options")
    print("1. Add Element") 
    print("2. Delete Element")
    print("3. Delete All Element")
    print("4. Exit")
    print("Note: Please give input in number e.g: 1, 2, 3, 4")

    Inp= input("Enter Your Choice")

    if Inp== "1":
        Elements.append(input("Enter Your Element:"))
    elif Inp== "2":
        Elements.remove(input("Enter Element to delete:"))
    elif Inp== "3":
        Elements.clear()
    elif Inp== "4":
        break
else:
     print("Invalid input")
     

    
                                            