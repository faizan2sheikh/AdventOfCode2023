# from collections import defaultdict

# sudo_activation = defaultdict(list)

# schematic = []

# with open('test.txt','r') as f:
#     lst = f.readlines()
    
#     vertical_pad = ['.']*(len(lst[0])+2)

#     matrix = []

#     matrix.append(vertical_pad)

#     for l in lst:
#         matrix.append(['.']+[c for c in l.strip()]+['.'])

#     matrix.append(vertical_pad)

#     mask_matrix = [['.']*len(i) for i in matrix]

#     for i in range(1, len(matrix)-1):
#         for j in range(1, len(matrix[i])-1):
#             if ((matrix[i-1][j] == '*') or (matrix[i+1][j] == '*') or (matrix[i][j-1] == '*')  or (matrix[i][j+1] == '*')  or (matrix[i-1][j-1] == '*')  or (matrix[i-1][j+1] == '*')  or (matrix[i+1][j-1] == '*')   or (matrix[i+1][j+1] == '*')) and str(matrix[i][j]).isdigit():
#                 sudo_activation[(i,j)].append()
#                 mask_matrix[i][j]='*'

#     def back_track_left(i,j):
#         if not str(matrix[i][j]).isdigit():
#             return
#         else:
#             mask_matrix[i][j]='*'
#             back_track_left(i,j-1)
    
#     def back_track_right(i,j):
#         if not str(matrix[i][j]).isdigit():
#             return
#         else:
#             mask_matrix[i][j]='*'
#             back_track_right(i,j+1)

#     for i in range(1, len(matrix)-1):
#         for j in range(1, len(matrix[i])-1):
#             if mask_matrix[i][j]=='*':
#                 back_track_left(i,j)
#                 back_track_right(i,j)

#     cur = ''
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if mask_matrix[i][j]=='*':
#                 cur+=matrix[i][j]
#             else:
#                 if cur!='':
#                     schematic.append(int(cur))
#                 cur=''

# print(schematic)
# print(sum(schematic))

import re

def parseEngineSchematic(schematic):
    width = len(schematic[0])+1
    numbers = {matchObj.span():matchObj.group(0) for matchObj in re.finditer(r'\d+','.'.join(schematic)+'.')}
    symbols = {matchObj.span():matchObj.group(0) for matchObj in re.finditer(r'[^\.\d]','.'.join(schematic)+'.')}
    return width,numbers,symbols
    
def solutionB(input):
    width,numbers,symbols = parseEngineSchematic(input)
    gearratios = list()
    for symbol in symbols:
        if symbols[symbol] == '*':
            positions = [symbol[1],symbol[0]-width,symbol[0]+width,symbol[1]+width,symbol[1]-width,symbol[0]-1,symbol[0]-width-1,symbol[0]+width-1]
            nums = {int(numbers[num]) for num in numbers for pos in positions if num[0] <= pos < num[1]}
            if(len(nums) == 2):
                gearratios.append(nums.pop()*nums.pop())
    print(sum(gearratios))
    
def solutionA(input):
    width,numbers,symbols = parseEngineSchematic(input)
    engineParts = [int(numbers[num]) for num in numbers for symbol in symbols if num[0]-width-1 <= symbol[0] <= num[1]-width or num[0]-1 <= symbol[0] <= num[1] or num[0]+width-1 <= symbol[0] <= num[1]+width]
    print(sum(engineParts))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput(r'test.txt')
    #input = ['467..114..','...*......','..35..633.','......#...','617*......','.....+.58.','..592.....','......755.','...$.*....','.664.598..']
    print(input)
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()