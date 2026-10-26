import re
import random
playing=True # Creates starting value to see if player wants to play again
while playing==True:
    possiblewords=["act", "ant", "art", "bag", "bat", "box", "bus", "cat", "cup", "day", "dog", "ear", "egg", "fan", "fox", "gem", "hat", "ice", "jar", "key", "map", "net", "owl", "pen", "pin", "sky", "sun", "toy", "van", "zoo", "area", "atom", "baked", "ball", "bark", "bell", "bird", "blue", "boat", "book", "cake", "camp", "card", "cave", "chef", "clay", "coin", "cone", "cook", "desk", "duck", "dusk", "farm", "fish", "flag", "frog", "game", "glow", "gold", "hill", "home", "jello", "kite", "lamp", "leaf", "lion", "moon", "nest", "park", "pear", "quiz", "rain", "rock", "ship", "star", "tree", "wave", "wind", "yard", "zero", "apple", "badge", "beach", "brave", "brick", "cabin", "camel", "candy", "chair", "chalk", "chart", "chess", "clock", "cloud", "count", "crown", "dance", "dream", "earth", "elbow", "field", "flame", "flute", "focus", "frame", "fresh", "frost", "giant", "globe", "grape", "grass", "green", "happy", "heart", "house", "juice", "lemon", "light", "lunch", "mouse", "music", "ocean", "paint", "paper", "piano", "plant", "polar", "prize", "robot", "scale", "shark", "smile", "space", "storm", "train", "truck", "voice", "water", "whale", "world", "active", "animal", "autumn", "baking", "banana", "basket", "blazer", "branch", "bridge", "bucket", "butter", "camera", "canvas", "canyon", "castle", "cheese", "cherry", "clever", "cosmic", "doctor", "dollar", "dragon", "eraser", "family", "forest", "freeze", "galaxy", "garden", "guitar", "helper", "jacket", "jungle", "kitten", "magnet", "marble", "monkey", "museum", "nature", "orange", "oxygen", "packet", "pencil", "planet", "pocket", "puzzle", "rabbit", "rocket", "school", "shadow", "silver", "square", "summer", "talent", "ticket", "travel", "turtle", "violet", "winter", "yellow", "balloon", "blanket", "booklet", "captain", "century", "chicken", "climate", "college", "compass", "crystal", "diamond", "dolphin", "drawing", "dynamic", "feather", "festival", "freedom", "glacier", "hamster", "harvest", "holiday", "horizon", "journey", "kingdom", "lantern", "library", "morning", "notebook", "oatmeal", "octopus", "penguin", "picture", "project", "pumpkin", "sandbox", "science", "swallow", "sweater", "thunder", "weather", "absolute", "alphabet", "astronaut", "backdrop", "backyard", "bicycle", "blizzard", "calendar", "campsite", "carnival", "computer", "dinosaur", "elephant", "flamingo", "fountain", "hardware", "hospital", "keyboard", "mountain", "mushroom", "painting", "peaceful", "sidewalk", "squirrel", "textbook", "triangle", "vacation", "wildlife", "adventure", "beautiful", "blueprint", "celebrate", "challenge", "classroom", "community", "crocodile", "different", "discovery", "dragonfly", "education", "geography", "jellyfish", "landscape", "principal", "satellite", "spaceship", "telescope", "playground", "basketball", "blackboard", "dandelion", "dictionary", "elementary", "helicopter", "microphone", "skateboard", "wilderness"]
    # Giant list of random words to choose from (Used Gemini to generate the list, it was not used for anything else)
    word = random.choice(possiblewords) # Chooses a random word to use for the game
    word=word.lower() # Puts word into lowercase so no issues occur related in capitalization
    print("Let's play hangman!")
    letguessed="?" # Adds filler character to replace to avoid bugs
    guessattempts="" # Makes a list of letters guessed to make sure something wasn't guessed multiple times
    curword = re.sub("[^" + letguessed + "]", "_", word) # Creates version of word that user can see hiding unknown letters
    lives=6
    win=False # Sets ups variables for loop
    while lives>=0 and win==False: #Keeps repeating until players runs out of lives or wins
        print("You have " + str(lives) + " lives left")
        print("You currently have " + curword)
        guess=input("Please type a letter you would like to guess to see if it is in the word. If you would like to see previous guesses type help: ")
        if len(guess)==1 and guess.isalpha() and not guess.lower() in guessattempts.lower(): # Checks if it is a single letter not already guessed
            if guess.lower() in word.lower():
                letguessed=(letguessed+guess) # Adds guessed letter to list of letters correctly identified
                curword = re.sub("[^" + letguessed + "]", "_", word) # Replaces all letters with underscores except guessed letters.
                print(guess.upper() + " was in the word")
            else:
                print("Letter not found!")
                lives=lives-1 # Decreases a player life in case they incorrectly guessed
            guessattempts=guessattempts+guess # Adds guess to list of attempted letters
        elif len(guess)==1 and guess.isalpha() and guess.lower() in guessattempts.lower(): # If it is a letter already guessed
            print("You have already guessed this letter")
        elif guess.lower()=="help": # Prints all guessed letters if user types help
            print("You have guessed: " + guessattempts)
        else: # If it is not a single letter
            print("Please enter a valid character with only one letter") 
        underscore_count = curword.count("_") # Counts the number of underscores left in the word to check if it has been fully guessed
        if underscore_count==0:
            print("You won! The word was " + word)
            win=True
    if lives<0:
        print("Out of lives, game over! The word was " + word)
    playasking=True # Creates variable to check if the program successly asked and got proper response to if user wants to play again
    while playasking==True:  
        playcheck=input("Would you like to play again?")
        if playcheck.lower()=="yes":
            playing=True
            playasking=False
        elif playcheck.lower()=="no":
            playing=False
            playasking=False
        else:
            print("Please enter yes or no.")
exit()


        
