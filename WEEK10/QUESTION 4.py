# 05/14/2026  Honour Okhavhe CIS106-001



def compute_bowling_averages(g1, g2, g3, handicap):
    """Computes base average and average including handicap."""
    base_average = (g1 + g2 + g3) / 3
    handicap_average = base_average + handicap
    return base_average, handicap_average

def main_prob4():
    print("--- Problem 4: Bowler Scores ---")
    last_name = input("Enter bowler's last name: ")
    game1 = int(input("Enter game 1 score: "))
    game2 = int(input("Enter game 2 score: "))
    game3 = int(input("Enter game 3 score: "))
    hcap = int(input("Enter handicap: "))
    
    avg, hcap_avg = compute_bowling_averages(game1, game2, game3, hcap)
    
    print("\n--- Bowler Stats ---")
    print(f"Name: {last_name}")
    print(f"Average Score: {avg:.1f}")
    print(f"Average with Handicap: {hcap_avg:.1f}\n")

main_prob4()