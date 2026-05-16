# 05/14/2026  Honour Okhavhe CIS106-001


# ==========================================
# Problem 1: Quantity, Price, and Discount
# ==========================================
def compute_total(quantity, price):
    """Computes total and applies a 10% discount if over $10,000."""
    total = quantity * price
    if total > 10000.00:
        total = total * 0.90  # Apply 10% discount
    return total

def problem_1():
    print("\n--- Problem 1: Total & Discount ---")
    sum_extended_price = 0.0
    
    while True:
        run = input("Do you want to run the program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: $"))
        
        total = compute_total(qty, price)
        sum_extended_price += total
        
        print(f"\nQuantity: {qty}")
        print(f"Price: ${price:,.2f}")
        print(f"Total: ${total:,.2f}\n")
        
    print(f"Sum of extended prices: ${sum_extended_price:,.2f}")


# ==========================================
# Problem 2: Batting Average
# ==========================================
def compute_batting_average(hits, at_bats):
    """Computes batting average."""
    if at_bats == 0:  # Prevent division by zero
        return 0.0
    return hits / at_bats

def problem_2():
    print("\n--- Problem 2: Batting Average ---")
    player_count = 0
    
    while True:
        run = input("Do you want to run the program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        last_name = input("Enter player's last name: ")
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at bats: "))
        
        avg = compute_batting_average(hits, at_bats)
        player_count += 1
        
        print(f"\nPlayer: {last_name}")
        print(f"Batting Average: {avg:.3f}\n")
        
    print(f"Total number of players entered: {player_count}")


# ==========================================
# Problem 3: Trip Miles Per Gallon (MPG)
# ==========================================
def compute_mpg(miles, gallons):
    """Computes miles per gallon."""
    if gallons == 0: # Prevent division by zero
        return 0.0
    return miles / gallons

def problem_3():
    print("\n--- Problem 3: Trip MPG ---")
    trip_count = 0
    
    while True:
        run = input("Do you want to run the program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        city = input("Enter destination city: ")
        miles = float(input("Enter miles travelled: "))
        gallons = float(input("Enter gallons used: "))
        
        mpg = compute_mpg(miles, gallons)
        trip_count += 1
        
        print(f"\nDestination: {city}")
        print(f"Miles Travelled: {miles:.1f}")
        print(f"MPG: {mpg:.1f}\n")
        
    print(f"Total number of trips entered: {trip_count}")


# ==========================================
# Problem 4: Payroll and Overtime
# ==========================================
def determine_pay_rate(job_code):
    """Returns the hourly pay rate based on job code."""
    code = job_code.strip().upper()
    if code == 'L':
        return 25.00
    elif code == 'A':
        return 30.00
    elif code == 'J':
        return 50.00
    else:
        return 0.00  # Default for invalid codes

def problem_4():
    print("\n--- Problem 4: Payroll ---")
    total_gross_pay = 0.0
    
    while True:
        run = input("Do you want to run the program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        last_name = input("Enter employee's last name: ")
        job_code = input("Enter job code (L, A, or J): ")
        hours = float(input("Enter hours worked: "))
        
        rate = determine_pay_rate(job_code)
        
        # Calculate Overtime (time and a half for hours over 40)
        if hours > 40:
            regular_pay = 40 * rate
            overtime_pay = (hours - 40) * (rate * 1.5)
            gross_pay = regular_pay + overtime_pay
        else:
            gross_pay = hours * rate
            
        total_gross_pay += gross_pay
        
        print(f"\nEmployee: {last_name}")
        print(f"Gross Pay: ${gross_pay:,.2f}\n")
        
    print(f"Total of all gross pay: ${total_gross_pay:,.2f}")


# ==========================================
# Problem 5: College Tuition
# ==========================================
def compute_tuition(credit_hours, district_code):
    """Computes tuition based on district code and credits."""
    code = district_code.strip().upper()
    if code == 'I':
        return credit_hours * 250.00
    elif code == 'O':
        return credit_hours * 550.00
    else:
        return 0.00 # Default for invalid codes

def problem_5():
    print("\n--- Problem 5: Tuition Calculator ---")
    total_tuition_owed = 0.0
    
    while True:
        run = input("Do you want to run the program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        last_name = input("Enter student's last name: ")
        credits = int(input("Enter credit hours: "))
        district_code = input("Enter district code (I for In-District, O for Out-of-District): ")
        
        tuition = compute_tuition(credits, district_code)
        total_tuition_owed += tuition
        
        print(f"\nStudent: {last_name}")
        print(f"Tuition Owed: ${tuition:,.2f}\n")
        
    print(f"Total of all tuition owed: ${total_tuition_owed:,.2f}")


# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()