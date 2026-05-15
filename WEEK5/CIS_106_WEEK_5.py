# 03/14/2026  Honour Okhavhe CIS106-001 Week5Question1


Quantity = int(input("Enter Quantity Of Widgets:  "))


if Quantity > 10000 :
    Price = 10
elif Quantity >= 5000 :
    Price = 20 
else : 
    Price = 30


ExtendedPrice = Quantity*Price
Tax = ExtendedPrice*0.07
TotalPrice = ExtendedPrice + Tax


print("ExtendedPrice :  $",ExtendedPrice)
print("Tax :  $",Tax)
print("TotalPrice  :  $",TotalPrice)

