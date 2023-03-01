
f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/year 2022/day7_input.txt", "r")
text = f.read()
text = text.split('\n')
text.remove('$ ls')

# Import
import re

dct = {}
dire = ''

for line in text:
    
    spt_line = line.split()

    if line.startswith("$ cd"):

        if spt_line[2] == '..':
            dire = dire[:dire.rindex('/')]

        elif line[5:] == '/':
            dire = 'root'
        else:
            dire += '/' + line[5:]
            dct.setdefault(dire, 0)

    elif spt_line[0].isnumeric():
        
        dct[dire] = dct.get(dire, 0) + int(spt_line[0])

# Agregarles a las carpetas el peso de las carpetas que contienen en su interior

# Creamos un nuevo diccionario ordenado, desde las cadenas más larga (con más /), hasta la más corta
new_dct = dict(sorted(dct.items(), key=lambda item: item[0].count('/')))
new_dct = dict(reversed(list(new_dct.items())))

# A las carpetas anteriores se les sumó todos los tamaños de los archivos que contienen
# pero no el tamaño de las carpetas que contienen. Tengo que sumar todas las carpetas en escalera

# Este loop empieza sumando los pesos de las carpetas más largas (más /) y va bajando por /

for k in new_dct:
    if k != 'root':
        k2 = 0
        k2 = re.findall('.*/', k)
        k2 = k2[0][0:-1]

        new_dct[k2] = new_dct.get(k2) + new_dct.get(k)

# Cantidad y Tamaño total de las carpetas de más de 100000
# Esta parte está mal 
# ej root/a/b/c  >> root/a/b + c >> root/a + b >> root + a

total_size = 0
count = 0

for key in new_dct:
    if new_dct[key] <= 100000:
        count += 1
        total_size += new_dct[key]

print('Carpetas con tamaño de más de 100000:', count)
print('Suma de Tamaño total de las carpetas de más de 100000:', total_size)

## Part 2
# Total disc space available : 70000000
# Need unuse space of 30000000
# Find a directory you can delete that will free up enough space to run the update
print('\n## Parte 2 ##\n')

total_size_root = new_dct.get('root')
print('Tamaño total de los archivos:', total_size_root)

size_avail = 70000000 - total_size_root
print('Espacio disponible:', size_avail)

# 70000000 - 30000000 = 40000000

if total_size_root > 40000000:
    to_delete = total_size_root - 40000000
    print('Hay que borrar carpetas para liberar:', to_delete)

elif total_size_root < 40000000:
    print('Hay suficiente espacio, no se necesita borrar nada')

size_del = []

for k in new_dct:
    if new_dct[k] >= to_delete:
        size_del.append(new_dct[k])
print('Se va a eliminar', min(size_del))