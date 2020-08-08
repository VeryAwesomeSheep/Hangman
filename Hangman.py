import random
import sys

print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit: ')
if menu == "exit":
    sys.exit()
elif menu == "play":
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    hidden_word = list("-"*(len(word)))
    guesses = []

    lifes = 8

    while True:
        display = "".join(hidden_word)
        print()
        print(display)
        if display == word:
            print("You guessed the word!", "You survived!", sep="\n")
            break
        guess = input("Input a letter: ")
        if len(guess) > 1:
            print("You should input a single letter")
            continue
        if guess in guesses:
            print("You already typed this letter")
            continue
        if guess.isalpha() and guess.islower():
            if guess in word:
                for i in range(len(word)):
                    if guess == word[i]:
                        hidden_word[i] = guess
                        guesses.append(guess)
            else:
                print("No such letter in the word")
                lifes -= 1
                guesses.append(guess)
        else:
            print("It is not an ASCII lowercase letter")
            continue
        if lifes == 0:
            print("You are hanged!")
            break
