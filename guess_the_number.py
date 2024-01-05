import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")

    lower_limit = int(input("Enter the lower limit for the number range: "))
    upper_limit = int(input("Enter the upper limit for the number range: "))
    secret_number = random.randint(lower_limit, upper_limit)
    player_guess = 0
    attempts = 0

    while player_guess != secret_number:
        try:
            player_guess = int(input(f"Enter your guess (between {lower_limit} and {upper_limit}): "))
            attempts += 1

            if player_guess < secret_number:
                print("Too low! Try again.")
            elif player_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue 
        
    print("Game over!")

guess_the_number()

