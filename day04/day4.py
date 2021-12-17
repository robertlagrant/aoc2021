from raw_input import raw_boards, numbers

board_size = 5
boards = [[[int(num_s) for num_s in raw_row.split()] for raw_row in raw_board.split("\n")] for raw_board in raw_boards]


def check_board_marks(marked_board):
    combos = [[(i, j) for j in range(board_size)] for i in range(board_size)] + \
             [[(j, i) for j in range(board_size)] for i in range(board_size)]

    return any(all(item in marked_board for item in combo) for combo in combos)


def run_game(winning_boards_stop_count: int):
    winner_boards = set()
    marked_boards = [set() for _ in boards]
    for num in numbers:
        for i, board in enumerate(boards):
            if i not in winner_boards:
                for row in range(board_size):
                    for col in range(board_size):
                        if board[row][col] == num:
                            marked_boards[i].add((row, col))

            if check_board_marks(marked_boards[i]):
                winner_boards.add(i)
                if len(winner_boards) == winning_boards_stop_count:
                    return score_game(i, marked_boards) * num


def score_game(index: int, marked_boards: list[set]):
    return sum(boards[index][row][col]
               for col in range(board_size)
               for row in range(board_size)
               if (row, col) not in marked_boards[index])


print(f"Part 1: {run_game(1)}")
print(f"Part 2: {run_game(len(boards))}")
