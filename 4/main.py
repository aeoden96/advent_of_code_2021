import itertools as it

def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            yield line.rstrip()


def read_tables(path):
    f = get_input(path)

    numbers = next(f).split(",")
    numbers = [int(i) for i in numbers]

    boards = []
    board = [[0] * 5 for i in range(5)]
    i = 0
    for line in f:
        if len(line) == 0:
            continue
        if i == 0:
            board = [[0]*5 for i in range(5)]
        board[i] = line.split()
        board[i] = [int(k) for k in board[i]]
        i += 1
        if i == 5:
            boards.append(board)
            i = 0

    return numbers, boards


def check_boards(boards):
    for k, board in enumerate(boards):
        for row in board:
            if sum(row) == 5:
                return k
        for col in zip(*board):
            if sum(col) == 5:
                return k
    return -1


numbers, boards = read_tables("input.txt")

boards_mark = []
for board in boards:
    # board_copy = [row[:] for row in board]
    board_copy = [[0] * 5 for i in range(5)]
    boards_mark.append(board_copy)

bb = [i for i in range(100)]
won_boards = set()

for n in numbers:
    print("Boards left",len(boards))

    for board_ind, board in enumerate(boards):
        for i in range(5):
            for j in range(5):
                if board[i][j] == n:
                    boards_mark[board_ind][i][j] = 1
    last_num = n
    if len(boards) == 1 and (k := check_boards(boards_mark)) != -1:
        break
    while (k := check_boards(boards_mark)) != -1:
        print("Board", bb[k]+1, "wins.")
        won_boards.add(bb[k])
        del boards[k]
        del boards_mark[k]
        del bb[k]

print(boards)
winning_board = boards[0]
winning_board_mark = boards_mark[0]

S = 0
for i in range(5):
    for j in range(5):
        if winning_board_mark[i][j] == 0:
            S += winning_board[i][j]

print(S)
print(S*last_num)

