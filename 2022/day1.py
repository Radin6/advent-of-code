f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/day1_input.txt", "r")
texto = f.read()

texto = texto.split('\n')

elf_total_cal = 0
list_elf_cal = []

# Convertir números a Enteros y '' a 0
texto = [0 if line =='' else int(line) for line in texto]
#print(texto)

for line in texto:
    elf_total_cal += line
    if line == 0:
        list_elf_cal.append(elf_total_cal)
        elf_total_cal = 0

grande = max(list_elf_cal)
print('El elfo con más calorías tiene ',grande)

list_elf_cal.sort(reverse=True)

suma_3 = list_elf_cal[0] + list_elf_cal[1] + list_elf_cal[2]

print('La suma de las cal de los 3 elfo después del primero',suma_3)
