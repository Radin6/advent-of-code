f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/year 2022/day11_input.txt", "r")
text = f.read()
text = text.split('\n')
text =  [elem.lstrip() for elem in text if elem != '']

import math
import copy

# 1 - Items per monkey
# items[monkey][item_monkey] = [[monkey1_items], [monkey2_items],...] | monkey1_items = [item1, item2,...]
# Extract items as integer as list of lists

items_mky = [item_list.lstrip('Starting items:').split(',') for item_list in text if item_list.startswith('Starting items:')]
items_mky = [[int(item) for item in item_list] for item_list in items_mky]
items_mky2 = copy.deepcopy(items_mky) # Only to use in part 2

# 2 - Operation per monkey
# oper_mky[monkey] = [[oper1], [oper2], ...]

oper_mky = [oper_list[17:] for oper_list in text if oper_list.startswith('Operation:')]

# 3 - Test per monkey
# test_mky[monkey] = [[divisible by this?, if true threw to this monkey, if false threw to this monkey]]

test_mky = [test_list.split()[::-1][0] for test_list in text if test_list.startswith('Test:')]
test_mky = [[int(test_mky[n]), int(text[n*6+4][-1]), int(text[n*6+5][-1])] for n in range(len(test_mky))]

print('test:', test_mky)
# Function test


# 4 - Do 20 cycles
n = 0
monkey_bs = 0
items_counter_mky = [int(0) for n in range(len(items_mky))]

while n < 20:
    
    for mky in range(len(items_mky)):

        while True:
            if items_mky[mky] != []:
                old = items_mky[mky][0]
                items_mky[mky].pop(0)
                items_counter_mky[mky] += 1

                new = eval(oper_mky[mky])
                new = math.floor(new/3)

                if new % test_mky[mky][0] == 0:
                    items_mky[test_mky[mky][1]].append(new)
                else:
                    items_mky[test_mky[mky][2]].append(new)

            else:
                break
    n += 1

print(items_counter_mky)

items_counter_mky.sort()

monkey_bs = items_counter_mky[-1] * items_counter_mky[-2]

print('Result 1:', monkey_bs)

## Part 2
items_counter_mky = [int(0) for n in range(len(items_mky))]

# Supermodulo
supermod = 1

for l in test_mky:
        supermod *= l[0]

print('sm:', supermod)

# Find monkey business level
n = 0
while n < 10000:
    
    for mky in range(len(items_mky2)):

        while True:
            if items_mky2[mky] != []:
                old = items_mky2[mky][0]
                items_mky2[mky].pop(0)
                items_counter_mky[mky] += 1

                new = eval(oper_mky[mky])
                new = new % supermod

                if new % test_mky[mky][0] == 0:
                    items_mky2[test_mky[mky][1]].append(new)
                else:
                    items_mky2[test_mky[mky][2]].append(new)
            else:
                break
    n += 1

print(items_counter_mky)

items_counter_mky.sort()

monkey_bs = items_counter_mky[-1] * items_counter_mky[-2]

print('Result 2:', monkey_bs)

'''Solution: I have no idea why this works. 
I don't know math that well, but what I did is multiply all of the testing numbers together, 
calling it "supermodulo", and every time a monkey inspects an item, 
set the item's value to the item mod the supermodulo, like item = item % supermodulo.
'''