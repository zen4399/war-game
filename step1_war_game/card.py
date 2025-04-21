class Card:
    "Represents a single playing card with suit and rank."

    ranks = ["A", "K", "Q", "J", "10", "9", "8",
             "7", "6", "5", "4", "3", "2"]

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def strength(self) -> int:
        """
        Return the strength index of this card.
        A smaller index means a stronger card.
        """
        return Card.ranks.index(self.rank)

    def __str__(self) -> str:
        "String representation for printing."
        return f"{self.suit}の{self.rank}"
