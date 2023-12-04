import re
with open("input.txt") as f:
    cards = f.read().splitlines()
#PART 1
total = 0
#PART 2
for card in range(len(cards)):
    raw = re.findall("[0-9]+|\|", cards[card])
    pipe = raw.index("|")
    breakpoint()
    wins = sum(i in raw[pipe+1:] for i in raw[1:pipe])
    #PART 1
    total += int(2 ** (wins - 1))

print(total)
