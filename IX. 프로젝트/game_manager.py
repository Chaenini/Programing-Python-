from tictactoe import TicTacToe


class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        print(self.ttt)
        self.ttt.set(1, 1)
        print(self.ttt)


if __name__ == '__main__':
    gm = GameManager()
    gm.play()