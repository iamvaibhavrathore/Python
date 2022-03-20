#********** if Statement ***************
a=int(input("Enter the value:- "))
if a%2==0:
    print(a,"Even Number") 

#********* if else ************

a=int(input("Enter the value:- "))
if a%2==0:
    print(a,"Even Number") 
# print("Error Wrong indentation")
    print("Correct Indentation")  
else:
    print(a, "Odd Number")


#************ if elif else statement **************
nw=int(input("Enter the value:- "))
if nw>=60:
    print("First Dev")
elif nw>=48:
    print("Seconf Dev")
elif nw>=35:
    print("third Dev")
else:
    print("Fail")    