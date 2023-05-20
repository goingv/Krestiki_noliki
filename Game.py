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
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Некорректный ход! Поле уже занято.")

    def check_winner(self):
        # Проверка по горизонтали
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Проверка по вертикали
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Проверка по диагоналям
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        # Ничья
        if all([cell != " " for row in self.board for cell in row]):
            return "Ничья"

        # Игра продолжается
        return None


game = TicTacToe()

while True:
    game.print_board()

    row = int(input("Введите номер строки (0-2): "))
    col = int(input("Введите номер столбца (0-2): "))

    game.make_move(row, col)

    winner = game.check_winner()
    if winner:
        print("Игра окончена.")
        if winner == "Ничья":
            print("Ничья!")
        else:
            print(f"Победитель: {winner}!")
        break
