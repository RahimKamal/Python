

Questions= [
    {
        "S.No": 1,
        "Question" : "What is Python",
        "Options"  : ["1.Computer Language", "2.Binary Language", "3.Human Language"],
        "Answer" : "1"
    
    },
    {
      "S.No": 2,
        "Question" : "What is C++",
        "Options"  : ["1.Computer Language", "2.Binary Language", "3.Human Language"],
        "Answer" : "1"
    
    },
    { 
     "S.No": 3,
        "Question" : "What is R",
        "Options"  : ["1.Computer Language", "2.Binary Language", "3.Human Language"],
        "Answer" : "1"
    
    }
]
#Score is always initially 0 by default score=0
Score= 0

for question in Questions:
    Data = str(question["S.No"]) + ": " + question["Question"] + "\n" + ", ".join(question["Options"]) + "\n"    
    Answer=input(Data)
    if Answer == question["Answer"]:
        Score +=1 

print("yourScore is:", str(Score))