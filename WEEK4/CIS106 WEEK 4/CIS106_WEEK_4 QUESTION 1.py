



quantity = int(input("enter quantity of an item"))
if quantity >= 1000:
    unitprice = 3.00
if quantity < 1000:
    unitprice = 5.00
extendedprice = quantity*unitprice
tax = extendedprice*7/100
total = extendedprice + tax

print (quantity)
print (unitprice)
print (extendedprice)
print (tax)
print (total)
