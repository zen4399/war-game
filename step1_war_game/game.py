# from .card import Card
from .deck import Deck
from .player import Player


class WarGame:
    """Main class to manage the War card game logic."""

    def __init__(self) -> None:
        print("戦争を開始します。")
        self.deck = Deck()
        self.deck.shuffle()
        half1, half2 = self.deck.deal()

        self.player1 = Player("プレイヤー1", half1)
        self.player2 = Player("プレイヤー2", half2)

        print("カードが配られました。")

    def play_round(self) -> int | None:
        """Conduct a single War round. Returns the winner (1 or 2) or None."""

        # テーブル上に出されたカードを保持しておくリスト
        # table_cards: list[Card] = []

        while True:
            # print("戦争!")

            # どちらかのプレイヤーがカードを切らせた場合は続行不能
            if not self.player1.has_cards() or not self.player2.has_cards():
                return None

            card1 = self.player1.draw_card()
            card2 = self.player2.draw_card()

            # 万が一Noneが返る場合はデッキ切れ
            if card1 is None or card2 is None:
                return None

            # table_cards.extend([card1, card2])

            print(f"{self.player1.name}のカードは {card1} です。")
            print(f"{self.player2.name}のカードは {card2} です。")

            strength1 = card1.strength()
            strength2 = card2.strength()

            if strength1 < strength2:
                return 1
            elif strength1 > strength2:
                return 2
            else:
                print("引き分けです。")
                print("戦争！")

    def start(self) -> None:
        """Start the War game."""
        print("戦争!")

        winner = self.play_round()

        if winner is None:
            print("どちらかの手札がなくなったため終了します。")
        else:
            print(f"プレイヤー{winner}が勝ちました。")
        print("戦争を終了します。")


def main() -> None:
    game = WarGame()
    game.start()


if __name__ == "__main__":
    main()
