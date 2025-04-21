import pytest
from step1_war_game.deck import Deck
from step1_war_game.card import Card


def test_deck_count():
    deck = Deck()
    assert len(deck.cards) == 52


def test_shuffle_changes_order():
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    assert any(
        c1.rank != c2.rank or c1.suit != c2.suit
        for c1, c2 in zip(deck1.cards, deck2.cards)
    )


def test_deal_halves():
    deck = Deck()
    half1, half2 = deck.deal()
    assert len(half1) == 26
    assert len(half2) == 26
    all_cards = half1 + half2
    expected = {(s, r) for s in Deck.suits for r in Card.ranks}
    assert {(c.suit, c.rank) for c in all_cards} == expected