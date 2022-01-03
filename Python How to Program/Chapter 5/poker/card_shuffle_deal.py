import constant
import random

def make_deck():
    my_deck = []
    for i in range(constant.DECK):
        card = (constant.FACES[i%13], constant.SUIT[i//13])
        my_deck.append(card)

    random.shuffle(my_deck)
    return my_deck


def get_card(my_deck):
    card = my_deck[0]
    my_deck.pop(0)
    return card

def deal_cards(my_deck):
    hand = []
    for _ in range(5):
        hand.append(get_card(my_deck))

    return hand