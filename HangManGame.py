import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "programming", "developer", "keyboard"]


# Function to choose a random word
def choose_word():
    return random.choice(word_list)


# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Main game function
def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6
    print("🎮 Welcome to Hangman!")

    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {attempts_left}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\n🎉 Congratulations! You guessed the word:", word)
                break
        else:
            print("❌ Wrong guess.")
            attempts_left -= 1

    else:
        print("\n💀 Game Over! The word was:", word)


# Run the game
if __name__ == "__main__":
    hangman()
