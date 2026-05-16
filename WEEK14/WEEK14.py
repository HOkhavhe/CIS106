# 04/15/26   Honour Okhavhe CIS106-001


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Added method for the assignment
    def compute_bonus(self, bonus_rate):
        """Computes the employee bonus of rate x salary (pay)"""
        return self.pay * bonus_rate

# --- Testing Part 1 ---

# Instantiate the object
emp_1 = Employee('Jane', 'Doe', 60000)

print("Employee Name:", emp_1.fullname())
print("Base Salary: $", emp_1.pay)

# Test the bonus method with a 10% bonus rate (0.10)
rate = 0.10
calculated_bonus = emp_1.compute_bonus(rate)

print(f"Calculated Bonus (at {rate*100}%): ${calculated_bonus:,.2f}")
