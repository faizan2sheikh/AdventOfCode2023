# Q1

worth = 0
with open('test.txt','r') as file:
    lst = file.readlines()
    for card in lst:
        c_id, numbers = card.split(':')
        c_id = int(c_id[5:])
        winning, have = numbers.strip().split(' | ')
        winning, have = set(winning.split(' ')), set(have.split(' '))
        if '' in winning:
            winning.remove('')
        if '' in have:
            have.remove('')    
        common = len(winning.intersection(have))
        if common > 0:
            worth+=2**(common-1)

print(worth)
#Q2

from collections import defaultdict
win_cards = defaultdict(int)

with open('test.txt','r') as file:
    lst = file.readlines()
    for card in lst:
        c_id, numbers = card.split(':')
        c_id = int(c_id[5:])
        winning, have = numbers.strip().split(' | ')
        winning, have = set(winning.split(' ')), set(have.split(' '))
        if '' in winning:
            winning.remove('')
        if '' in have:
            have.remove('')    
        common = len(winning.intersection(have))
        win_cards[c_id]+=1
        for t in range(win_cards[c_id]):
            for win_card in range(c_id+1, c_id+common+1):
                win_cards[win_card]+=1

print(sum(win_cards.values()))

