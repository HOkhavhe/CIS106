

LastName = input("enter last name:  ")
NumberOfDependents = int(input("enter number of dependents:  "))
GrossIncome = float(input("enter gross income:  "))

AdjustedGrossIncome = GrossIncome - (NumberOfDependents * 12000)

if AdjustedGrossIncome > 50000 :
   TaxRate = 0.20
else : TaxRate = 0.10

IncomeTax = AdjustedGrossIncome * TaxRate

if IncomeTax < 0 :
   IncomeTax = 100


print("LastName: ", LastName)
print("GrossIncome: $", GrossIncome)
print("NumberOfDependents: ", NumberOfDependents)
print("AdjustedGrossIncome: $", AdjustedGrossIncome)
print("IncomeTax: $", IncomeTax)





