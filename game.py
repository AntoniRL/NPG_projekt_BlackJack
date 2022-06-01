from inspect import stack
import random
import os
from colorama import Fore


class Game:
    def __init__(self, players_list, number_of_decks=1):
        self.stack = []  # Stos kart
        self.dealer_cards = []
        self.number_of_players = len(players_list)  # Liczba graczy
        self.players_list = players_list  # Lista graczy
        self.number_of_decks = number_of_decks  # Liczba użytych talii
        self.stack_creation()

    def rozdanie(self):
        for _ in range(2):
            for i in range(len(self.players_list)):
                player_card = self.stack.pop()
                self.players_list[i].add_card(player_card)
            dealer_card = self.stack.pop()
            self.dealer_cards.append(dealer_card)   
        print(self.players_list[0])

    def stack_creation(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
        symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                  "K": 10}
        self.stack = []
        for _ in range(self.number_of_decks):
            for suit in suits:  # Pętla dla każdego koloru    
                for card in symbols:  # Pętla dla każdej karty w danym kolorze
                    self.stack.append(
                        Card(suits_values[suit], card, values[card]))  # Dodanie karty o danych wartościach do stosu
        random.shuffle(self.stack)  # Przetasowanie stosu kart
        return self.stack

    def play_again(self):
        pass


    def hit(self):
        pass

    def clear(self):
        os.system('cls')

    def print_table(self):
        #interfejs da radę pokazać 7 kart dla krupiera i góra 10 kart gracza(po modyfikacji możliwe jest 14 i 20 odpowiednio), chyba wystarczy
        player_size = 20
        dealer_size = 14

        player_cards = self.players_list[0].cards  # jedyny gracz istniejący w trybie jednoosobowym, najprawdopoboniej do zmiany
        dealer_cards = self.dealer_cards

        player_n_chars = len(player_cards)
        dealer_n_chars = len(dealer_cards)

        init_space = int((player_size - dealer_size) / 2) + 1

        self.clear()

        player_hand_chars = ""
        player_hand_chars += "╱" + int((player_size - 2 * player_n_chars) / 2) * " "
        for card in player_cards:
            player_hand_chars += card + " "
        player_hand_chars += (player_size - len(player_hand_chars) + 1) * " " + "╲"

        dealer_hand_chars = ""
        dealer_hand_chars += "╱" + int((dealer_size - 2 * dealer_n_chars) / 2) * " "
        for card in dealer_cards:
            dealer_hand_chars += card
        dealer_hand_chars += (dealer_size - len(dealer_hand_chars) + 1) * " " + "╲"

        print(Fore.GREEN + "  Wins: {:2d}".format(5) + Fore.RED + "   Losses: {:2d}".format(3) + Fore.WHITE)
        print(init_space * " " + dealer_size * "_")
        print("   " + dealer_hand_chars)
        print("  ╱                ╲    Bet: {}\n ╱                  ╲   Your score: {}".format(14, 13))
        print(player_hand_chars)
        print((player_size + 2) * chr(8254))
        print("[H]it\n[S]tand\n[Q]uit")


    def blackjack(self):
        pass

    def score(self):
        pass


class Card:
    def __init__(self, suit, symbol, value):
        self.suit = suit  # Kolor
        self.symbol = symbol  # Symbol karty
        self.value = value  # Wartość karty


class Player:
    def __init__(self,cards,nick,nr_wins):
        self.nick = nick 
        self.cards = cards #Aktualne posiadane przez gracza karty
        self.nr_wins = nr_wins
    def add_card(self,card):
        self.cards.append(card)

    def total(self):
        total = 0
        for card in self.cards:
            total+=card.value
            if card.symbol == "A" and total>21: 
                total-=10
        return total