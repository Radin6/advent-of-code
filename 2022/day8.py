f = open("/Users/Admin/Desktop/ConquerBlock/adventofcode/year 2022/day8_input.txt", "r")
text = f.read()
text = text.split('\n')
text = [[c for c in line] for line in text]

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it
# Determine whether or not is VISIBLE (True|False)

# Function to check it the given tree is visible
def visible(row_v, col_v):
    
    #tree = text[row_v][col_v]
    visible = False
    
    if row_v == 0 or row_v == len(text) or col_v == 0 or col_v == len(text):
        visible = True
        return visible
    
    else:
        side1_visible, side2_visible, side3_visible, side4_visible = True, True, True, True
        for x in range(len(text)):
            
            if col_v > x and text[row_v][x] >= text[row_v][col_v]:  # Left
                side1_visible = False

            if col_v < x and text[row_v][x] >= text[row_v][col_v]:  # Right
                side2_visible = False

            if text[x][col_v] >= text[row_v][col_v] and row_v < x:  # Downside
                side3_visible = False

            if text[x][col_v] >= text[row_v][col_v] and row_v > x:  # Upside
                side4_visible = False

        if side1_visible == True or side2_visible == True or side3_visible == True or side4_visible == True:
            #print('R:', row_v, 'C:', col_v,'s1:',side1_visible,'s2:',side2_visible,'s3:',side3_visible,'s4:',side4_visible)
            visible = True
            return visible
                
# End Function

## Funcion to get tree view score >>Part 2
def score(text_s, row_s, col_s):
    point1, point2, point3, point4 = 0, 0, 0, 0
    break1, break2, break3, break4 = False, False, False, False
    total_points = 0

    for x in range(1, len(text_s)-1):
        

            # Left
        if break1 == False and col_s - x >= 0:
            if text_s[row_s][col_s - x] < text_s[row_s][col_s]:
                point1 += 1
            elif text_s[row_s][col_s - x] >= text_s[row_s][col_s]:
                point1 += 1
                break1 = True

            # Right
        if break2 == False and col_s + x <= len(text_s)-1: 
            if text_s[row_s][col_s + x] < text_s[row_s][col_s]:
                point2 += 1
            elif text_s[row_s][col_s + x] >= text_s[row_s][col_s]:
                point2 += 1
                break2 = True
            
            # Downside
        if break3 == False and row_s + x <= len(text_s)-1:
            if text_s[row_s + x][col_s] < text_s[row_s][col_s]:
                point3 += 1
            elif text_s[row_s + x][col_s] >= text_s[row_s][col_s]:
                point3 += 1
                break3 = True
                
            # Upside
        if break4 == False and row_s + x >= 0:
            if text_s[row_s - x][col_s] < text_s[row_s][col_s]:
                point4 += 1
            elif text_s[row_s - x][col_s] >= text_s[row_s][col_s]:
                point4 += 1
                break4 = True
        if break1 == True and break2 == True and break3 == True and break4 == True:
            break

    total_points = point1 * point2 * point3 * point4
    return total_points
                
# End Function

count = 0
list_points = []

for row in range(len(text)):
    for col in range(len(text[0])):
        
        list_points.append(score(text, row, col))

        if visible(row , col) == True:
            count += 1


print('Part 1:', count)
print('Part 2:', max(list_points))