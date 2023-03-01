
f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/day6_input.txt", "r")
text = f.read()

n = 0

while True:
    x1, x2 ,x3 ,x4 = text[n], text[1+n], text[2+n], text[3+n]
    if x1!=x2 and x2!=x3 and x3!=x4 and x1!=x4 and x2!=x4 and x1!=x3:
        print(x1, x2, x3, x4)
        num = n + 4
        break
    n += 1

print('La solución es:', num)

# Part 2
n = 0
num2 = 0
count = 0

while True:
    count = 0
    for x in range(14):
        for y in range(14):
            if text[n+x] == text[n+y]:
                count += 1
    if count == 14:
        num2 = n + 14
        break
    n += 1

print('La solución de la parte 2 es:', num2)