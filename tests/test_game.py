import pytest
import step1_war_game.deck as deck_mod
from step1_war_game.game import WarGame


def test_game_runs(capsys, monkeypatch):
    monkeypatch.setattr(deck_mod.Deck, "shuffle", lambda self: None)

    def fake_deal(self):
        from step1_war_game.card import Card
        return ([Card("ハート", "A")], [Card("スペード", "2")])
    monkeypatch.setattr(deck_mod.Deck, "deal", fake_deal)

    game = WarGame()
    game.start()
    captured = capsys.readouterr()
    assert "戦争を開始します" in captured.out
    assert "プレイヤー1が勝ちました" in captured.out