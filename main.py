#!/usr/bin/python
# -*- coding: utf-8 -*-

from pickle import TRUE
from pprint import pprint
from tkinter import W
import game
import pulpit

def main():
    n = pulpit.start_pulpit() #Odebranie z funkcji start_pulpit zmiennych (Lista graczy , liczba talii)
    Gra = game.Game(n[0],int(n[1])) #Inicjacja klasy Gra typu Game
    while TRUE: #Pętla sprawdzająca kiedy gracz chce odejść od stołu
        Gra.rozdanie() 
        Gra.print_table()
        while TRUE: 
            temp1 = input("[H]IT / [S]TAND \n").lower() #Wybór ruchu gracza
            if temp1 == 's':
                break 
            elif Gra.players_list[0].total()>21:
                print ("Za dużo")
                break
            else:
                player_card = Gra.stack.pop()
                Gra.players_list[0].add_card(player_card)
                Gra.print_table()
        temp2 = input("[K]EEP PLAYING / [L]EAVE THE TABLE\n").lower()
        if temp2 == 'l':
            pulpit.clear()
            break
    pulpit.end_pulpit()
main()