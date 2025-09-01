#!/usr/bin/python3
def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check all win conditions (rows, columns, diagonals)."""
    # Rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    # Columns
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]
                and board[0][col] != " "):
            return board[0][col]

    # Diagonals
    if (board[0][0] == board[1][1] == board[2][2]
            and board[0][0] != " "):
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]
            and board[0][2] != " "):
        return board[0][2]

    return None


def is_board_full(board):
    """Return True if there are no empty spaces left."""
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_input(prompt):
    """Prompt the user for a number between 0 and 2."""
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1, 2):
                return value
            print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def tic_tac_toe():
    """Main game loop."""
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
