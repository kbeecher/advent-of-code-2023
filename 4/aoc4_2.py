import re

def get_numbers(card: list[str], side: int) -> list[int]:
    # side = 0 means left side (winners)
    # side = 1 means right side (my numbers)
    return [
        int(match.group(0))
        for match in re.finditer(r'\d+', card.split('|')[side])
    ]

def get_wins(winners: list[int], my_numbers: list[int]) -> int:
    return len(set(winners) & set(my_numbers))

def mark_extras(extras: list[int], idx: int, how_many: int, multiples: int) -> None:
    idx += 1
    for n in range(idx, idx + how_many):
        extras[n] += multiples


score = 0
lines = open('input.txt', 'r').readlines()

winners = []
my_numbers = []
num_cards = [1 for l in lines]

for n in range(0, len(lines)):
    card = lines[n].split(':')[1]
    winners.append(get_numbers(card, 0))
    my_numbers.append(get_numbers(card, 1))


for i in range(0, len(lines)):
    mark_extras(num_cards, i, get_wins(winners[i], my_numbers[i]), num_cards[i])

print(sum(num_cards))

