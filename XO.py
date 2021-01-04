from colored import stylize, fg


class XO:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.symbols = ["X", "Y"]

    def set(self, index, symbol):
        if not (self.board[index] == "X" or self.board[index] == "O"):
            self.board[index] = symbol
            return True
        else:
            return False

    

    def isTie(self):
        if not self.isWinner(self.symbols[0]) and not self.isWinner(self.symbols[1]):
            return True
