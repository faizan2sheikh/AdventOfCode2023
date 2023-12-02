limit = {'red':12, 'green':13, 'blue':14}

wins = 0

with open('test.txt','r') as file:
    lst = file.readlines()

    # lst = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 1 blue; 2 green']

    for game in lst:
        flag = True
        g_id, reveals = game.split(':')
        g_id = int(g_id[5:])
        reveals = reveals.strip()
        sets = list(map(str.strip,reveals.split(';')))
        for s in sets:
            if flag == True:
                s = list(map(str.strip,s.split(',')))
                for c in s:
                    c = c.split()
                    if int(c[0])>limit[c[1]]:
                        flag = False
            else:
                break
        if flag==True:
            wins+=g_id

print(wins)