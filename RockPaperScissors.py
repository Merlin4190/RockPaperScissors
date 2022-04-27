#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random


class Player:
    def __init__(self):
        self.mymove = ""
        self.theirmove = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.myMove = my_move
        self.theirMove = their_move

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move: ")
            move = move.lower()
            if move in moves:
                return move
            else:
                print("You have a typo, please try again!")

class ReflectPlayer:
    def __init__(self):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    playerScore = 0
    randomPlayerScore = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if(move1 == move2):        	
            print(f"SCORE BOARD=> {self.playerScore}:{self.randomPlayerScore}  \n DRAW!!! \n")

        elif(beats(move1, move2) is True):
           self.playerScore += 1
           print(f"SCORE BOARD=> {self.playerScore}:{self.randomPlayerScore}  \n WIN!!! \n")
        else:
            self.randomPlayerScore += 1
            print(f"SCORE BOARD=> {self.playerScore}:{self.randomPlayerScore}  \n LOST!!! \n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1,4):
            print(f"Round {round}:")

            self.play_round()

        if(self.playerScore > self.randomPlayerScore):
            print("FINAL VERDICT: CONGRATULATIONS, YOU WON...")
        elif(self.playerScore < self.randomPlayerScore):
            print("FINAL VERDICT: YOU LOST, BEST OF LUCK NEXT TIME...")
        else:
            print("FINAL VERDICT: IT ENDED IN A DRAW")

        print("Game over!")

    def score():
        pass


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
