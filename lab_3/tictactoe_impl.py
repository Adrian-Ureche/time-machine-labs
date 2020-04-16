class Game:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.move_count = 0

    def __repr__(self):
        return (
            f"Game(\n"
            f"    {self.board[0]}\n"
            f"    {self.board[1]}\n"
            f"    {self.board[2]}\n"
            f")\n"
        )

    def mark(self, x, y):
        self.move_count += 1
        if self.move_count % 2 == 1:
            symbol = "X"
        else:
            symbol = "O"
        self.board[x][y] = symbol
