def possible(n, board, x, y):
    if any([n in line for line in board]):
            return False
    if y >= 2 and x == 1:
        if sum(board[0]) + board[1][1] != sum(board[y-1]) + n:
            return False
    if y == 4 and x == 1:
        if sum(board[0]) + board[1][1] != board[y][0] + n + board[0][1]:
            return False
    return True

board = [
    [0, 0], 
    [0, 0], 
    [0, 0], 
    [0, 0], 
    [0, 0] 
    ]

highscore = 0

def solve():
    global board
    global highscore
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                for n in range(1, 11):
                    if possible(n, board, x, y):
                        board[y][x] = n
                        solve()
                        if not any([0 in line for line in board]):
                            flat = []
                            first_nums = [line[0] for line in board]
                            starting_node = min(first_nums)
                            start = first_nums.index(starting_node)

                            board_copy = [board[(start + i) % 5] for i in range(5)]
                            for line_no, line in enumerate(board_copy):
                                for num in line:
                                    flat.append(num)
                                flat.append(board_copy[(line_no+1)%5][1])
                            joined = int("".join([str(num) for num in flat]))
                            if joined > highscore and len(str(joined)) == 16:
                                highscore = joined
                        board[y][x] = 0
                return

solve()
print(highscore)
