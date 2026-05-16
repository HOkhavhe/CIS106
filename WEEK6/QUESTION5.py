04/15/26   Honour Okhavhe CIS106-001



# Problem 5: Order Discounts

sum_of_discounts = 0

# Prompt the user on whether they want to do this program 
run_program = input("Do you want to process an order? (Enter 'Yes' to continue): ")

# If the user answers Yes then go into the while loop [cite: 33]
while run_program == "Yes":
    # Prompt the user for quantity and price of an item 
    quantity = int(input("Enter the item quantity: "))
    price = float(input("Enter the item price: "))
    
    # Compute extended price (quantity times price of an item) 
    extended_price = quantity * price
    
    # If the extended price is greater than 10000.00 compute a discount of 25%. All other orders get a 10% discount. 
    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10
        
    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount
    
    # For each order sum the discount amount 
    sum_of_discounts += discount_amount
    
    # For each order display extended price, discount amount, total 
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")
    
    # Second prompt at the bottom, inside the loop [cite: 36]
    run_program = input("Do you want to do this loop again? (Enter 'Yes' to continue): ")

# After the loop (all data entered) display the sum of all the discounts 
print(f"Sum of all discounts applied: ${sum_of_discounts:.2f}")