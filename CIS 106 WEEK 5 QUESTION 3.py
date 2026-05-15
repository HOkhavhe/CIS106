# 03/14/2026  Honour Okhavhe CIS106-001 Week5Question3


Principal = float(input("Enter Principal Amount : "))
Years = int(input("Enter years to maturity : "))


if Principal > 100000 and Years == 5 :
    rate = 0.06
elif 50000 <= Principal <= 100000 and Years == 10 :
    rate = 0.05
elif 50000 <= Principal <= 100000 and Years == 5 :
    rate = 0.04
else:
    rate = 0.02


Interest = Principal * rate


print("Principal: $", Principal)
print("Interest Rate: ", rate * 100, "%")
print("First Year Interest: $", Interest)


