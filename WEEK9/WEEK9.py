# 05/14/2026  Honour Okhavhe CIS106-001



# ==========================================
# Problem 1: Sales Forecast
# ==========================================
def compute_forecast(month, sales):
    """Computes next month's sales based on the forecast percentage."""
    month = month.strip().lower()[:3] # Get first 3 letters for easy matching
    
    if month in ['jan', 'feb', 'mar']:
        forecast_percent = 0.10
    elif month in ['apr', 'may', 'jun']:
        forecast_percent = 0.15
    elif month in ['jul', 'aug', 'sep']:
        forecast_percent = 0.20
    elif month in ['oct', 'nov', 'dec']:
        forecast_percent = 0.25
    else:
        forecast_percent = 0.0 # Default if invalid month
        
    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales

def problem_1():
    print("\n--- Problem 1: Sales Forecast ---")
    while True:
        run = input("Do you want to run the Sales Forecast program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        last_name = input("Enter salesperson's last name: ")
        month = input("Enter the month (e.g., Jan, Feb): ")
        sales = float(input("Enter current month's sales: $"))
        
        next_sales = compute_forecast(month, sales)
        
        print(f"\nSalesperson: {last_name}")
        print(f"Next Month's Forecasted Sales: ${next_sales:,.2f}\n")


# ==========================================
# Problem 2: Room Square Footage & Paint
# ==========================================
def compute_square_footage(length, width, height):
    """Computes the total square footage of a room (floor, ceiling, 4 walls)."""
    sq_ft = (2 * length * width) + (2 * length * height) + (2 * width * height)
    return sq_ft

def problem_2():
    print("\n--- Problem 2: Paint Calculator ---")
    while True:
        run = input("Do you want to run the Paint Calculator program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        length = float(input("Enter room length (ft): "))
        width = float(input("Enter room width (ft): "))
        height = float(input("Enter room height (ft): "))
        
        sqft = compute_square_footage(length, width, height)
        gallons_needed = sqft / 50.0
        
        print(f"\nTotal Square Footage: {sqft:.1f} sq ft")
        print(f"Gallons of paint needed: {gallons_needed:.2f} gallons\n")


# ==========================================
# Problem 3: Automobile Out-The-Door Price
# ==========================================
def compute_otd_price(msrp, make, model, ev_code):
    """Computes final out-the-door price including discounts and 7% tax."""
    make_model = f"{make.strip().lower()} {model.strip().lower()}"
    ev_code = ev_code.strip().upper()
    
    # Determine discount
    if ev_code == 'Y':
        discount_percent = 0.30
    elif make_model == "honda accord":
        discount_percent = 0.10
    elif make_model == "toyota rav4":
        discount_percent = 0.15
    else:
        discount_percent = 0.05
        
    discount_amount = msrp * discount_percent
    new_msrp = msrp - discount_amount
    tax = new_msrp * 0.07
    total_price = new_msrp + tax
    
    return total_price

def problem_3():
    print("\n--- Problem 3: Automobile Pricing ---")
    sum_msrp = 0.0
    sum_sales_price = 0.0
    
    while True:
        run = input("Do you want to run the Auto Pricing program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        make = input("Enter vehicle make: ")
        model = input("Enter vehicle model: ")
        ev_code = input("Is it an Electric Vehicle? (Y/N): ")
        msrp = float(input("Enter MSRP (Sticker Price): $"))
        
        final_price = compute_otd_price(msrp, make, model, ev_code)
        
        sum_msrp += msrp
        sum_sales_price += final_price
        
        print(f"\nVehicle: {make} {model}")
        print(f"Out-The-Door Total (with tax & discount): ${final_price:,.2f}\n")
        
    print("-" * 30)
    print(f"Sum of all MSRPs entered: ${sum_msrp:,.2f}")
    print(f"Sum of all Final Sales Prices: ${sum_sales_price:,.2f}")


# ==========================================
# Problem 4: Train Ticket Price
# ==========================================
def compute_ticket_price(miles):
    """Determines train ticket price based on miles from Chicago."""
    if miles >= 30:
        return 12.00
    elif miles >= 20:
        return 10.00
    elif miles >= 10:
        return 8.00
    else:
        return 5.00

def problem_4():
    print("\n--- Problem 4: Train Tickets ---")
    total_ticket_sales = 0.0
    
    while True:
        run = input("Do you want to run the Train Ticket program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        last_name = input("Enter passenger's last name: ")
        miles = float(input("Enter miles from downtown Chicago: "))
        
        price = compute_ticket_price(miles)
        total_ticket_sales += price
        
        print(f"\nPassenger: {last_name}")
        print(f"Ticket Price: ${price:,.2f}\n")
        
    print("-" * 30)
    print(f"Total revenue from all tickets: ${total_ticket_sales:,.2f}")


# ==========================================
# Problem 5: Property Assessed Value
# ==========================================
def compute_assessed_value(county, market_value):
    """Computes assessed value based on county percentages."""
    county = county.strip().lower()
    
    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70
        
    return market_value * percent

def problem_5():
    print("\n--- Problem 5: Property Assessed Value ---")
    sum_market_values = 0.0
    sum_assessed_values = 0.0
    
    while True:
        run = input("Do you want to run the Property Value program? (Yes or No): ").strip().lower()
        if run != 'yes':
            break
            
        county = input("Enter County name: ")
        market_value = float(input("Enter Market Value of home: $"))
        
        assessed_val = compute_assessed_value(county, market_value)
        
        sum_market_values += market_value
        sum_assessed_values += assessed_val
        
        print(f"\nCounty: {county.capitalize()}")
        print(f"Assessed Value: ${assessed_val:,.2f}\n")
        
    print("-" * 30)
    print(f"Sum of all Market Values: ${sum_market_values:,.2f}")
    print(f"Sum of all Assessed Values: ${sum_assessed_values:,.2f}")


# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()