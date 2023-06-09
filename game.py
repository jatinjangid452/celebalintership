import random

class WordGuessGame:
    def __init__(self):
        self.words = ["apple", "banana", "cherry", "grape", "orange"]
        self.word = random.choice(self.words)
        self.attempts = 3

    def play(self):
        print("Welcome to the Word Guessing Game!")
        print("Guess the word within 3 attempts.")

        while self.attempts > 0:
            guess = input("Enter your guess: ")
            
            if guess.lower() == self.word:
                print("Congratulations! You guessed it correctly.")
                return
            
            self.attempts -= 1
            print("Wrong guess. Attempts left:", self.attempts)
        
        print("Game over! The word was", self.word)

game = WordGuessGame()
game.play()
