import random
from .card import Card


class Deck:
    "Represents a deck of 52 playing cards and provides basic operations."

    suits = ["ハート", "ダイヤ", "クラブ", "スペード"]

    def __init__(self) -> None:
        self.cards = [Card(s, r) for s in Deck.suits for r in Card.ranks]

    def shuffle(self) -> None:
        "Shuffle the deck."
        random.shuffle(self.cards)

    def deal(self) -> tuple[list[Card], list[Card]]:
        "Deal the deck into two halves and return them."
        half = len(self.cards) // 2
        return (self.cards[:half], self.cards[half:])
