import random
import pprint

chessboard = [[0]*8 for n in range(8)]
numberQueens = 1
for numberQueens in range(9):
    random.choice(chessboard)[random.randrange(len(chessboard))] += numberQueens
pprint.pprint(chessboard)


def column(matrix, i):
    return [row[i] for row in matrix]


def get_cost(matrix):
    h = 0
    l = len(chessboard)
    col = 0
    for i in column(chessboard,col):
        print column(chessboard,col)
        for j in column(chessboard, col + 1):
            print column(chessboard, col)
            # if chessboard[i][i] == chessboard[i][j]:
            #     h += 1
            # diagonal = j - i
            # if (chessboard[i][i] == chessboard[i][j] - diagonal or chessboard[i][i] == chessboard[i][j] + diagonal):
            #     h += 1
        col += 1


# def hillClimb(matrix):
#     global column
#     moves = {}
#     i = 0
#     for col in column(chessboard,i):
#         best_move = column(chessboard,col)
#         i += 1
#         for row in range(len(chessboard)):
#             if best_move == row:
#                 continue
#             board_copy = list(chessboard)
#
#
#
#
#
# get_cost(chessboard)
# print get_cost(chessboard)
#
# def make_move_steepest_hill(board):
#     moves = {}
#     for col in range(len(board)):
#         best_move = board[col]
#
#         for row in range(len(board)):
#             if board[col] == row:
#                 # We don't need to evaluate the current
#                 # position, we already know the h-value
#                 continue
#
#             board_copy = list(board)
#             # Move the queen to the new row
#             board_copy[col] = row
#             moves[(col, row)] = get_h_cost(board_copy)
#
#     best_moves = []
#     h_to_beat = get_h_cost(board)
#     for k, v in moves.iteritems():
#         if v < h_to_beat:
#             h_to_beat = v
#
#     for k, v in moves.iteritems():
#         if v == h_to_beat:
#             best_moves.append(k)
#
#     # Pick a random best move
#     if len(best_moves) > 0:
#         pick = random.randint(0, len(best_moves) - 1)
#         col = best_moves[pick][0]
#         row = best_moves[pick][1]
#         board[col] = row
#
#     return board
#
#     # test = np.random.randint(8, size=(1, 8))
# # col = [8]
# # row = [8]
# # board = [row][col]
# get_h_cost(chessboard)
# print get_h_cost(chessboard)
# make_move_steepest_hill(chessboard)
# print make_move_steepest_hill(chessboard)

# Matrix = [[0]*2 for n in range(8)]
# value = 2
# l = len(Matrix)
# for a in range(l):
#       for b in range(len(Matrix[a])):
#                if Matrix[a][b] == value:
#                     Matrix[a][b] = 1
#                else:
#                     Matrix[a][b] = 0
# print Matrix
