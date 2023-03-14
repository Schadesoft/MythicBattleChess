import random

# Set up the board
board = []
for i in range(8):
    row = []
    for j in range(8):
        row.append(" ")
    board.append(row)

# Define the pieces
pieces = {
    "gnome": {"symbol": "G", "moves": [(-1, -1), (-1, 1), (1, -1), (1, 1)]},
    "valkyrie": {"symbol": "V", "moves": [(-1, -2), (-2, -1), (1, -2), (-2, 1), (1, 2), (2, 1), (-1, 2), (2, -1)]},
    "hoplite": {"symbol": "H", "moves": [(-1, 0), (1, 0)]},
    "centaur": {"symbol": "C", "moves": [(0, -1), (0, 1)]},
    "minotaur": {"symbol": "M", "moves": [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -2), (0, 2), (-2, 0), (2, 0)]}
}

# Define the players
players = {
    "Greek": {"pieces": ["hoplite", "centaur", "minotaur"], "color": "W"},
    "Norse": {"pieces": ["gnome", "valkyrie", "minotaur"], "color": "B"}
}

# Place the pieces randomly on the board
for player, data in players.items():
    for piece in data["pieces"]:
        while True:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if board[row][col] == " ":
                board[row][col] = data["color"] + pieces[piece]["symbol"]
                break

# Define the function to print the board
def print_board(board):
    print("   a b c d e f g h")
    print("  +-----------------+")
    for i in range(8):
        row = str(i+1) + " |"
        for j in range(8):
            row += board[i][j] + "|"
        print(row)
        print("  +-----------------+")

# Define the function to check if a move is valid
def is_valid_move(board, piece, row, col, new_row, new_col):
    # Check if the new position is on the board
    if new_row < 0 or new_row > 7 or new_col < 0 or new_col > 7:
        return False
    # Check if the piece can make that move
    moves = pieces[piece]["moves"]
    move = (new_row - row, new_col - col)
    if move not in moves:
        return False
    # Check if there is no piece of the same color at the new position
    if board[new_row][new_col] != " " and board[new_row][new_col][0] == board[row][col][0]:
        return False
    return True

# Define the function to move a piece
def move_piece(board, row, col, new_row, new_col):
    piece = board[row][col][1]
    board[new_row][new_col] = board[row][col]
    board[row][col] = " "

# Play the game
