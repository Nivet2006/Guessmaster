import random

def display_scoreboard():
    try:
        with open("scoreboard.txt", "r") as file:
            print("\n--- Scoreboard ---")
            print(file.read())
    except FileNotFoundError:
        print("\n--- Scoreboard ---")
        print("No scores yet.")

def update_scoreboard(player_name, attempts):
    try:
        with open("scoreboard.txt", "a") as file:
            file.write(f"{player_name}: {attempts} attempts\n")
    except:
        print("Failed to update the scoreboard.")

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    player_name = input("Enter your name: ")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations, {player_name}! You guessed the number in {attempts} attempts!")
                update_scoreboard(player_name, attempts)
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            guess_number()
        elif play_again.lower() == "no":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

    display_scoreboard()

guess_number()
