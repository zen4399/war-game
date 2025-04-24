from .card import Card
from .deck import Deck
from .player import Player


class WarGame:
    """Main class to manage the War card game logic."""

    def __init__(self, player_names: list[str]) -> None:
        if not 2 <= len(player_names) <= 5:
            raise ValueError("プレイヤーの人数は2~5人にしてください。")

        print("戦争を開始します。")
        self.deck = Deck()
        self.deck.shuffle()
        hands = self.deck.deal(len(player_names))
        self.players = [
            Player(name, hand) for name, hand in zip(player_names, hands)
        ]
        print("カードが配られました。")

    def play_round(self) -> tuple[Player | None, list[Card]]:
        pool: list[Card] = []
        
        while True:
            print("戦争!")
            table_cards: list[Card] = []
            draws: list[tuple[Player, Card]] = []

            for p in self.players:
                card = p.draw_card()
                if card is None:
                    return None, pool
                draws.append((p, card))
                table_cards.append(card)
                print(f"{p.name}のカードは{card}です。")

            pool.extend(table_cards)
            strengths = [(p, c.strength()) for p, c in draws]
            min_str = min(s for _, s in strengths)
            winners = [p for p, s in strengths if s == min_str]

            if len(winners) == 1:
                winner = winners[0]
                print(f"{winner.name}が勝ちました。")
                return winners[0], pool
            else:
                print("引き分けです。")


    def start(self) -> None:
        table_pool: list[Card] = []

        while all(p.has_cards() for p in self.players):
            winner, cards_used = self.play_round()
            table_pool.extend(cards_used)

            if winner:
                print(f"{winner.name}は{len(table_pool)}枚のカードをもらいました。")
                winner.add_cards(table_pool)
                table_pool = []
            
            for p in self.players:
                if not p.has_cards():
                    print(f"{p.name}の手札がなくなりました。")

        for p in self.players:
            print(f"{p.name}の手札の枚数は{p.total_cards()}枚です。")

        ranking = sorted(self.players, key=lambda p: p.total_cards(), reverse=True)
        for i, player in enumerate(ranking, start=1):
            print(f"{player.name}が{i}位です。")
        
        print("戦争を終了します。")