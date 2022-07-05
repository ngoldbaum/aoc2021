with open("input") as f:
    input = f.read().split("\n\n")

draws = list(map(int, input[0].split(",")))
boards = [
    list(map(lambda r_str: list(map(int, r_str.split())), r_str))
    for r_str in [b.split("\n") for b in input[1:]]
]
marks = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]


def mark(boards, marks, draw):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, el in enumerate(row):
                if el == draw:
                    marks[i][j][k] = True


def get_winning_score(board, marks):
    score = 0
    for row, row_marks in zip(board, marks):
        for el, mark in zip(row, row_marks):
            if mark is False:
                score += el
    return score


def score(boards, marks):
    ret = []
    for i, (board, mark_rows) in enumerate(zip(boards, marks)):
        mark_columns = list(zip(*mark_rows))
        for mark_row, mark_column in zip(mark_rows, mark_columns):
            if all(mark_row) or all(mark_column):
                ret.append((i, get_winning_score(board, mark_rows)))
    return ret


for draw in draws:
    mark(boards, marks, draw)
    winners = score(boards, marks)
    if winners:
        # reverse sort by index since we delete winning boards below, this
        # avoids corrupting the board index as we delete boards
        winners = sorted(winners, key=lambda el: el[0], reverse=True)
        for winner_board, winner_score in winners:
            print(
                f"board {winner_board} won with score {winner_score*draw} on draw {draw}"
            )
            del boards[winner_board]
            del marks[winner_board]
