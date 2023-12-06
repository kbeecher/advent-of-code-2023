import functools
import operator

'''
m = time spent moving
c =   "    "   charging
l = time limit

distance = speed * time spent moving
d = s * m

m = l - c

c = l - m

s = c

Therefore by substitution:
d = (l - m) * m

'''

def get_distance(charge_time: int, limit: int) -> int:
    movement_time = limit - charge_time
    return (limit - movement_time) * movement_time

limits = [44, 80, 65, 72]
records = [208, 1581, 1050, 1102]
ways = []

for round in range(0, len(limits)):
    distances = [
        # Don't need to test first or last possibilities since 
        # they're always 0
        get_distance(poss, limits[round]) for poss in range(1, limits[round])
    ]
    wins = filter(lambda d: d > records[round], distances)
    ways.append(len(list(wins)))

print(functools.reduce(operator.mul, ways, 1))
