#Puzzle adalah Binary Puzzle 1 dimensi yang hanya mengikuti (0,2)-constraint.
#Blank Cell dinotasikan dengan '_'

puzzle = '_00_10_0_11__00_'
#puzzle = '___00_010__10__'
#puzzle = '100___0011'
a = list(puzzle)
change = True

while change:
    change = False
    for i in range(1,len(a)-2):
        #pair constraint
        if a[i] == a[i+1] and a[i-1]  == '_':
            if a[i] == '0':
                a[i-1] = a[i+2] = '1'
                change =True
            elif a[i] == '1':
                a[i-1] = a[i+2] = '0'
                change =True
        if a[i] == a[i+1] and a[i+2]  == '_':
            if a[i] == '0':
                a[i-1] = a[i+2] = '1'
                change =True
            elif a[i] == '1':
                a[i-1] = a[i+2] = '0'
                change =True

        #trio constraint
        if a[i] == a[i+2] and a[i+1] == '_':
            if a[i] == '0':
                a[i+1] = '1'
                change =True
            elif a[i] == '1':
                a[i+1] = '0'
                change =True

puzzle, ''.join(a)
