import random
import pprint

chessboard = [[0]*8 for n in range(8)]
for numberQueens in range(1,8):
    random.choice(chessboard)[random.randrange(len(chessboard))] += numberQueens
pprint.pprint(chessboard)
print len(chessboard)

def get_h_cost(board):
    h = 0
    for i in range(len(board)):
        # Check every column we haven't already checked
        for j in range(i + 1, len(board)):
            # Queens are in the same row
            if board[i] == board[j]:
                h += 1
            # Get the difference between the current column
            # and the check column
            offset = j - i
            # To be a diagonal, the check column value has to be
            # equal to the current column value +/- the offset
            if board[i] == board[j] - offset or board[i] == board[j] + offset:
                h += 1

    return h


def make_move_steepest_hill(board):
    moves = {}
    for col in range(len(board)):
        best_move = board[col]

        for row in range(len(board)):
            if board[col] == row:
                # We don't need to evaluate the current
                # position, we already know the h-value
                continue

            board_copy = list(board)
            # Move the queen to the new row
            board_copy[col] = row
            moves[(col, row)] = get_h_cost(board_copy)

    best_moves = []
    h_to_beat = get_h_cost(board)
    for k, v in moves.iteritems():
        if v < h_to_beat:
            h_to_beat = v

    for k, v in moves.iteritems():
        if v == h_to_beat:
            best_moves.append(k)

    # Pick a random best move
    if len(best_moves) > 0:
        pick = random.randint(0, len(best_moves) - 1)
        col = best_moves[pick][0]
        row = best_moves[pick][1]
        board[col] = row

    return board

    # test = np.random.randint(8, size=(1, 8))
# col = [8]
# row = [8]
# board = [row][col]
get_h_cost(chessboard)
print get_h_cost(chessboard)
make_move_steepest_hill(chessboard)
print make_move_steepest_hill(chessboard)
print chessboard