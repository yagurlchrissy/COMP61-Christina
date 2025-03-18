import random

score = 0
rounds = 0
wins = 0
draws = 0
losses = 0

round_numbers = []
player_totals = []
computer_totals = []
results = []

def roll_die():
    return random.randint(1, 6)

def roll_multiple_dice(num_dice=2):
    return sum(roll_die() for _ in range(num_dice))

def get_round_result(player_total, computer_total):
    global score, wins, draws, losses
    if player_total > computer_total:
        score += 10
        wins += 1
        return "Win"
    elif player_total < computer_total:
        score -= 5
        losses += 1
        return "Loss"
    else:
        draws += 1
        return "Draw"

def shop(score):
    print("\nWelcome to the Shop!")
    print("1. Extra Die Roll (Costs 20 points)")
    print("2. Double Points Next Round (Costs 30 points)")
    print("3. Exit Shop")
    
    choice = input("Choose an option: ")
    
    if choice == "1" and score >= 20:
        print("You purchased an extra die roll for the next round!")
        return score - 20, 3
    elif choice == "2" and score >= 30:
        print("Your points will be doubled next round!")
        return score - 30, "double"
    elif choice == "3":
        print("Leaving the shop...")
    else:
        print("Not enough points or invalid choice!")
    
    return score, 2

def display_statistics():
    print("\nGame Over! Here are your final statistics:")
    print(f"Total Rounds Played: {rounds}")
    print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
    print(f"Final Score: {score}")
    print("\nRound History:")
    for i in range(len(round_numbers)):
        print(f"Round {round_numbers[i]}: Player {player_totals[i]} - Computer {computer_totals[i]} | {results[i]}")


while True:
    print(f"\nCurrent Score: {score}")
    visit_shop = input("Do you want to visit the shop? (yes/no): ").lower()
    if visit_shop == "yes":
        score, dice_rolls = shop(score)
    else:
        dice_rolls = 2
    
    player_total = roll_multiple_dice(dice_rolls)
    computer_total = roll_multiple_dice()
    result = get_round_result(player_total, computer_total)
    
    rounds += 1
    round_numbers.append(rounds)
    player_totals.append(player_total)
    computer_totals.append(computer_total)
    results.append(result)
    
    print(f"Round {rounds}: Player rolled {player_total}, Computer rolled {computer_total} -> {result}")
    
    continue_game = input("Do you want to play another round? (yes/no): ").lower()
    if continue_game != "yes":
        break

display_statistics()
