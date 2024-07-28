# Guess the Number

A simple Python program where the user tries to guess a randomly generated number within a specified range.

## Features

- **Set Range**: Allows the user to define the lower and upper bounds for the random number.
- **Guessing**: Prompts the user to guess the number, providing feedback on whether the guess is too low, too high, or correct.
- **Tracking Attempts**: Keeps track of the number of guesses made.

## Usage

1. **Set the Range**
    - The user is prompted to enter a lower bound and an upper bound.
    - If the lower bound is greater than or equal to the upper bound, the program will display an error message and exit.

2. **Make a Guess**
    - The user is prompted to guess a number within the specified range.
    - The program provides feedback on whether the guess is too low, too high, or correct.
    - The game continues until the user guesses the correct number.

## Example


Welcome to Guess the Number!
Enter the lower bound: 1
Enter the upper bound: 100
Guess a number between 1 and 100: 50
Too low!
Guess a number between 1 and 100: 75
Too high!
Guess a number between 1 and 100: 62
Congratulations! You guessed the number in 3 tries.
