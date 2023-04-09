# List Of dictionary?

Questions= [
    {
        "SNo.": 1,
        "Question" : "What is Python",
        "Options"  : ["1.Computer Language, 2.Binary Language, 3.Human Language"],
        "Answer" : "Computer Language"
    
    },
    {
      "S.No": 2,
        "Question" : "What is C++",
        "Options"  : ["1.Computer Language", "2.Binary Language", "3.Human Language"],
        "Answer" : "Computer Language"
    
    },
    { 
     "S.No": 3,
        "Question" : "What is R",
        "Options"  : ["1.Computer Language, 2.Binary Language, 3.Human Language"],
        "Answer" : "Computer Language"
    
    }
]



# How to get Information from the list of dictionary
print(Questions[1])

# How to get specific information from the specific Dictionary

print(Questions[0]["Options"])


New_Question=[
    { "Question" : "Who is Shahab",
        "Options"  : ["1.Computer, 2.My Son, 3.Bike, 4. My Friend"],
        "Answer" : "My Son"}
]

#How to add another dictionary in the list

Questions.append(New_Question)
print(Questions)

#How to get Specific key from the specific dictionary of the list

print(Questions[1]["Options"][1])


# How to make dictionary in dictionary?

Students= {
    1:{ "Name":"Shahab",
        "Age": 22,
        "Gender":"Apki Marzi",
        "Son of": "Rahim Daddy"  },
    2:{ "Name":"Shayan",
        "Age": 23,
        "Gender":"Male",
        "Son of": "Aehle Muhallah"  },
    3:{ "Name":"Usman",
        "Age": 24,
        "Gender":"Not identify",
        "Son of": "Rahim Daddy"  }
}

print(Students)

# How to get Information of a specific key
print(Students[1])