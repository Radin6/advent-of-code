import re
import string
import copy

f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/day5_input.txt", "r")
text = f.read()
text = text.split('\n')
moves = []

# Moves
for line in text:
    if line.startswith('move'):
        line = line.replace('move ','').replace('from ','').replace('to ','')
        line = line.split()
        line = [int(line[0]) , int(line[1]), int(line[2])]
        moves.append(line)

#print(moves)

# Stack 1-9 , cada fila es un Stack

stacks = []
stacks2 = []

for line in text:
    if line.startswith('['):
        stacks.append(line)

for n in range(9):
    s = []
    for line in stacks[::-1]:
        if line[1+4*n] in string.ascii_uppercase:
            s.append(line[1+4*n])
    stacks2.append(s)

stacks3 = copy.deepcopy(stacks2)

# Voy a utilizar .pop() y .append()

cantidad_num = 0

for move_num in range(len(moves)):      # move = [cantidad, desde, hacia] - move[0] = cantidad | move[1] = desde | move[2] = hacia
    cantidad_num = 0
    cantidad = moves[move_num][0]
    desde = moves[move_num][1] - 1
    hacia = moves[move_num][2] - 1
    
    while cantidad != cantidad_num:
        
        stacks2[hacia].append(stacks2[desde][-1])
        stacks2[desde].pop()
        cantidad_num += 1

# Result 1

result = ''

for n in stacks2:
    result += n[-1]

print('1.Las cajas quedan:',result)

## Part 2
print(stacks3)

for move_num in range(len(moves)):      # move = [cantidad, desde, hacia] - move[0] = cantidad | move[1] = desde | move[2] = hacia
    cantidad = moves[move_num][0]
    desde = moves[move_num][1] - 1
    hacia = moves[move_num][2] - 1
    
    stacks3[hacia].extend(stacks3[desde][-cantidad:])
    stacks3[desde] = stacks3[desde][:len(stacks3[desde])-cantidad]
    #stacks3[desde].pop()

# Result 2

result2 = ''

for n in stacks3:
    result2 += n[-1]

print('2.Las cajas quedan:',result2)
