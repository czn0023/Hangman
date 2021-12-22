#Declare Variables
open(r"words.txt")
import random
playagain = True
wins = 0
losses = 0
while playagain == True:
    hangman = random.choice(list(open(r"words.txt")))
    hangman = hangman.upper()
    hangman = hangman.rstrip("\n")
    pickedhangmen = []
    while hangman in pickedhangmen:
        hangman = random.choice(list(open(r"words.txt")))
    pickedhangmen.append(hangman)
    print(pickedhangmen)
    brokenhangman = list(hangman)
    blankhangman = "-" * len(hangman)
    print(hangman)
    guesses = 7
    print(brokenhangman)
    print(blankhangman)
    print("Try to guess the word!")
    #If guesses reach 0, end game
    while guesses > 0:
        print("You have " + str(guesses) + " guesses left.")
        userword = str(input("Guess a letter or the answer:"))
        #Case is kept by using upper for all inputs and the hangman
        userword = userword.upper()
        #If length of input is more than 1, the user is guessing the word. If not, they are guessing a letter
        if len(userword) > 1:
            if userword == hangman:
                print("Congragulations! You guessed correctly!")
                wins += 1
                #Exit loop, correct answer was given
                break
            else:
                print("That is not correct!")
                #Incorrect guess, closer to losing
                guesses = guesses - 1
                if guesses == 1:
                    break
        else:
            #Add user guess to list for later use
            if userword in brokenhangman:
                print("That letter is in the hangman!")
                #Display guessed letters and their location in the hangman
                index = 0
                while index != len(brokenhangman):
                    if userword == brokenhangman[index]:
                        blankhangman = blankhangman[:index] + userword + blankhangman[index + 1:]
                        index += 1
                    else:
                        index += 1
                print(index)
                print(blankhangman)
            else:
                print("That letter is not in the hangman.")
                guesses = guesses - 1
                print(blankhangman)
    if guesses <= 1:
        print("You've ran out of guesses! You lose.")
        losses += 1
        print("Wins: " + str(wins))
        print("Losses: " + str(losses))
        redo = str(input("Do you want to play again? Y/N"))
        redo = redo.upper()
        if redo != "Y":
            playagain = False
    else:
        print("Wins: " + str(wins))
        print("Losses: " + str(losses))
        redo = str(input("Do you want to play again? Y/N"))
        redo = redo.upper()
        if redo != "Y":
            playagain = False
print("Thanks for playing!")