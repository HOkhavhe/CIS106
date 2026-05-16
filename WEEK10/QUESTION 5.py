# 05/14/2026  Honour Okhavhe CIS106-001


# Initialize global variables at the top of the script
total = 0.0
tax = 0.0

def compute_global_totals(quantity, unit_price):
    """Computes total and tax, modifying global variables directly."""
    # The 'global' keyword tells Python we want to modify the variables defined outside this function
    global total
    global tax
    
    total = quantity * unit_price
    tax = total * 0.07

def main_prob5():
    print("--- Problem 5: Global Variables ---")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: $"))
    
    # We don't need to capture returned variables because the function modifies the globals
    compute_global_totals(qty, price)
    
    print("\n--- Transaction Summary ---")
    print(f"Total Amount: ${total:,.2f}")
    print(f"Tax Amount (7%): ${tax:,.2f}\n")

main_prob5()
