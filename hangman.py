import random
import time

print ("Let's play hangman (in english)!")
wantToPlay = True
while (wantToPlay):
    try:
        word = random.choice(open('words.txt').read().splitlines())
    except FileNotFoundError:
                print("Error: File 'words.txt' not found.")
                break

    lives= 6
    guessed_letters= []
    wordSoFar= ["_"] * len(word)
    while lives >= 0:
        time.sleep(1)
        print("\n")
        print(*wordSoFar)
        print("Lives left: ", lives)
        guess = input("Guess a letter (or the entire word by typing \"guess answer\"): ").lower()

        if guess == "help":
            print("\nGuessed letters: ", *sorted(guessed_letters))
            continue
        
        #guessing the whole word
        if guess == "guess answer":
            answer = input("Enter your guess for the word: ")
            if not answer.isalpha():
                print("It seems like you don't understand what a word is. In case you don't know, a word is a combination of letters, and it does NOT contain any numbers or special characters. Lets try again.")
                continue
            
            if answer == word:
                print("\nCongratulations! You've guessed the word!")
                break
            else:
                lives -= 1
                print("\nWrong guess! If you want to know what letters you have guessed, type \"help\"")
                continue


        #guessing more than one letter
        if len(guess)!= 1:
            print("\nNot a valid input. Must be a single letter. Exactly one letter. If you want to know what letters you have guessed, type \"help\"")
            time.sleep(1)
            continue

        if not guess.isalpha():
            print("\nNot a valid input. Must be a letter.")
            continue

        

        if guess in guessed_letters:
            print("\nYou already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    wordSoFar[i] = guess


        else:
            lives -= 1
            print("\nLetter not found! If you want to know what letters you have guessed, type \"help\"")
            time.sleep(0.6)
            continue
        if all(letter in guessed_letters for letter in word):
            print("\nWord guessed , you've won!")
            break
        wantToPlay = input("\nDo you want to play again? (y/n): ").lower() == "y"



