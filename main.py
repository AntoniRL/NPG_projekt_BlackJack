#!/usr/bin/python
# -*- coding: utf-8 -*-


from pickle import TRUE

import game
import pulpit

def main():
    n = pulpit.start_pulpit()
    Gra = game.Game(n[0],int(n[1]))

    while TRUE:
        Gra.rozdanie()
        Gra.print_table()
        while TRUE:
            temp1 = input("[H]IT / [S]TAND \n").lower()
            if temp1 == 's':
                break 
            player_card = Gra.stack.pop()
            Gra.players_list[0].add_card(player_card)
            Gra.print_table()
        temp2 = input("[K]EEP PLAYING / [L]EAVE THE TABLE\n").lower()
        if temp2 == 'l':
            pulpit.clear()
            break
    pulpit.end_pulpit()    
main()    

