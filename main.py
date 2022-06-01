#!/usr/bin/python
# -*- coding: utf-8 -*-

import game
import pulpit

def main():
    n = pulpit.start_pulpit()
    Gra = game.Game(n[0],int(n[1]))
    Gra.rozdanie()
    Gra.print_table()

main()    