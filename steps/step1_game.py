# war_game/steps/step1_game.py
"""
Step1: シンプルな一回だけの対戦を表示するエントリポイント。
このコードは、WarGame クラスをインスタンス化し、ゲームを開始します。
"""

from war_game.core.base_game import WarGame


def main() -> None:
    names = ["プレイヤー1", "プレイヤー2"]
    game = WarGame(names)
    game.play_round()
    print("戦争を終了します。")


if __name__ == "__main__":
    main()
