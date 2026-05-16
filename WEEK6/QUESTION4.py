04/15/26   Honour Okhavhe CIS106-001


# Problem 4: Employee Gross Pay

total_gross_pay = 0
employee_count = 0

# Prompt the user on whether they want to do this program 
run_program = input("Do you want to enter employee data? (Enter 'Yes' to continue): ")

# If the user answers Yes then go into the while loop [cite: 21]
while run_program == "Yes":
    # Prompt the user for employee last name, hours worked and rate of pay 
    last_name = input("Enter employee last name: ")
    hours_worked = float(input("Enter hours worked: "))
    pay_rate = float(input("Enter rate of pay: "))
    
    # Compute gross pay with time and a half for hours over 40 
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours_worked * pay_rate
        
    # Sum the gross pay and count the number of employees 
    total_gross_pay += gross_pay
    employee_count += 1
    
    # For each employee display their last name and gross pay 
    print(f"Employee: {last_name}, Gross Pay: ${gross_pay:.2f}")
    
    # Second prompt at the bottom, inside the loop [cite: 30]
    run_program = input("Do you want to do this loop again? (Enter 'Yes' to continue): ")

# After the loop (all data entered) 
if employee_count > 0:
    # Compute and display the average pay 
    average_pay = total_gross_pay / employee_count
    
    # Display the sum of all the gross pays, and count of the number of employees 
    print(f"Total employees processed: {employee_count}")
    print(f"Sum of all gross pays: ${total_gross_pay:.2f}")
    print(f"Average pay: ${average_pay:.2f}")
else:
    print("No employee data was entered.")
