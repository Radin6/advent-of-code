f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/year 2022/day10_input.txt", "r")
text = f.read()
text = text.splitlines()

# noop >>> 0 | addx >>> number
text = [0 if line == 'noop' else int(line[5:]) for line in text]

# 1 - Determine signal strenght on each cycle (x_cycle)

x_cycle = [1, 1]   # Each element is total X on the cycle
z = 0

for line in text:

    if line != 0:    # addxs
        z = line + x_cycle[-1]
        x_cycle.append(z)
        x_cycle.append(z)

    elif line == 0: # noop
        x_cycle.append(x_cycle[-1])

# 2 - Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles and total sum of them
x_total_sig = 0

for cycle in range(19,220, 40):
    x_total_sig += x_cycle[cycle]*(cycle+1)

print('Result 1:', x_total_sig)

## Part 2

sprite = [0, 0, 0]
num = 0

for n in range(6):
    for position in range(40):
        
        sprite = [x_cycle[position+num] - 1, x_cycle[position+num], x_cycle[position+num] + 1]

        if position in sprite:
            print('#',end = '')

        else:
            print('.',end = '')
    print()
    num += 40