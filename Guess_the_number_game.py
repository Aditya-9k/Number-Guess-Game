import random

class GuessTheNumber:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.guesses = 0

    def make_guess(self, guess):
        self.guesses += 1
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            return f"Congratulations! You guessed the number in {self.guesses} tries."

def main():
    print("Welcome to Guess the Number!")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    
    if lower_bound >= upper_bound:
        print("Invalid range. The lower bound must be less than the upper bound.")
        return
    
    game = GuessTheNumber(lower_bound, upper_bound)
    
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            result = game.make_guess(guess)
            print(result)
            if "Congratulations" in result:
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
