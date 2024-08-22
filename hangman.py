import random

def hangman():
    word_list = ['python', 'flatsome', 'hangman', 'development', 'agency']
    word = random.choice(word_list)
    guessed_word = ['_'] * len(word)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")

    while attempts > 0:
        print("\nCurrent word:", ' '.join(guessed_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts remaining.")

    if attempts == 0:
        print("\nYou've run out of attempts. The word was:", word)

hangman()

