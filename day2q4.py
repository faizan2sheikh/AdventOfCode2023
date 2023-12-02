import numpy as np

power_sum = 0

with open('test.txt','r') as file:
    
    lst = file.readlines()

    for game in lst:
        power_set = {'green':1,'red':1,'blue':1}
        g_id, reveals = game.split(':')
        reveals = reveals.strip()
        sets = list(map(str.strip,reveals.split(';')))
        for s in sets:
            s = list(map(str.strip,s.split(',')))
            for c in s:
                c = c.split()
                power_set[c[1]]=max(int(c[0]),power_set[c[1]])
        game_power = np.prod(list(power_set.values()))
        power_sum+=game_power
print(power_sum)