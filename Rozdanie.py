from inspect import stack
import random
class Game:
    def __init__(self,stack,dealer_cards,number_of_players,players_list,number_of_decks):
        self.stack = stack #Stos kart
        self.dealer_cards = dealer_cards #Karty krupiera
        self.number_of_players = number_of_players #Liczba graczy
        self.players_list = players_list #Lista graczy
        self.number_of_decks = number_of_decks #Liczba użytych talii

    def rozdanie (self):
        for _ in range(2):
            for i in range(len(self.players_list)):
                player_card = stack.pop()
                self.players_list[i].add_card(player_card)
            dealer_card = stack.pop()
            self.dealer_cards.append(dealer_card)   
        print(self.players_list[0])

    def stack_creation(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
        symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        self.stack = []
        for i in range(self.number_of_decks):
            for suit in suits:  # Pętla dla każdego koloru    
                for card in symbols:  # Pętla dla każdej karty w danym kolorze
                    self.stack.append(Card(suits_values[suit], card, values[card]))   # Dodanie karty o danych wartościach do stosu
        random.shuffle(self.stack) #Przetasowanie stosu kart
        return self.stack 

class Card:
    def __init__(self, suit, symbol, value):    
        self.suit = suit #Kolor 
        self.symbol = symbol #Symbol karty
        self.value = value #Wartość karty

class Player:
    def __init__(self,cards,nick):
        self.nick = nick 
        self.cards = cards #Aktualne posiadane przez gracza karty
    def add_card(self,card):
        self.cards.append(card)