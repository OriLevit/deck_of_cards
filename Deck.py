from Card import Card
import json


class Deck:
    def __init__(self, deck_size=52, jokers=False, shuffle=True, ace_high=True):
        cards = open("cards.json")
        cards_list = json.load(cards)
        deck = []
        for _ in range(deck_size):
            current_card = Card(cards_list[_]["value"], cards_list[_]["suit"], cards_list[_]["name"])
            deck.append(current_card)

        self.deck = deck
        self.deck_size = deck_size
        self.jokers = jokers
        self.shuffle = shuffle
        self.ace_high = ace_high
