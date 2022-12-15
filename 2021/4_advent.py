choice = [
    13,
    79,
    74,
    35,
    76,
    12,
    43,
    71,
    87,
    72,
    23,
    91,
    31,
    67,
    58,
    61,
    96,
    16,
    81,
    92,
    41,
    6,
    32,
    86,
    77,
    42,
    0,
    55,
    68,
    14,
    53,
    26,
    25,
    11,
    45,
    94,
    75,
    1,
    93,
    83,
    52,
    7,
    4,
    22,
    34,
    64,
    69,
    88,
    65,
    66,
    39,
    97,
    27,
    29,
    78,
    5,
    49,
    82,
    54,
    46,
    51,
    28,
    98,
    36,
    48,
    15,
    2,
    50,
    38,
    24,
    89,
    59,
    8,
    3,
    18,
    47,
    10,
    90,
    21,
    80,
    73,
    33,
    85,
    62,
    19,
    37,
    57,
    95,
    60,
    20,
    99,
    17,
    63,
    56,
    84,
    44,
    40,
    70,
    9,
    30,
]

# Set up 2D array
boards = []
with open("4_input.txt") as f:
    board = []
    for line in f:
        if line.strip() == "":
            boards.append(board)
            board = []
            continue
        s = line.strip().split(" ")
        without_empty_strings = [string for string in s if string != ""]
        s = without_empty_strings
        p = []
        for i in range(len(s)):
            p.append(int(s[i]))
        board.append(p)

# go through each board and mark the numbers (add a star?)
# at the end, check for marked row or column


def checkWin(board):
    rowStreak = 0
    columnStreak = 0
    for i in range(5):
        for j in range(5):
            val = board[i][j]
            if val >= 1000:  # then number has been guessed
                rowStreak += 1
        if rowStreak == 5:
            return True
        else:
            rowStreak = 0
    for i in range(5):
        for j in range(5):
            val = board[j][i]
            if val >= 1000:  # then number has been guessed
                columnStreak += 1
        if columnStreak == 5:
            return True
        else:
            columnStreak = 0
    return False


# TODO: giga loop these chad loops
winningScore = 0
hasWon = False
choiceNum = 0
winningBoard = []
while not hasWon:
    for i in range(len(boards)):  # go through all the boards
        for j in range(5):  # we know it's 5 x 5
            for k in range(5):
                num = boards[i][j][k]
                if num == choice[choiceNum]:
                    num += 1000
                    boards[i][j][k] = num
        if checkWin(boards[i]):
            hasWon = True
            winningBoard = boards[i]
            winningScore = choice[choiceNum]
            print("Done")
            break
    choiceNum += 1

sum = 0
for i in range(5):
    for j in range(5):
        if winningBoard[i][j] < 1000:
            sum += winningBoard[i][j]

print(winningBoard)
print(choiceNum)
print(sum)
