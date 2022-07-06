with open("input") as f:
    input = f.read().split("\n\n")

draws = list(map(int, input[0].split(",")))
boards = [
    list(
        map(lambda r_str: list(map(lambda el: [int(el), False], r_str.split())), r_str)
    )
    for r_str in [b.split("\n") for b in input[1:]]
]


def mark(boards, draw):
    for board in boards:
        for row in board:
            for el in row:
                if el[0] == draw:
                    el[1] = True


def get_winning_score(board):
    score = 0
    for row in board:
        for el in row:
            if el[1] is False:
                score += el[0]
    return score


def check_marks(el):
    return el[1]


def score(boards):
    ret = []
    for i, board in enumerate(boards):
        board_t = list(zip(*board))
        for board_row, board_column in zip(board, board_t):
            if all(map(check_marks, board_row)) or all(map(check_marks, board_column)):
                ret.append((i, get_winning_score(board)))
    return ret


for draw in draws:
    mark(boards, draw)
    winners = score(boards)
    if winners:
        # reverse sort by index since we delete winning boards below, this
        # avoids corrupting the board index as we delete boards
        winners = sorted(winners, key=lambda el: el[0], reverse=True)
        for winner_board, winner_score in winners:
            print(
                f"board {winner_board} won with score {winner_score*draw} on draw {draw}"
            )
            del boards[winner_board]
