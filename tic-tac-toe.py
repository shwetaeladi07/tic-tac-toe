# Tic-Tac-Toe

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to play the game
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Initialize players
    players = ["X", "O"]
    current_player = players[0]

    # Game loop
    while True:
        print_board(board)

        # Get the current player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Update the board
        board[row][col] = current_player

        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if it's a tie
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the next player
        current_player = players[(players.index(current_player) + 1) % 2]

# Start the game
play_game()