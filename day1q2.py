digits = {'0','1','2','3','4','5','6','7','8','9'}
chars = {'1':'1','2':'2','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
def find_digit(line):
    for c in line:
        if c in digits:
            return c

nums = []

with open('test.txt','r') as f:
    lst = f.readlines()
    # lst = ['two1nine','8eightwo','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen' ]
    for line in lst:
        ind = []
        for c in chars:
            if c in line:
                index_val_s = line.find(c)
                if index_val_s!=-1:
                    ind.append([index_val_s,c])
                index_val_e = line.rfind(c)
                if index_val_e!=-1:
                    ind.append([index_val_e,c])
        ind = sorted(ind, key=lambda x: x[0])
        if ind:
            first = ind[0]
            last = ind[-1]
            line = line.replace(first[1], chars[first[1]])
            line = line.replace(last[1], chars[last[1]])
        # print(line)
        nums.append(int(find_digit(line)+find_digit(line[::-1])))

# print(nums)
print(sum(nums))