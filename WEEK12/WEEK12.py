# 05/14/2026  Honour Okhavhe CIS106-001



# PROBLEMS 1, 2, & 3: Student Exam Scores


# 1 & 2: Write functions to display names and scores (parallel arrays) [cite: 3, 7]
def display_data(names, scores):
    print("\n--- Student Scores ---")
    for i in range(len(names)):
        print(f"Name: {names[i]}, Score: {scores[i]}")

# 1 & 2: Display names and scores in reverse order [cite: 3, 7]
def display_reverse(names, scores):
    print("\n--- Student Scores (Reversed) ---")
    # Loop backwards through the array
    for i in range(len(names) - 1, -1, -1):
        print(f"Name: {names[i]}, Score: {scores[i]}")

# 3: Load data from a file into parallel arrays 
def load_student_data(filename):
    names_array = []
    scores_array = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                names_array.append(data[0])
                scores_array.append(int(data[1]))
        return names_array, scores_array
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it first.")
        return [], []

# 3: Display highest and lowest scores using specific variable logic [cite: 9, 10, 11, 12, 13]
def display_extremes(names, scores):
    if not scores:
        return
        
    high_var = 0      # Initialize to 0 as requested [cite: 10]
    high_index = 0
    low_var = 999     # Initialize to 999 as requested [cite: 13]
    low_index = 0

    for i in range(len(scores)):
        # Check for highest [cite: 11]
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
            
        # Check for lowest [cite: 13]
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("\n--- Score Extremes ---")
    print(f"Highest Score: {names[high_index]} with a score of {high_var}")
    print(f"Lowest Score:  {names[low_index]} with a score of {low_var}")



# PROBLEMS 4 & 5: Baseball Player Averages


# 4: Load list of 10 player names and averages from file [cite: 14]
def load_player_data(filename):
    players_array = []
    averages_array = []

    try:
        with open("players.txt", 'r') as file:
            for line in file:
                data = line.split()
                if len(data) >= 2: # skip blank or incomplete lines
                    players_array.append(data[0])
                    averages_array.append(float(data[1]))

               
        return players_array, averages_array

    except FileNotFoundError:
            print(f"Error: {filename} not found. ")
            return [], []

# 4: Write a function to display the arrays [cite: 16]
def display_players(names, averages):
    print("\n--- Player Batting Averages ---")
    for i in range(len(names)):
        print(f"Player: {names[i]}, Average: {averages[i]:.3f}")

# 4 & 5: Search for last name and display result or "Not Found" message [cite: 17, 18]
def search_player(names, averages, target_name):
    found = False
    for i in range(len(names)):
        # Using .lower() ensures the search isn't case-sensitive
        if names[i].lower() == target_name.lower():
            print(f">>> Found: {names[i]} has a batting average of {averages[i]:.3f}")
            found = True
            break # Exit loop once found
            
    if not found:
        print(f">>> Name not found [cite: 18]")


# MAIN EXECUTION BLOCK

if __name__ == "__main__":
    
    # --- Executing Problems 1, 2, & 3 ---
    print("LOADING STUDENT DATA...")
    student_names, student_scores = load_student_data('students.txt')
    
    if student_names and student_scores:
        display_data(student_names, student_scores)
        display_reverse(student_names, student_scores)
        display_extremes(student_names, student_scores)
        
    print("\n" + "="*40 + "\n")

    # --- Executing Problems 4 & 5 ---
    print("LOADING PLAYER DATA...")
    player_names, batting_averages = load_player_data('players.txt')
    
    if player_names and batting_averages:
        display_players(player_names, batting_averages)
        
        print("\n--- Player Search ---")
        # 4: Repeatedly ask the user for a last name using a while loop [cite: 16]
        while True:
            user_input = input("Enter a player's last name to search (or type 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print("Exiting search. Goodbye!")
                break
                
            search_player(player_names, batting_averages, user_input)

