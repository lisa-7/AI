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

    def evaluate_state(self, player):
        # Heuristic evaluation function
        # Assign a score to the game state based on desirability for the given player
        score = 0
        if self.check_winner(player):
            score += 10
        if self.check_winner('X' if player == 'O' else 'O'):
            score -= 10
        return score

    def get_best_move(self):
        best_score = float('-inf')
        best_move = None
        for move in self.get_available_moves():
            self.make_move(move)
            score = self.minimax(0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, depth, maximizing_player):
        if self.is_game_over():
            return self.evaluate_state('O')  # Assuming AI is 'O'
        
        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_available_moves():
                self.make_move(move)
                eval = self.minimax(depth+1, False)
                self.board[move] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_available_moves():
                self.make_move(move)
                eval = self.minimax(depth+1, True)
                self.board[move] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def play(self):
        while not self.is_game_over():
            self.print_board()
            if self.current_player == 'X':
                move = int(input("Enter your move (1-9): ")) - 1  # Adjust move to 0-based indexing
                while move not in self.get_available_moves():
                    move = int(input("Invalid move. Enter your move (1-9): ")) - 1
                self.make_move(move)
            else:
                self.make_move(self.get_best_move())
        self.print_board()
        if self.check_winner('X'):
            print("You win!")
        elif self.check_winner('O'):
            print("AI wins!")
        else:
            print("It's a draw!")

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
