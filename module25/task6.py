class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                print(f"Игрок {self.current_player} выиграл!")
                return True
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Эта клетка уже занята!")

    def check_winner(self, row, col):
        player = self.board[row][col]
        return (
            all(self.board[row][i] == player for i in range(3)) or
            all(self.board[i][col] == player for i in range(3)) or
            all(self.board[i][i] == player for i in range(3)) or
            all(self.board[i][2 - i] == player for i in range(3))
        )

game = TicTacToe()
game.print_board()

while True:
    row = int(input("Введите номер строки (0-2): "))
    col = int(input("Введите номер столбца (0-2): "))
    if game.make_move(row, col):
        break
    game.print_board()
