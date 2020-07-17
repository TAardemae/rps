#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time

moves = ['rock', 'paper', 'scissors']


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
            if move.lower() in moves:
                return move.lower()


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
        self.move_cycle = random.choice(moves)

    def move(self):
        self.move_cycle = moves[(moves.index(self.move_cycle) + 1) %
                                len(moves)]
        return self.move_cycle


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Score ledger:
        self.score1 = [int(0)]
        self.score2 = [int(0)]

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}, Player 2: {move2}")
        # Display round outcomes and keep score
        if move1 == move2:
            print(bcolors.YELLOW + "** TIE **" + bcolors.END)
        elif beats(move1, move2) is True:
            print(bcolors.GREEN + "** PLAYER ONE WINS **" + bcolors.END)
            self.score1.append(int(1))
        else:
            print(bcolors.RED + "** PLAYER TWO WINS **" + bcolors.END)
            self.score2.append(int(1))
        print(f"Score: Player One {sum(self.score1)}, "
              f"Player Two {sum(self.score2)}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("\nGame start! (3 rounds total)\n")
        number_of_rounds = 3
        for round_number in range(number_of_rounds):
            print(f"Round {round_number}:")
            self.play_round()
        p1_total = sum(self.score1)
        p2_total = sum(self.score2)
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

    # This function is used to determine whether to play
    # single or multiple rounds
    def select_game(self):
        if gamerounds == '1':
            game.play_round()
        else:
            game.play_game()


if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors, Go!")
    while True:
        print("\nChoose how many rounds to play:")
        gamerounds = input("(1) Single round; (2) Three rounds "
                           "(Enter 1 or 2) > ")
        if gamerounds == '1':
            break
        if gamerounds == '2':
            break
    # Setting up for any combination of players:
    print("\nChoose Player One:")
    while True:
        print('(1) Human; (2) Computer-Random; (3) Computer-Reflect\n'
              '(4) Computer-Cycle; (5) Computer- Rock')
        Input1 = input('Enter number > ')
        List1 = [1, 2, 3, 4, 5]
        if int(Input1) in List1:
            break
    del List1[List1.index(int(Input1))]
    print("\nChoose Player Two (cannot be same as Player One):")
    while True:
        Input2 = input('Enter number > ')
        if int(Input2) in List1:
            break

    Opponents = [HumanPlayer, RandomPlayer, ReflectPlayer, CyclePlayer, Player]

    Player1 = Opponents[int(Input1) - 1]
    Player2 = Opponents[int(Input2) - 1]

    game = Game(Player1(), Player2())
    if gamerounds == '1':
        game.play_round()
    else:
        game.play_game()
