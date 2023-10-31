import random

# List of words for the game
words = ["programming", "hangman", "challenge", "developer", "python", "intermediate"]

def choose_random_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = []
    for letter in word:
        if letter in guessed_letters:
            displayed.append(letter)
        else:
            displayed.append('_')
    return ' '.join(displayed)

def hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    max_attempts = 6
    incorrect_attempts = 0

    print("Welcome to Hangman!")

    while incorrect_attempts < max_attempts:
        print("\nSecret Word: " + display_word(secret_word, guessed_letters))
        print("Guessed Letters: " + ' '.join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess in secret_word:
                print("Correct guess!")
                if display_word(secret_word, guessed_letters) == secret_word:
                    print(f"Congratulations! You've guessed the word: {secret_word}")
                    break
            else:
                print("Incorrect guess.")
                incorrect_attempts += 1
                print(f"Attempts left: {max_attempts - incorrect_attempts}")

    if incorrect_attempts == max_attempts:
        print(f"Game over! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
