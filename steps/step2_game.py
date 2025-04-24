# war_game/steps/step2_game.py
"""
Step2: スコア機能を追加した WarGame のエントリポイント。
各ラウンドの勝者をスコアとして累積します。
"""

from war_game.core.base_game import WarGame


def main() -> None:
    names = ["プレイヤー1", "プレイヤー2"]
    game = WarGame(names)
    game.start()


if __name__ == "__main__":
    main()
