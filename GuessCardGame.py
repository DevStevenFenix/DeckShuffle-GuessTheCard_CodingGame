from random import shuffle
import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    ##### Start Game #####

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        self.__newDeck = self.cards.copy()

    def __repr__(self):
        return f'Cards Left:{len(self.cards)} \n {self.cards}'

    #### Restart Game #####
    def restart_game(self):
        self.cards = self.__newDeck
        return self.cards

    #### Shuffle Deck #####
    def shuffle(self):
        shuffle(self.cards)
        return self

    #### Remove Card #####
    def remove_card(self):
        if len(self.cards) < 1:
            raise ValueError('No cards left in the Deck')
        print(f'The card removed is: {self.cards[0]}')
        self.cards.pop(0)

    #### Take a Random Card ####
    def take_random(self):
        if len(self.cards) < 1:
            raise ValueError('No cards left in the Deck')
        random_number = random.randint(0, len(self.cards))
        print(f'You feeling lucky huh?, the random card removed is: {self.cards[random_number]}')
        self.cards.pop(random_number)
        print(f'###############\nCards Left: {len(self.cards)}\n###############')

    ##### Take a try and guess the next card! dont cheat ;) #######

    def guess_the_card(self):
        guess: str = (input('Which card comes next?'))
        if guess == str(self.cards[0]):
            print('you fucking get it!')
            print(f'{self.cards[0]} has been removed from the deck')
            self.cards.pop(0)
        else:
            print('nah ah ah, try again')


######## Start your game here! ##########
deck = Deck()
deck.take_random()