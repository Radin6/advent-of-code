# Import
import re

f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/day4_input.txt", "r")
text = f.read()
text = text.split('\n')

text_re = []
count = 0
count_2 = 0 # Para la parte 2

for line in text:
    line_re = re.split('-|,', line)
    text_re.append(line_re)
    
    a,b,c,d = int(line_re[0]),int(line_re[1]),int(line_re[2]),int(line_re[3])

    if (a >= c and b <= d) or (a <= c and b >= d): # Condición para que un elfo contenga dentro el total de casilleros del otro
        count += 1
    
    if (a<= c <=b) or (a<= d <=b)or (c<= a <=d) or (c<= b <=d): # Para la parte 2
        count_2 += 1

print('La cantidad de tareas que contienen totalmente a otras es:', count)

print('La cantidad total de coincidencias son:', count_2)    # Parte 2



