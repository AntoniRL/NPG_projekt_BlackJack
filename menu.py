
import random


def hitorstand(turns, dscore, playercards, dealercards):   # players choice as to whether he would like to hit or stand
    if turns == 'PLAYER':  # checking if it is players turn
        choice = input('Would you like to hit or stand?').upper()
        if choice == 'HIT':
            print('YOUR CARD:')
            pf, ps = playercards.cardsrandom()
            return ps, pf
        elif choice == 'STAND':
            return 0, 0
    elif turns == 'DEALER':  # checking dealers turn
        if dscore <= 17:   # dealer hits by default if the score is less than equal to 17
            print('DEALERS CARD:')
            df, ds = dealercards.cardsrandom()
            return ds, df
        else:
            print('As per the rules dealer chooses to stand!')
            return 0, 0