"""TicTacToe"""
import numpy as np


class TicTacToe():
    """Get all TicTacToe playing stuff here."""

    def __init__(self, player1="X", player2="O"):
        self.board = np.zeros([3, 3])
        self.turn = 1
        self.player1 = player1
        self.player2 = player2
        self._play_values = {self.player1: -1, self.player2: 1}
        self.active_player = self.player1
        self.game_active = True

    def _boardsum(self):
        """Recalculate sum in all directions to get status of game."""
        b = self.board
        return [
            *np.sum(b, axis=0),  # horizontal
            *np.sum(b, axis=1),  # vertical
            np.sum(np.diag(b)),  # diagonal
            np.sum([b[0, 2], b[1, 1], b[2, 0]]),  # antidiagonal
        ]

    def _game_status(self):
        """Get status of game (active?)."""
        if self.turn == 9 or 3 in self._boardsum() or -3 in self._boardsum():
            self.game_active = False
        return self.game_active

    def apply_update(self, x, y):
        """Apply update to board - set mark.
        TODO: Bad conditions for correct move."""
        if x in [0, 1, 2] and y in [0, 1, 2] and self.game_active:
            b = self.board
            if b[x, y] == 0:
                b[x, y] = self._play_values[self.active_player]
                self.turn += 1
                self._update_active_player()
                self._game_status()
                print("set")
                return True
            else:
                print("try again")
        else:
            print("wrong")
        return False

    def _update_active_player(self):
        """Change active player from player1 to player2 and vice versa.
        Keep until there is a better idea."""
        if self.active_player == self.player1:
            self.active_player = self.player2
        elif self.active_player == self.player2:
            self.active_player = self.player1

    def play(self):
        """Play a game of TicTacToe."""
        self.turn = 1
        while self.game_active:
            print("It`s {}s turn.".format(self.active_player))
            self.apply_update(0, 0)
            self.turn += 1
            self._update_active_player()


def test():
    t = TicTacToe('Hallo', 'Welt!')
    print(t._play_values.keys())
    print(t._play_values.values())
    t.apply_update(0, 0)
    t.apply_update(1, 0)
    t.apply_update(0, 1)
    t.apply_update(1, 1)
    t.apply_update(0, 2)
    t.apply_update(1, 2)
    b = t.board
    print(b)
    print(t._boardsum())
    print(t.game_active)


if __name__ == "__main__":
    test()
