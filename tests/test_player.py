import pytest
from step1_war_game.player import Player
from step1_war_game.card import Card


def test_draw_and_has_cards():
    hand = [Card("ハート", "A"), Card("ダイヤ", "K")]
    player = Player("p", hand.copy())
    card = player.draw_card()
    assert isinstance(card, Card)
    assert player.has_cards()
    player.draw_card()
    assert not player.has_cards()
    assert player.draw_card() is None
