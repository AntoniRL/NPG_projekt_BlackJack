#!/urs/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import colored, cprint
from pyfiglet import Figlet
from prettytable import PrettyTable
import game
import time
import os


def print_red(x): return cprint(x, 'red')
def print_green(x): return cprint(x, 'green')


def clear_line():
    """Kasuje ostatnią linię"""
    print("\033[A                                                 \033[A")


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


f = Figlet(font='straight')

wins = 0
losses = 0


def print_players():
    pass


def start_pulpit():
    global wins
    global losses
    players_list = []  # lista graczy [Pleyer()]
    number_of_decks = 0

    while True:
        print(f.renderText('    WELCOEM TO\nB L A C K J A C K !'))
        print(" "*10+"-"*32+"\n")
        print(
            " "*16+f"\033[1;32;40mWINS:  \033[1;37;40m{wins}   \033[1;31;40mLOSSES:  \033[1;37;40m{losses}\n")
        print(" "*10+"-"*32+"\n")

        # pętla obsługująca dodawanie graczy
        while True:
            nick = input("\033[3;37;40mType a players nick: \033[0;37;40m")
            age = input("\033[3;37;40mType the players age: \033[0;37;40m")
            # sprawdzam czy gracz jest pełnoletni
            if int(age) < 18:
                clear_line()
                clear_line()
                print("Sorry, you are too young to play Blackjack :(")
                if 18-int(age) == 1:
                    print(f"Come back in {18-int(age)} year.")
                else:
                    print(f"Come back in {18-int(age)} years.")
                con = input("[C]ontinue\n").lower()
                if con == 'c':
                    clear_line()
                    clear_line()
                    clear_line()
                    clear_line()
                    continue
            # Dodanie gracza do gry
            players_list.append(game.Player(nick))
            clear_line()
            clear_line()
            more_players = input(
                "Do you want to add more players? [Y]es/[N]o\n").lower()
            if more_players == 'y':
                clear_line()
                clear_line()
                continue
            else:
                clear_line()
                clear_line()
                break
        # Wybór ilości talii
        number_of_decks = input(
            "\033[3;37;40mType number of decks (1-8): \033[0;37;40m")
        clear_line()
        clear_line()
        # Wypisanie wszystkich graczy biorących udział w grze
        my_table = PrettyTable()
        my_table.field_names = ["No.", "Name", "Times win"]
        for i in range(len(players_list)):
            my_table.add_row(
                [i+1, players_list[i].nick, players_list[i].nr_wins])
        print("\nPLAYERS:\n", my_table, '\n')
        # Wypisanie ilości talii
        print("Number of card decks: " + str(number_of_decks) + "\n")
        # Pytanie czy można podejść do gry
        temp = input("[S]TART GAME / [G]o back to menu\n").lower()
        if temp == 's':
            clear()
            break
        else:
            clear()
            continue
    return players_list, number_of_decks


def end_pulpit():
    pass


# # Kod wypisujący wygraną i przegraną
# print_red(f.renderText('DEFEAT'))
# print_green(f.renderText('WIN!'))

start_pulpit()
