import random

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.current_player = 'X'

    def print_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print('| ' + ' | '.join(self.board[i:i+3]) + ' |')
            print('-------------')

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.check_winner('X') or self.check_winner('O') or self.is_board_full()

    def make_move(self, move):
        if self.board[move] == ' ':
            self.board[move] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def get_available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def play_random_move(self):
        available_moves = self.get_available_moves()
        if available_moves:
            return self.make_move(random.choice(available_moves))
        return False

    def play(self):
        while not self.is_game_over():
            self.print_board()
            if self.current_player == 'X':
                move = int(input("Enter your move (0-8): "))
                while move not in self.get_available_moves():
                    move = int(input("Invalid move. Enter your move (0-8): "))
                self.make_move(move)
            else:
                self.play_random_move()
        self.print_board()
        if self.check_winner('X'):
            print("X wins!")
        elif self.check_winner('O'):
            print("O wins!")
        else:
            print("It's a draw!")

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
