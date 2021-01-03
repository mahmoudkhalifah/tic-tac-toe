from colored import stylize, fg


class XO:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.symbols = ["X","Y"]

    def set(self, index, symbol):
        if not (self.board[index] == "X" or self.board[index] == "O"):
            self.board[index] = symbol
            return True
        else: return False

    def isWinner(self, symbol):
        # check the row s
        for i in range(0, 9, 3):
            if self.board[i] == symbol and self.board[i + 1] == symbol and self.board[i + 2] == symbol:
                return True
        # check the columns
        for i in range(0, 3):
            if self.board[i] == symbol and self.board[i + 3] == symbol and self.board[i + 6] == symbol:
                return True
        # check from left to right diagonal
        if self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol:
            return True
        # check from right to left diagonal
        if self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol:
            return True
        return False

    def isTie(self):
        if not self.isWinner(self.symbols[0]) and not self.isWinner(self.symbols[1]):
            return True
