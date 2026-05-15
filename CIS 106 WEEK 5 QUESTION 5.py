# 03/14/2026  Honour Okhavhe CIS106-001 Week5Question5


LastName = input("Enter employee last name : ")
Salary = float(input("Enter Salary : "))
JobLevel = int(input("Enter Job Level : "))


if JobLevel >= 10 :
    Rate = 0.25
elif JobLevel >= 5 :
    Rate = 0.20
else : 
    Rate = 0.10


Bonus = Salary * Rate 


print("LastName : ", LastName)
print("Bonus : $ ", Bonus)

