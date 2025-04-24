import random
from .card import Card


class Deck:
    "Represents a deck of 52 playing cards and provides basic operations."

    suits = Card.suits
    ranks = Card.ranks

    def __init__(self) -> None:
        self.cards = [Card(s, r) for s in Deck.suits for r in Deck.ranks]

    def shuffle(self) -> None:
        "Shuffle the deck."
        random.shuffle(self.cards)

    def deal(self, num_players: int) -> list[list[Card]]:
        "Deal the deck into num_players hands and return them."
        hands = [[] for _ in range(num_players)]
        for idx, card in enumerate(self.cards):
            hands[idx % num_players].append(card)
        return hands

