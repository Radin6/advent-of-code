# First column(oponent)     Second column(you)
# A Rock                    X Rock
# B Paper                   Y Paper
# C Scissors                Z Scissor

# Total score = points of shape you selected + Points of the round 
# points of shape you selected (points_shape) : 1 Rock, 2 Paper, 3 Scissors
# Points of the round (points_round) : 0 if you lost, 3 if draw, 6 you if won

f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/day2_input.txt", "r")
texto = f.read()

texto = texto.split('\n')

total_score = 0
points_shape = 0
points_round = 0

for line in texto:
    if line[0] == 'A' and line[2] == 'X':
        points_shape += 1
        points_round += 3
    elif line[0] == 'A' and line[2] == 'Y':
        points_shape += 2
        points_round += 6
    elif line[0] == 'A' and line[2] == 'Z':
        points_shape += 3
        points_round += 0
    elif line[0] == 'B' and line[2] == 'X':
        points_shape += 1
        points_round += 0
    elif line[0] == 'B' and line[2] == 'Y':
        points_shape += 2
        points_round += 3
    elif line[0] == 'B' and line[2] == 'Z':
        points_shape += 3
        points_round += 6
    elif line[0] == 'C' and line[2] == 'X':
        points_shape += 1
        points_round += 6
    elif line[0] == 'C' and line[2] == 'Y':
        points_shape += 2
        points_round += 0
    elif line[0] == 'C' and line[2] == 'Z':
        points_shape += 3
        points_round += 3

total_score = points_shape + points_round

print('My Total points are:', total_score)

# Part 2

# First column(oponent)     Second column(you)  points of shape you selected
# A Rock                    X Lose              Rock        1
# B Paper                   Y Draw              Paper       2
# C Scissors                Z Win               Scissors    3

total_score2 = 0
points_shape2 = 0
points_round2 = 0

for line in texto:
    if line[0] == 'A' and line[2] == 'X':   # Rock-Lose = Scissors (3)
        points_shape2 += 3
        points_round2 += 0
    elif line[0] == 'A' and line[2] == 'Y': # Rock-Draw = Rock (1)
        points_shape2 += 1
        points_round2 += 3
    elif line[0] == 'A' and line[2] == 'Z': # Rock-Win = Paper (2)
        points_shape2 += 2
        points_round2 += 6
    elif line[0] == 'B' and line[2] == 'X': # Paper-Lose = Rock (1)
        points_shape2 += 1
        points_round2 += 0
    elif line[0] == 'B' and line[2] == 'Y': # Paper-Draw = Paper (2)
        points_shape2 += 2
        points_round2 += 3
    elif line[0] == 'B' and line[2] == 'Z': # Paper-Win = Scissors (3)
        points_shape2 += 3
        points_round2 += 6
    elif line[0] == 'C' and line[2] == 'X': # Scissors-Lose = Paper (2)
        points_shape2 += 2
        points_round2 += 0
    elif line[0] == 'C' and line[2] == 'Y': # Scissors-Draw = Scissors (3)
        points_shape2 += 3
        points_round2 += 3
    elif line[0] == 'C' and line[2] == 'Z': # Scissors-Win = Rock (1)
        points_shape2 += 1
        points_round2 += 6

total_score2 = points_shape2 + points_round2

print('My Total points are:', total_score2)