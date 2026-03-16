


ApplianceName = input("Enter Appliance Name:   ")
ApplianceCost = float(input("Enter Appliance Cost:  "))

if ApplianceCost > 1000:
    warranty =  ApplianceCost * 0.10
else : warranty = ApplianceCost * 0.05

TotalCost = ApplianceCost + warranty

print("ApplianceName : ",ApplianceName)
print("ApplianceCost : ",ApplianceCost)
print("Warranty : ",warranty)
print("TotalCost : ",TotalCost)






