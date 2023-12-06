import math

'''
m = time spent moving
c =   "    "   charging
l = time limit

m = l - c

distance = speed * time spent moving
d = s * m

s = c

Substitute m and s

d = c * (l - c)
d = -c^2 + cl
c^2 - cl + d = 0

Solve quadratic formula like this:
c = l + sqrt(l^2 - 4d) / 2
c = l - sqrt(l^2 - 4d) / 2

'''

limits = [44806572]
records = [208158110501102]
ways = []

l = limits[0]
d = records[0]

c1 = (l + math.sqrt(math.pow(l, 2) - 4 * d)) / 2
c2 = (l - math.sqrt(math.pow(l, 2) - 4 * d)) / 2

print(f'{math.ceil(max(c1, c2)) - math.ceil(min(c1,c2))}')