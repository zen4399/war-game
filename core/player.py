import random
from .card import Card


class Player:
    """Represents a player in the War game."""

    def __init__(self, name: str, hand: list[Card]) -> None:
        self.name = name
        self.hand = hand
        self.won_cards = []  # 勝利して獲得したカードを保持するリスト
        self.total_won_count = 0    # 獲得したカードの枚数をカウントする変数

    def has_cards(self) -> bool:
        """Check if the player still has any cards."""
        return len(self.hand) > 0 or len(self.won_cards) > 0

    def check_and_refill(self) -> None:
        """手札が空の場合、勝利カードをシャッフルして手札に加える"""
        if not self.hand and self.won_cards:
            random.shuffle(self.won_cards)
            self.hand = self.won_cards
            self.won_cards = []


    def draw_card(self) -> Card | None:
        """Draw (pop) the top card from the player's hand.
        Returns None if the hand is empty."""
        self.check_and_refill()
        if self.hand:
            return self.hand.pop(0)
        return None

    def add_cards(self, cards: list[Card]) -> None:
        """Add cards to the won_cards pile."""
        added = len(cards)
        self.won_cards.extend(cards)
        self.total_won_count += added

    def total_cards(self) -> int:
        """Return the total number of cards (hand + won)."""
        return len(self.hand) + len(self.won_cards)
