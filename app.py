
import random

def hangman():
    # List of words for the game
    words = ["python", "programming", "hangman", "challenge", "computer"]
    word = random.choice(words)  # Randomly select a word
    guessed_letters = set()      # To keep track of letters already guessed
    incorrect_guesses = 0
    max_incorrect = 6            # Maximum allowed incorrect guesses
    
    # Create a display version of the word with underscores for each letter
    display = ['_' for _ in word]
    
    print("Welcome to Hangman! Lets Guess Computer Tech")
    
    # Game loop continues until the player either guesses the word or runs out of guesses
    while incorrect_guesses < max_incorrect and "_" in display:
        print("\nCurrent word: " + " ".join(display))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        # Validate input: ensure a single alphabetical character is entered
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        # If the guess is in the word, reveal its position(s)
        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")
    
    # Check the game outcome after the loop
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nSorry, you've run out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()
