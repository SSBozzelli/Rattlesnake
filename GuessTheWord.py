__author__ = 'Andrew'
#A word guessing program

import random
import string


def inWord(letter, word):
    letterFound = False
    for char in word:
        if char == letter:
            letterFound = True
    return letterFound


def timesInWord(letter, word):
    letterTimes = 0
    for char in word:
        if char == letter:
            letterTimes += 1
    return letterTimes


def printWord(word, guesses):
    for char in word:
        letterFound = False
        for guess in guesses:
            if char == guess:
                letterFound = True
        if letterFound:
            print char, " ",
        else:
            print "_ ",


def getLetter():
    letter = raw_input("Guess a letter: ")
    letterOkay = False
    while not letterOkay:
        if not letter.isalpha():
            print "You must enter a letter"
            letter = raw_input("Guess a letter: ")
        elif len(letter) > 1:
            print "Enter only 1 letter"
            letter = raw_input("Guess a letter: ")
        else:
            letterOkay = True
    return letter

def checkWin(word, guesses):
    numberGuessed = 0
    for guess in guesses:
        numberGuessed += timesInWord(guess, word)
    if numberGuessed == len(word):
        return True
    else:
        return False

def createGame(badGuesses):
    man = ['________',
           '|       |',
           '|       O',
           '|       |',
           '|      /|\ ',
           '|       |',
           '|      / \ ']
    counter = 0
    while counter < badGuesses:
        print man[counter]
        counter += 1

def main():

    answer = random.choice(["watermelon", "banana", "pineapple", "coconut", "tomato"])
    correctGuesses = []
    endGame = False
    wrongGuesses = 0

    while not endGame:
        printWord(answer, correctGuesses)
        guess = getLetter()
        if inWord(guess, answer):
            print "You guessed correct"
            correctGuesses.append(guess)
        else:
            print "You guessed wrong. Try again"
            wrongGuesses += 1
            if wrongGuesses < 7:
                createGame(wrongGuesses)
            else:
                createGame(wrongGuesses)
                print "The word was", answer.upper()
                print "LOSER"
                endGame = True
        if checkWin(answer, correctGuesses):
            print "The word was", answer.upper()
            print "WINNER"
            endGame = True
if __name__ == "__main__":
    main()


