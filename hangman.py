
import random

WORDS = ["PYTHON", "COMPUTER", "COLLEGE", "STUDENT", "PROGRAM"]

HANGMAN = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


def play_hangman():
    word = random.choice(WORDS)
    correct_letters = set()
    wrong_letters = set()
    max_attempts = 6

    print("\n================================")
    print("   HANGMAN WORD GUESSING GAME")
    print("================================")
    print("Guess the hidden word!")

    while len(wrong_letters) < max_attempts:
        print(HANGMAN[len(wrong_letters)])

        display_word = " ".join(
            letter if letter in correct_letters else "_"
            for letter in word
        )

        print("Word:", display_word)
        print("Wrong letters:", sorted(wrong_letters))
        print("Attempts left:", max_attempts - len(wrong_letters))

        if all(letter in correct_letters for letter in word):
            print("\nCongratulations! You won!")
            print("The word was:", word)
            return

        guess = input("\nEnter one letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter only one letter from A to Z.")
            continue

        if guess in correct_letters or guess in wrong_letters:
            print("You already guessed that letter!")
            continue

        if guess in word:
            correct_letters.add(guess)
            print("Correct guess!")
        else:
            wrong_letters.add(guess)
            print("Wrong guess! Try again.")

    print(HANGMAN[5])
    print("\nGame over! You lost.")
    print("The correct word was:", word)


if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("Thanks for playing!")
            break
