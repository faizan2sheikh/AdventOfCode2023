digits = {'0','1','2','3','4','5','6','7','8','9'}
def find_digit(line):
    for c in line:
        if c in digits:
            return c

nums = []

with open('test.txt','r') as f:
    lst = f.readlines()
    for line in lst:
        nums.append(int(find_digit(line)+find_digit(line[::-1])))

print(sum(nums))