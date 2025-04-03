def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}, enter your move (row and column, e.g., 1 2): ")

        try:
            row, col = map(int, input().split())
            if board[row][col] == " ":
                board[row][col] = current_player
            else:
                print("That spot is taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as numbers between 0 and 2.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
