import os
import sys

class InfiniteTicTacToe:
    def __init__(self):
        # 3x3 board represented by a flat list
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        
        # Queues to track the sequence of moves for each player
        # Move history looks like: [oldest_move, middle_move, newest_move]
        self.move_history = {"X": [], "O": []}

    def clear_screen(self):
        """Clears the terminal screen for a clean UI."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self):
        """Prints a clean, formatted grid with helpful warnings."""
        self.clear_screen()
        print("=== INFINITE TIC-TAC-TOE ===")
        print("Rule: Placing a 4th piece deletes your 1st piece!\n")
        
        # Visual cues: Let players know if a piece is about to fade out
        for player in ["X", "O"]:
            if len(self.move_history[player]) == 3:
                oldest_index = self.move_history[player][0]
                # Convert list index to grid position (1-9) for user readability
                grid_pos = oldest_index + 1
                print(f"⚠️  Notice: Player {player}'s piece at position {grid_pos} will vanish next turn.")
        print()

        # Displaying the 3x3 layout
        b = self.board
        print(f" {b[0]} | {b[1]} | {b[2]}     [ 1 | 2 | 3 ]")
        print("---+---+---    ---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]}     [ 4 | 5 | 6 ]")
        print("---+---+---    ---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]}     [ 7 | 8 | 9 ]")
        print("\n============================\n")

    def check_winner(self):
        """Checks the 8 standard winning combinations."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in win_conditions:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]
        return None

    def make_move(self, position):
        """Handles placement logistics and sequential piece deletion."""
        index = position - 1  # Map 1-9 input to 0-8 indexing
        player = self.current_player

        # 1. Update Board and Player History Array
        self.board[index] = player
        self.move_history[player].append(index)

        # 2. Deletion Mechanic: Check if player has dropped their 4th piece
        if len(self.move_history[player]) > 3:
            # Pop the oldest index tracking position from history queue
            vanished_index = self.move_history[player].pop(0)
            # Clear it off the actual visible board canvas
            self.board[vanished_index] = " "

        # 3. Swap Turn
        self.current_player = "O" if player == "X" else "X"

    def play_game(self):
        """Primary gameplay loop execution."""
        while True:
            self.display_board()
            print(f"Player {self.current_player}'s Turn.")
            
            # Input capturing and validation logic
            try:
                move = int(input("Choose an open position (1-9): "))
                if move < 1 or move > 9:
                    input("Invalid input. Position must be between 1 and 9. Press Enter...")
                    continue
                if self.board[move - 1] != " ":
                    input("That cell is already occupied! Press Enter...")
                    continue
            except ValueError:
                input("Invalid input. Please enter a valid number (1-9). Press Enter...")
                continue

            # Execute valid choice move
            self.make_move(move)

            # Check if that move triggered a victory state
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"🎉 Congratulations! Player {winner} wins the match! 🎉\n")
                break

if __name__ == "__main__":
    # Launch game instances natively
    game = InfiniteTicTacToe()
    game.play_game()