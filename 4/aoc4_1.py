import math
import re

def get_numbers(card: list[str], side: int) -> list[int]:
    '''
    side = 0 means left side (winners)
    side = 1 means right side (my numbers)
    '''
    return [
        int(match.group(0))
        for match in re.finditer(r'\d+', card.split('|')[side])
    ]

score = 0
lines = open('input.txt', 'r').readlines()

for line in lines:
    card = line.split(':')[1]

    winners = get_numbers(card, 0)
    my_numbers = get_numbers(card, 1)

    matches = set(winners) & set(my_numbers)
    score += 0 if len(matches) == 0 else math.pow(2, len(matches) - 1)

print(score)