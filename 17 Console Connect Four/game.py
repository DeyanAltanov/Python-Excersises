def get_player_choice(player):
    print(f"Player {player}, please choose a column:")
    return int(input()) - 1


def get_lowest_free_row_index():
    free_row_indices = []

    def lowest_row_index(board, column_index):
        while len(free_row_indices) < column_index + 1:
            free_row_indices.append(0)

        row_index = len(board) - free_row_indices[column_index] - 1
        free_row_indices[column_index] += 1
        return row_index

    return lowest_row_index


def apply_player_choice(board, column_index, player):
    row_index = lowest_row_index(board, column_index)
    board[row_index][column_index] = player
    return row_index, column_index


def in_range(value, max_value):
    return 0 <= value < max_value


def is_win_value(board, row_index, col_index, rows, cols, player):
    return in_range(col_index, cols) and in_range(row_index, rows) and board[row_index][col_index] == player



def win_condition(board, player, row_index, col_index, count=4):
    rows_count = len(board)
    cols_count = len(board[0])
    left_horizontal_values = [is_win_value(board, row_index, col_index + c, rows_count, cols_count, player) for c in range(count)]
    right_horizontal_values = [is_win_value(board, row_index, col_index - c, rows_count, cols_count, player) for c in range(count)]
    down_vertical_values = [is_win_value(board, row_index + r, col_index, rows_count, cols_count, player) for r in range(count)]
    down_left_diagonal_values = [is_win_value(board, row_index + d, col_index - d, rows_count, cols_count, player) for d in range(count)]
    down_right_diagonal_values = [is_win_value(board, row_index + d, col_index + d, rows_count, cols_count, player) for d in range(count)]
    up_left_diagonal_values = [is_win_value(board, row_index - d, col_index - d, rows_count, cols_count, player) for d in range(count)]
    up_right_diagonal_values = [is_win_value(board, row_index - d, col_index + d, rows_count, cols_count, player) for d in range(count)]
    return all(left_horizontal_values) or all(down_vertical_values) or all(right_horizontal_values) or all(down_left_diagonal_values) or all(down_right_diagonal_values) or all(up_left_diagonal_values) or all(up_right_diagonal_values)


def print_winner_message(player):
    print(f"The winner is player {player}!")


def is_valid(board, index):
    return len(board[0]) > index >= 0 == board[0][index]


def print_board(board):
    for row in board:
        print(row)


def play(board, player=1):
    while True:
        player_choice = get_player_choice(player)
        if not is_valid(board, player_choice):
            print('Invalid index!')
            continue
        row_index, col_index = apply_player_choice(board, player_choice, player)
        print_board(board)
        if win_condition(board, player, row_index, col_index):
            print_winner_message(player)
            break
        player = 2 if player == 1 else 1


def create_board(rows=6, cols=7):
    return [[0] * cols for _ in range(rows)]


print(f"Rows count: ", end='')
rows = int(input())
while True:
    if rows < 5:
        print("Value cannot be less than 5.")
    else:
        break
    print(f"Rows count: ", end='')
    rows = int(input())

print(f"Cols count: ", end='')
cols = int(input())
while True:
    if cols < 5:
        print("Value cannot be less than 5.")
    else:
        break
    print(f"Cols count: ", end='')
    cols = int(input())

lowest_row_index = get_lowest_free_row_index()
board = create_board(rows, cols)
play(board)