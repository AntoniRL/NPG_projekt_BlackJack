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

                    self.stack.append(Card(suits_values[suit], card, values[card]))   # Dodanie karty o danych wartościach do stosu
        random.shuffle(self.stack) #Przetasowanie stosu kart
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

        player_cards = self.players_list[0].cards  # jedyny gracz istniejący w trybie jednoosobowym
        dealer_cards = self.dealer_cards

        player_n_chars = len(player_cards)
        dealer_n_chars = len(dealer_cards)

        init_space = int((player_size - dealer_size) / 2) + 1

        self.clear()

        player_hand_chars = "╱" + int((player_size - 2 * player_n_chars) / 2) * " "
       
        for card in player_cards:
            player_hand_chars += card.symbol + " "

        player_hand_chars += (player_size - len(player_hand_chars) + 1) * " " + "╲"

        print(player_cards)
        print(player_hand_chars)

        dealer_hand_chars = ""
        dealer_hand_chars += "╱" + int((dealer_size - 2 * dealer_n_chars) / 2) * " "

        for card in dealer_cards:
            dealer_hand_chars += card.symbol

        dealer_hand_chars += (dealer_size - len(dealer_hand_chars) + 1) * " " + "╲"

        print(Fore.GREEN + "  Wins: {:2d}".format(5) + Fore.RED + "   Losses: {:2d}".format(3) + Fore.WHITE)
        print(init_space * " " + dealer_size * "_")
        print("   " + dealer_hand_chars)
        print("  ╱                ╲    Bet: {}\n ╱                  ╲   Your score: {}".format(14, self.players_list[0].total()))
        print(player_hand_chars)
        print((player_size + 2) * chr(8254))


    def blackjack(self):
        if total(player_hand) == 21: #Sprawdza czy wartość na ręce jest równa
            print_results(dealer_hand, player_hand)
            print("You win !\n")
            play_again()
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print("You lose\n")
            play_again()

    def score(self):
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print("Sorry. You busted. You lose.\n")
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print("Dealer busts. You win!\n")
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print("Sorry. Your score isn't higher than the dealer. You lose.\n")
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print("Congratulations. Your score is higher than the dealer. You win\n")


class Card:
    def __init__(self, suit, symbol, value):    
        self.suit = suit #Kolor 
        self.symbol = symbol #Symbol karty
        self.value = value #Wartość karty


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

    def save(self):
        saves_path = os.path.abspath(os.getcwd()) + "\\saves"
        curr_save_path = saves_path + f"\\{self.nick}.txt"

        if not os.path.isdir(f"{saves_path}"):
            try:
                os.mkdir(saves_path)
            except:
                print("An error has occured")

        prep_data = ""
        data = [self.nick, self.nr_wins]

        try:
            save_file = open(f"{curr_save_path}", "w")
        except:
            print("An error has occured")

        for x in data:
            prep_data += str(x) + "\n"

        save_file.write(prep_data)
        save_file.close()

    def open_save(self):
        curr_save_path = os.path.abspath(os.getcwd()) + f"\\saves\\{self.nick}.txt"

        if os.path.exists(curr_save_path):

            read_data = []

            try:
                save_file = open(f"{curr_save_path}", "r")
            except:
                print("An error has occured")

            for line in save_file:
                read_data.append(line.replace("\n", ""))
        
            self.nick, self.nr_wins = tuple(read_data)

        else:
            print("Save not found")