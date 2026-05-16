# 04/15/26 Honour Okhavhe CIS106-001


# Define the Employee class
class Employee:
    # 1. Recreate class and modify to receive a bonus rate
    def __init__(self, last_name, salary, bonus_rate):
        self.last_name = last_name
        self.salary = float(salary)
        self.bonus_rate = float(bonus_rate)

    # 2. Add a method that computes and returns the bonus amount
    def compute_bonus(self):
        return self.salary * self.bonus_rate

    # 3. Add a method that computes and returns the total compensation
    def compute_total_compensation(self):
        # Total compensation is salary + bonus amount
        return self.salary + self.compute_bonus()


# --- Main Program (Instantiating and using the object) ---

# Get input from the user (optional, but good for testing)
print("--- Enter Employee Details ---")
name_input = input("Enter employee last name: ")
salary_input = float(input("Enter employee salary: "))
bonus_rate_input = float(input("Enter bonus rate (e.g., 0.10 for 10%): "))

# Instantiate the employee object with the provided details
emp1 = Employee(name_input, salary_input, bonus_rate_input)

# Call the methods to get the calculations
bonus_amount = emp1.compute_bonus()
total_comp = emp1.compute_total_compensation()

# Display the results
print("\n--- Employee Compensation Report ---")
print(f"Employee Name: {emp1.last_name}")
print(f"Base Salary: ${emp1.salary:,.2f}")
print(f"Bonus Amount: ${bonus_amount:,.2f}")
print(f"Total Compensation: ${total_comp:,.2f}")