f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/year 2022/day9_input.txt", "r")
text = f.read()
text = text.splitlines()
text = [[line.split()[0], int(line.split()[1])] for line in text]

## 1.Determine dimension
# x: column , y = row
x, y = 0, 0
x_max, x_min = 0, 0
y_max, y_min = 0, 0
x_len, y_len = 0, 0
moves = [] # moves = [[x0, y0], [x1, y1], .....]

for move in text:
    if move[0] == 'L':
        x = x - move[1]
        moves.append([x, y])
    elif move[0] == 'R':
        x = x + move[1]
        moves.append([x, y])
    elif move[0] == 'U':
        y = y - move[1]
        moves.append([x, y])
    elif move[0] == 'D':
        y = y + move[1]
        moves.append([x, y])

x_max = max(moves, key=lambda x:x[0])[0]
x_min = min(moves, key=lambda x:x[0])[0]
x_len = x_max - x_min + 1

y_max = max(moves, key=lambda y:y[1])[1]
y_min = min(moves, key=lambda y:y[1])[1]
y_len = y_max - y_min + 1

## 2. Determine starting point
x_0 = x_len - x_max -1 # Column (index)
y_0 = y_len - y_max -1 # Row    (index)

## Function check if it is neccesary to move the tail: True|False

def move_tail(rowT_m, colT_m, rowH_m, colH_m):

    if abs(rowT_m - rowH_m) > 1 or abs(colT_m - colH_m) > 1:
        return True
    else:
        return False

## keep track of the tail steps by #
trail_track = [['0' for i in range(x_len)] for u in range(y_len)]
n_positions = 0

def tacking(rowT_t, colT_t, n_pos):
    
    if trail_track[rowT_t][colT_t] != '#':
        trail_track[rowT_t][colT_t] = '#'
        n_pos += 1

    return n_pos

rowT, colT = y_0, x_0
rowH, colH = y_0, x_0


for order in text:
    n = 0

    while n < order[1]:

        if order[0] == 'L':
            if move_tail(rowT, colT, rowH, colH-1) == True:
                colT = colH
                rowT = rowH
            colH -=  1
            n_positions = tacking(rowT, colT, n_positions)

        elif order[0] == 'R':
            if move_tail(rowT, colT, rowH, colH+1) == True:
                colT = colH
                rowT = rowH
            colH += 1
            n_positions = tacking(rowT, colT, n_positions)
        
        elif order[0] == 'U':
            if move_tail(rowT, colT, rowH-1, colH) == True:
                colT = colH
                rowT = rowH
            rowH -= 1
            n_positions = tacking(rowT, colT, n_positions)
        
        elif order[0] == 'D':
            if move_tail(rowT, colT, rowH+1, colH) == True:
                colT = colH
                rowT = rowH
            rowH += 1
            n_positions = tacking(rowT, colT, n_positions)
        n += 1

print('Result 1:', n_positions)

## Part 2
trail_track = [['0' for i in range(x_len)] for u in range(y_len)]
n_positions = 0
rope = [[y_0, x_0] for num in range(10)]
row, col = y_0, x_0

for order in text:
    n = 0
    
    while n < order[1]:
        
        for knot in range(len(rope)):

            rowK = rope[knot][0]    # knot row 
            colK = rope[knot][1]    # knot column

            if order[0] == 'L':
            
                if knot == 0:   # Head
                    rope[knot][1] -= 1
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif rowK != row and colK != col and move_tail(rowK, colK, row, col) == True:
                    rope[knot][0], rope[knot][1] = row, colK -1
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif rowK == row and move_tail(rowK, colK, row, col) == True:
                    rope[knot][1] = colK -1
                    col = rope[knot][1]
                    
                if knot == 9:
                    n_positions = tacking(row, col, n_positions)
            
            if order[0] == 'R':
            
                if knot == 0:   # Head
                    rope[knot][1] += 1
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif rowK != row and colK != col and move_tail(rowK, colK, row, col) == True:
                    rope[knot][0], rope[knot][1] = row, colK +1
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif rowK == row and move_tail(rowK, colK, row, col) == True:
                    rope[knot][1] = colK +1
                    col = rope[knot][1]
                    
                if knot == 9:
                    n_positions = tacking(row, col, n_positions)

            if order[0] == 'D':
            
                if knot == 0:   # Head
                    rope[knot][0] += 1
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif rowK != row and colK != col and move_tail(rowK, colK, row, col) == True:
                    rope[knot][0], rope[knot][1] = rowK +1 , col
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif colK == col and move_tail(rowK, colK, row, col) == True:
                    rope[knot][0] = rowK +1
                    row = rope[knot][0]
                    
                if knot == 9:
                    n_positions = tacking(row, col, n_positions)

            if order[0] == 'U':
            
                if knot == 0:   # Head
                    rope[knot][0] -= 1
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif rowK != row and colK != col and move_tail(rowK, colK, row, col) == True:
                    rope[knot][0], rope[knot][1] = rowK -1 , col
                    row = rope[knot][0]
                    col = rope[knot][1]

                elif colK == col and move_tail(rowK, colK, row, col) == True:
                    rope[knot][0] = rowK -1
                    row = rope[knot][0]
                    
                if knot == 9:
                    n_positions = tacking(row, col, n_positions)
            n += 1

print('Result 2:', n_positions)


#If the head is ever two steps directly up, down, left, or right from the tail, 
#the tail must also move one step in that direction so it remains close enough

#Otherwise, if the head and tail aren't touching and aren't in the same row or column, 
#the tail always moves one step diagonally to keep up: