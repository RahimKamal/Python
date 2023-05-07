Num1=10
Num2=5

def AddNum(Num2,Num1):
    Result=Num1-Num2
    print(Result)

AddNum(Num1,Num2)

def My_Function(Rahim_has=50, Shahab_has=40):
    Spent_in_Fries= Rahim_has-Shahab_has
    print(Spent_in_Fries)

My_Function(60,55) 


def My_Course(Institute,Language, Duration="3 Months" ):
    print(Institute+Language+Duration)
#In Python when you define any value of parameter, you have to write it in the end of the function like in the upper function.

Institute= "Rahim Inst"
Language= " Python"
Duration= "  1 Month"

My_Course("Rahim Inst", "Python", "1 Month")