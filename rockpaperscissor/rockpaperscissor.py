import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print(f"\n--- Score | You: {user_score} - Computer: {computer_score} ---")
        user_choice = input("Enter rock, paper, scissors (or 'quit'): ").lower()
        
        if user_choice == "quit":
            print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
            print("Goodbye!")
            break
            
        if user_choice not in options:
            print("Invalid choice, try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1