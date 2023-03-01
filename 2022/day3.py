# Import
import string

f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/day3_input.txt", "r")
text = f.read()
text = text.split('\n')

# Define priority list
prior_list = []

a = string.ascii_lowercase
A = string.ascii_uppercase

aA = a + A

for n in aA:
    prior_list.append([n, aA.index(n) + 1])

#string.ascii_uppercase

l2 = 0 
total_priority = 0

for line in text:
    romper = False
    l2 = int(len(line)/2)   # Mitad de len(line) en entero
    
    for x in line[0:l2]:
        for y in line[l2:]:
            if x == y:
                total_priority += prior_list[aA.index(x)][1]
                romper = True
                break
        if romper == True:
            break

print(total_priority)

# Part 2
total_priority2 = 0

for group in range(0,int(len(text)),3):
    romper = False

    for x in text[group]:
        for y in text[group+1]:
            for z in text[group+2]:
                if x == y and y == z:
                    total_priority2 += prior_list[aA.index(x)][1]
                    romper = True
                    break
            if romper == True:
                break
        if romper == True:
            break

print(total_priority2)
