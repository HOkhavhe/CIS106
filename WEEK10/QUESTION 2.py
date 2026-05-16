# 05/14/2026  Honour Okhavhe CIS106-001


def compute_student_stats(score1, score2, score3):
    """Computes total points and average of 3 exams."""
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score

def main_prob2():
    print("--- Problem 2: Student Scores ---")
    last_name = input("Enter student's last name: ")
    s1 = float(input("Enter exam 1 score: "))
    s2 = float(input("Enter exam 2 score: "))
    s3 = float(input("Enter exam 3 score: "))
    
    total, average = compute_student_stats(s1, s2, s3)
    
    print("\n--- Student Report ---")
    print(f"Name: {last_name}")
    print(f"Total Points: {total}")
    print(f"Average Score: {average:.2f}\n")

main_prob2()