normal = {'0','1','2','3','4','5','6','7','8','9','.'}

sudo_activation = []

schematic = []

with open('test.txt','r') as f:
    lst = f.readlines()
    
    vertical_pad = ['.']*(len(lst[0])+2)

    matrix = []

    matrix.append(vertical_pad)

    for l in lst:
        matrix.append(['.']+[c for c in l.strip()]+['.'])

    matrix.append(vertical_pad)

    mask_matrix = [['.']*len(i) for i in matrix]

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            if ((matrix[i-1][j] not in normal) or (matrix[i+1][j] not in normal) or (matrix[i][j-1] not in normal)  or (matrix[i][j+1] not in normal)  or (matrix[i-1][j-1] not in normal)  or (matrix[i-1][j+1] not in normal)  or (matrix[i+1][j-1] not in normal)   or (matrix[i+1][j+1] not in normal)) and str(matrix[i][j]).isdigit():
                sudo_activation.append([i,j])
                mask_matrix[i][j]='*'

    def back_track_left(i,j):
        if not str(matrix[i][j]).isdigit():
            return
        else:
            mask_matrix[i][j]='*'
            back_track_left(i,j-1)
    
    def back_track_right(i,j):
        if not str(matrix[i][j]).isdigit():
            return
        else:
            mask_matrix[i][j]='*'
            back_track_right(i,j+1)

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            if mask_matrix[i][j]=='*':
                back_track_left(i,j)
                back_track_right(i,j)

    cur = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if mask_matrix[i][j]=='*':
                cur+=matrix[i][j]
            else:
                if cur!='':
                    schematic.append(int(cur))
                cur=''

print(schematic)
print(sum(schematic))
