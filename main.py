#!/usr/bin/python
# -*- coding: utf-8 -*-

from pickle import TRUE
from pprint import pprint
from tkinter import W
import game
import pulpit


def main():
    # Odebranie z funkcji start_pulpit zmiennych (Lista graczy , liczba talii)
    n = pulpit.start_pulpit()
    Gra = game.Game(n[0], int(n[1]))  # Inicjacja klasy Gra typu Game
    while TRUE:  # Pętla sprawdzająca kiedy gracz chce odejść od stołu
        Gra.rozdanie()
        Gra.print_table(False)
        while TRUE:  # Ruch gracza
            if Gra.players_list[0].total() >= 21:
                break
            temp1 = input("[H]IT / [S]TAND \n").lower()  # Wybór ruchu gracza
            if temp1 == 's':
                break
            else:
                Gra.hit()
        Gra.print_table(True)
        # Pętla ,w której krupier dobiera karty jeśli przegrywa
        while Gra.dealer.total() < Gra.players_list[0].total() <= 21:
            dealer_card = Gra.stack.pop()
            Gra.dealer.add_card(dealer_card)
            Gra.print_table(True)
        Gra.score()
        if len(Gra.stack) < 5:  # Warunek zabezpieczający przed skończeniem się kart
            temp1 = input(
                "Kończą się karty. Chcesz ponowne rozdanie? [T/N]\n").lower()
        else:
            temp2 = input("[K]EEP PLAYING / [L]EAVE THE TABLE\n").lower()
        if temp1 == 't':  # Jeśli kończą się karty,a gracz chce grać dalej tworzy nowy stos
            Gra.stack_creation()
        elif temp2 == 'l' or temp1 == 'n':  # Warunek sprawdzający czy gracz chce skończyć grę
            pulpit.clear()
            break

    pulpit.end_pulpit()


main()
