import pytest
from step1_war_game.card import Card


def test_card_strength():
    card_A = Card("ハート", "A")
    assert card_A.strength() == 0
    card_2 = Card("スペード", "2")
    assert card_2.strength() == len(Card.ranks) - 1


def test_str():
    card = Card("ダイヤ", "10")
    assert str(card) == "ダイヤの10"
