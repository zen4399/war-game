from typing import List, Optional
from .card import Card


class Player:
    """Represents a player in the War game."""

    def __init__(self, name: str, hand: List[Card]) -> None:
        self.name = name
        self.hand = hand

    def draw_card(self) -> Optional[Card]:
        """Draw(pop) the top card from the player's hand.
        Returns None if the hand is empty."""
        if self.hand:
            return self.hand.pop(0)
        return None

    def has_cards(self) -> bool:
        """Check if the player still has any cards."""
        return bool(self.hand)
