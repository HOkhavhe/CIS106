

item = input ("Enter item (A or B):  ")
quantity = int(input("Enter quantity:  "))

if item == "A" :
   unit_price = 10.00
else :
    unit_price = 20.00

ExtendedPrice = quantity*unit_price


print(item)
print("Unit Price:  $",unit_price)
print("ExtendedPrice:  $",ExtendedPrice)
