# 05/14/2026  Honour Okhavhe CIS106-001



# ==========================================
# Problem 1: Compound Interest
# ==========================================
def prob1_compound_interest():
    print("\n--- Problem 1: Compound Interest ---")
    while True:
        try:
            principal = float(input("Enter principle amount: "))
            rate = float(input("Enter interest rate (e.g., 0.10): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        print(f"\n{'Year':<10} {'Beginning':<15} {'Ending'}")
        print(f"{'':<10} {'Balance':<15} {'Balance'}")
        
        current_balance = principal
        total_interest = 0.0

        for year in range(1, 6):
            annual_interest = current_balance * rate
            ending_balance = current_balance + annual_interest
            total_interest += annual_interest
            
            print(f"{year:<10} ${current_balance:,.2f}{'':<4} ${ending_balance:,.2f}")
            
            current_balance = ending_balance

        print(f"Total interest earned: ${total_interest:,.2f}")
        
        again = input("\nCalculate another? (y/n): ").strip().lower()
        if again != 'y':
            break

# ==========================================
# Problem 2: Fibonacci Sequence
# ==========================================
def prob2_fibonacci():
    print("\n--- Problem 2: Fibonacci Sequence ---")
    a, b = 1, 1
    print(f"1: {a}")
    print(f"2: {b}")
    
    # Loop 18 times to get the remaining 18 numbers (20 total)
    for i in range(3, 21):
        next_num = a + b
        print(f"{i}: {next_num}")
        a = b
        b = next_num

# ==========================================
# Problem 3: Employee Bonuses (File I/O)
# ==========================================
def prob3_bonuses():
    print("\n--- Problem 3: Employee Bonuses ---")
    total_bonuses = 0.0
    
    try:
        with open('employees.txt', 'r') as file:
            while True:
                name = file.readline().strip()
                if not name:
                    break # End of file
                
                salary_str = file.readline().strip()
                salary = float(salary_str)
                
                if salary >= 100000:
                    rate = 0.20
                elif salary >= 50000:
                    rate = 0.15
                else:
                    rate = 0.10
                    
                bonus = salary * rate
                total_bonuses += bonus
                
                print(f"Employee: {name:<12} Salary: ${salary:<10,.2f} Bonus: ${bonus:,.2f}")
                
        print(f"\nSum of all bonuses paid out: ${total_bonuses:,.2f}")
    except FileNotFoundError:
        print("Error: 'employees.txt' not found. Please create it.")

# ==========================================
# Problem 4: Extended Prices (File I/O)
# ==========================================
def prob4_orders():
    print("\n--- Problem 4: Order Parsing ---")
    total_extended_prices = 0.0
    order_count = 0
    
    try:
        with open('orders.txt', 'r') as file:
            print(f"{'Item':<10} | {'Qty':<5} | {'Price':<8} | {'Extended'}")
            print("-" * 40)
            
            while True:
                item = file.readline().strip()
                if not item:
                    break
                
                qty = int(file.readline().strip())
                price = float(file.readline().strip())
                
                extended_price = qty * price
                total_extended_prices += extended_price
                order_count += 1
                
                print(f"{item:<10} | {qty:<5} | ${price:<7.2f} | ${extended_price:,.2f}")
                
        if order_count > 0:
            average_order = total_extended_prices / order_count
            print("-" * 40)
            print(f"Total of extended prices: ${total_extended_prices:,.2f}")
            print(f"Total number of orders:   {order_count}")
            print(f"Average order amount:     ${average_order:,.2f}")
    except FileNotFoundError:
        print("Error: 'orders.txt' not found. Please create it.")

# ==========================================
# Problem 5: Student Tuition (File I/O)
# ==========================================
def prob5_tuition():
    print("\n--- Problem 5: Student Tuition ---")
    total_tuition = 0.0
    student_count = 0
    
    try:
        with open('students.txt', 'r') as file:
            print(f"{'Student':<10} | {'Credits':<8} | {'Tuition Owed'}")
            print("-" * 35)
            
            while True:
                name = file.readline().strip()
                if not name:
                    break
                
                district_code = file.readline().strip().upper()
                credits = int(file.readline().strip())
                
                if district_code == 'I':
                    cost_per_credit = 250.00
                else:
                    cost_per_credit = 500.00
                    
                tuition = credits * cost_per_credit
                total_tuition += tuition
                student_count += 1
                
                print(f"{name:<10} | {credits:<8} | ${tuition:,.2f}")
                
        print("-" * 35)
        print(f"Sum of all tuition owed: ${total_tuition:,.2f}")
        print(f"Total number of students: {student_count}")
    except FileNotFoundError:
        print("Error: 'students.txt' not found. Please create it.")

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    prob1_compound_interest()
    prob2_fibonacci()
    prob3_bonuses()
    prob4_orders()
    prob5_tuition()