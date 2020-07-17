#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time

# ledger for keeping track of score
score1 = [int(0)]
score2 = [int(0)]

moves = ['rock', 'paper', 'scissors']
moves2 = ['rock', 'paper', 'scissors']  # Used for Cycle Player mode


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


# colors for highlighting ties, and which player wins
class bcolors:
    GREEN = '\033[92m'  # used if Player One wins (typically Human player)
    END = '\033[0m'  # changes color back to default
    YELLOW = '\033[93m'  # used for Tie
    RED = '\033[91m'  # used if Player Two wins


"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# New class created for random player
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# New class created for human player
class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, or scissors? > ")
            if move in moves:
                break
            else:
                move = input("Rock, paper, or scissors? > ")
                if move in moves:
                    break
        return move


# New class created for reflect player-mode
class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


# New class created for cycle-player mode
class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_round = None

    def move(self):
        if moves2 == []:
            moves2.extend(['paper', 'rock', 'scissors'])
            move = random.choice(moves2)
            del moves2[moves2.index(move)]
            return move
        else:
            move = random.choice(moves2)
            del moves2[moves2.index(move)]
            return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}, Player 2: {move2}")
        # Display round outcomes and keep score
        if move1 == move2:
            print(bcolors.YELLOW + "** TIE **" + bcolors.END)
        elif beats(move1, move2) is True:
            print(bcolors.GREEN + "** PLAYER ONE WINS **" + bcolors.END)
            score1.append(int(1))
        else:
            print(bcolors.RED + "** PLAYER TWO WINS **" + bcolors.END)
            score2.append(int(1))
        print(f"Score: Player One {sum(score1)}, Player Two {sum(score2)}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("\nGame start! (3 rounds total)\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        p1_total = sum(score1)
        p2_total = sum(score2)
        # Display game results
        print("Final score:")
        print(f"Player One: {p1_total}; Player Two: {p2_total}\n")
        if p1_total > p2_total:
            print(bcolors.GREEN + "Player One Wins Overall!" + bcolors.END)
            print("Game over!")
        elif p1_total < p2_total:
            print(bcolors.RED + "Player Two Wins Overall!" + bcolors.END)
            print("Game over!")
        else:
            while True:
                print_pause(bcolors.YELLOW + "Tie!" + bcolors.END)
                play_again = input("Play again to break tie? (y or n) > ")
                if play_again == 'y':
                    game.play_game()
                    break
                elif play_again == 'n':
                    print("Game over!")
                    break

# This function is used to determine whether to play single or multiple rounds
    def select_game(self):
        if gamerounds == '1':
            game.play_round()
        else:
            game.play_game()


if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors, Go!")
    while True:
        print("Choose type of game:\n")
        gametype = input("(1) Computer only; (2) Human vs Computer "
                         "(1 or 2) > ")
        if gametype == '1':
            break
        if gametype == '2':
            break
    while True:
        print("\nChoose how many rounds to play:")
        gamerounds = input("(1) Single round; (2) Three rounds (1 or 2) > ")
        if gamerounds == '1':
            break
        if gamerounds == '2':
            break
    if gametype == '1':  # Computer-only mode
        game = Game(RandomPlayer(), RandomPlayer())
        if gamerounds == '1':
            game.play_round()
        else:
            game.play_game()
    else:
        while True:  # Human-player mode
            print("\nChoose Computer opponent type:\n")
            opponent = input("(1) Random; (2) Reflect; (3) Cycle; (4) Rock"
                             "\n(enter 1, 2, 3, or 4) > ")

            if opponent == '1':
                print("You selected Random-mode opponent")
                game = Game(HumanPlayer(), RandomPlayer())
                game.select_game()
                break
            elif opponent == '2':
                print("You selected Reflect-mode opponent")
                game = Game(HumanPlayer(), ReflectPlayer())
                game.select_game()
                break
            elif opponent == '3':
                print("You selected Cycle-mode opponent")
                game = Game(HumanPlayer(), CyclePlayer())
                game.select_game()
                break
            elif opponent == '4':
                print("You selected Rock-mode opponent")
                game = Game(HumanPlayer(), Player())
                game.select_game()
                break
