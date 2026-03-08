import random

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def move_computer():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            break


def play_tic_tac_toe():
    computer = "O"
    plyaer = "X"
    while True:
        print_board(board)

        while True:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = plyaer
                break
            print("Invalid move. Try again.")

        if check_win(board, plyaer):
            print("You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        move_computer()

        if check_win(board, computer):
            print("Computer wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_tic_tac_toe()
