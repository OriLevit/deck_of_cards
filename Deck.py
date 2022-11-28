from Card import Card
import json


class Deck:
    def __init__(self, deck_size=52, jokers=False, shuffle=True, ace_high=True):
        cards = open("cards.json")
        cards_list = json.load(cards)
        deck = []
        for card in cards_list:
            current_card = Card(value=cards_list[card]['value'], suit=cards_list[card]['suit'],
                                name=cards_list[card]['name'])
            deck.append(current_card)

        self.deck = deck
        self.deck_size = deck_size
        self.jokers = jokers
        self.shuffle = shuffle
        self.ace_high = ace_high


