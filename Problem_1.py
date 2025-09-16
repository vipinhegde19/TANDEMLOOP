#calculator
A=int(input("Enter the First Number: "))
B=int(input("Enter the First Number: "))

Op=input("Enter the operations: \n 1.Addition +: \n2.Substraction -: \n3.Multiplication *: \n4.Division /: \n")
if Op=="1" or Op=="+":
    print(f"{A} + {B} ={A+B}")
if Op=="2" or Op=="-":
    print(f"{A} - {B} ={A-B}")
if Op=="3" or Op=="*":
    print(f"{A} * {B} ={A*B}")
if Op=="4" or Op=="/":
    print(f"{A} / {B} ={A/B}")
