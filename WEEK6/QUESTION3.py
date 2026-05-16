04/15/26   Honour Okhavhe CIS106-001


# Problem 3: Student Exam Averages

student_count = 0

# Prompt the user on whether they want to do this program (just before the while loop) 
run_program = input("Do you want to enter student data? (Enter 'Yes' to continue): ")

# "Yes" entry means they want to continue [cite: 9]
while run_program == "Yes":
    # Prompt the user for their last name and two exam scores 
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))
    
    # Compute the average exam score 
    average = (score1 + score2) / 2
    student_count += 1
    
    # Display last name and average 
    print(f"Student: {last_name}, Average Score: {average:.2f}")
    
    # Second prompt at the bottom, inside the loop [cite: 18]
    run_program = input("Do you want to do this loop again? (Enter 'Yes' to continue): ")

# After the loop, display a count of the number of students who entered data 
print(f"Total number of students processed: {student_count}")