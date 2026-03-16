



NumberOfBooks = int(input("Enter the Number Of Books:  "))
CostPerBook = float(input("Enter the cost per book:   "))

OrderTotal = NumberOfBooks*CostPerBook

if OrderTotal > 50 :
    ShippingFee = 0 
else : ShippingFee = 25


print ("Order total: ", OrderTotal)
print ("Shipping fee: ", ShippingFee)







