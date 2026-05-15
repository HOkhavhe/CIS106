# 03/14/2026  Honour Okhavhe CIS106-001 Week5Question2


PartNumber = input("Enter Part Number : ")
Quantity = int(input("Enter Quantity :  "))


if PartNumber == "10" or PartNumber == "55" :
   UnitCost = 1.00
elif PartNumber == "99" :
   UnitCost = 2.00
elif PartNumber == "80" or PartNumber == "70" :
   UnitCost = 3.00
else : 
    UnitCost = 5.00


TotalCost = Quantity * UnitCost

print("PartNumber :", PartNumber)
print("UnitCost : $", UnitCost)
print("TotalCost :  $", TotalCost)