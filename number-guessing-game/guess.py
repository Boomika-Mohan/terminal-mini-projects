import random


def choose_difficulty():
    levels = {"1": (10, 5), "2": (50, 7), "3": (100, 10)}  # (max number, attempts)
    print("Choose difficulty:")
    print("1. Easy   (1-10,  5 attempts)")
    print("2. Medium (1-50,  7 attempts)")
    print("3. Hard   (1-100, 10 attempts)")
    while True:
        choice = input("Enter 1, 2 or 3: ").strip()
        if choice in levels:
            return levels[choice]
        print("Invalid choice. Try again.")


def get_guess(max_number):
    while True:
        try:
            guess = int(input("Your guess: "))
            if 1 <= guess <= max_number:
                return guess
            print(f"Enter a number between 1 and {max_number}.")
        except ValueError:
            print("Please enter a valid number.")


def play():
    max_number, attempts = choose_difficulty()
    secret = random.randint(1, max_number)
    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt}/{attempts}")
        guess = get_guess(max_number)
        if guess == secret:
            print(f"Correct! You got it in {attempt} attempt(s).")
            return
        print("Too low!" if guess < secret else "Too high!")

    print(f"Out of attempts. The number was {secret}.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()