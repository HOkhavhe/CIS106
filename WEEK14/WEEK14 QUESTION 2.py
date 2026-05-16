# 05/15/26   Honour Okhavhe CIS106-001


class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        # .upper() ensures the code logic works even if a lowercase 'i' or 'o' is entered
        self.district_code = district_code.upper() 
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        """Computes tuition based on district code and credits"""
        if self.district_code == 'I':
            return self.enrolled_credits * 250.00
        else:
            return self.enrolled_credits * 500.00

# --- Testing Part 2 ---

# Test 1: In-district student ('I')
student_in = Student('Alice', 'Smith', 'I', 12)
tuition_in = student_in.compute_tuition()

print("Student:", student_in.first_name, student_in.last_name, "(In-District)")
print(f"Tuition Owed: ${tuition_in:,.2f}")

print("-" * 30)

# Test 2: Out-of-district student ('O')
student_out = Student('Bob', 'Jones', 'O', 15)
tuition_out = student_out.compute_tuition()

print("Student:", student_out.first_name, student_out.last_name, "(Out-of-District)")
print(f"Tuition Owed: ${tuition_out:,.2f}")