# 05/14/2026  Honour Okhavhe CIS106-001



def compute_sales_metrics(sales):
    """Computes commission and next year's target based on sales."""
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
        
    next_year_target = sales * 0.05
    return commission, next_year_target

def main_prob3():
    print("--- Problem 3: Sales Report ---")
    last_name = input("Enter salesperson's last name: ")
    sales_amount = float(input("Enter total sales: $"))
    
    comm, target = compute_sales_metrics(sales_amount)
    
    print("\n--- Salesperson Report ---")
    print(f"Name: {last_name}")
    print(f"Commission Earned: ${comm:,.2f}")
    print(f"Next Year's Target: ${target:,.2f}\n")

main_prob3()