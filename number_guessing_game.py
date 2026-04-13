import random

play_again = "yes"

while play_again == "yes":
    print("\nWelcome to the Number Guessing Game!")
    print("Choose a difficulty: easy, medium, or hard")

    difficulty = input("Enter difficulty: ").lower()

    if difficulty == "easy":
        secret_number = random.randint(1, 10)
        max_attempts = 5
    elif difficulty == "medium":
        secret_number = random.randint(1, 25)
        max_attempts = 4
    elif difficulty == "hard":
        secret_number = random.randint(1, 50)
        max_attempts = 3
    else:
        print("Invalid difficulty. Defaulting to easy.")
        secret_number = random.randint(1, 10)
        max_attempts = 5

    attempts = 0
    guessed_correctly = False

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("Correct! You guessed it in", attempts, "tries!")
            guessed_correctly = True
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        print("Attempts left:", max_attempts - attempts)

    if not guessed_correctly:
        print("Out of attempts! The number was", secret_number)

    play_again = input("Do you want to play again? (yes/no): ").lower()

print("Thanks for playing!")