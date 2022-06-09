import random
import art
lives = 0
numbers_guessed = []
guess = 0


def game(difficulty):
    global guess
    global lives
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    number = random.randint(1, 100)
    while number != guess and lives > 0:
        print(f"\nYou have {lives} attempts to guess the number")
        guess = int(input("Please guess a number between 1 and 100\n"))
        if guess == number:
            return "\nCongratulations, you guessed correctly!"
        elif guess > number:
            lives -= 1
            print("\nYou guessed too high!\nGuess again.")
        elif guess < number:
            lives -= 1
            print("\nYou guessed too low!\nGuess again.")
    if lives == 0:
        return f"Sorry you are out of lives! The number was {number}"


print(art.logo)
print("Welcome to the Number Guessing Game!")
difficulty = input("Please choose a difficulty. Type 'easy' or 'hard\n").lower()
print(game(difficulty))
