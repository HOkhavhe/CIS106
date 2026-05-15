# 03/14/2026  Honour Okhavhe CIS106-001 Week5Question4



Tickets = int(input("Enter number of tickets: "))


if Tickets >= 25:
    price = 50
elif Tickets >= 10:
    price = 60
elif Tickets >= 5:
    price = 70
else:
    price = 75


Totalcost = Tickets * price


print("Tickets:", Tickets)
print("Price per Ticket: $", price)
print("Total Cost: $", Totalcost)
