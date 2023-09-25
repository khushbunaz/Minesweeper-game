import random

def create_board(rows, cols, mines):
    # Create an empty board filled with zeros
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly on the board
    for _ in range(mines):
        while True:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            if board[row][col] != -1:
                board[row][col] = -1
                break

    # Calculate numbers around mines
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == -1:
                continue
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= row + dr < rows and 0 <= col + dc < cols and board[row + dr][col + dc] == -1:
                        board[row][col] += 1

    return board

def print_board(board, revealed):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if revealed[row][col]:
                if board[row][col] == -1:
                    print("*", end=" ")
                else:
                    print(board[row][col], end=" ")
            else:
                print(".", end=" ")
        print()

def reveal(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True

    if board[row][col] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if 0 <= row + dr < len(board) and 0 <= col + dc < len(board[0]):
                    reveal(board, revealed, row + dr, col + dc)

def play_minesweeper(rows, cols, mines):
    board = create_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    while True:
        print_board(board, revealed)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))

        if board[row][col] == -1:
            print("Game Over! You hit a mine!")
            break
        else:
            reveal(board, revealed, row, col)

        # Check if all non-mined cells are revealed
        if all(all(revealed[row][col] or board[row][col] == -1 for col in range(cols)) for row in range(rows)):
            print("Congratulations! You win!")
            break

if __name__ == "__main__":
    rows = 10
    cols = 10
    mines = 20
    play_minesweeper(rows, cols, mines)
