# 05/14/2026  Honour Okhavhe CIS106-001


def compute_discount(quantity, price, discount_rate):
    """Computes discount amount and final discounted price."""
    subtotal = quantity * price
    # Assuming discount_rate is provided as a decimal (e.g., 0.10 for 10%)
    discount_amount = subtotal * discount_rate
    discounted_price = subtotal - discount_amount
    return discount_amount, discounted_price

def main_prob1():
    print("--- Problem 1: Discount Calculator ---")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: $"))
    rate = float(input("Enter discount rate (as a decimal, e.g., 0.15 for 15%): "))
    
    # Call function and unpack the two returned values
    disc_amt, final_price = compute_discount(qty, price, rate)
    
    print("\n--- Receipt ---")
    print(f"Quantity: {qty}")
    print(f"Unit Price: ${price:,.2f}")
    print(f"Discount Amount: ${disc_amt:,.2f}")
    print(f"Discounted Final Price: ${final_price:,.2f}\n")

main_prob1()