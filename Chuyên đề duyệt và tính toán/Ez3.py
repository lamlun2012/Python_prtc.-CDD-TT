with open("RECT.INP","r") as f:
    n = int(f.readline().strip())
    rects = tuple(map(int, f.readline().strip().split())) for _ in range(n)
from math import gcd

ratios = {}
for a, b in rects:
    g = gcd(a, b)
    ra, rb = (a // g, b // g)
    ratios[(ra, rb)] = ratios.get((ra, rb), 0) + 1
    if ra > rb:
        ra, rb = rb, ra
    ratios[(ra, rb)] = ratios.get((ra, rb), 0) + 1
    
num_groups = len(ratios)
max_group_size = max(ratios.values())
with open("RECT.OUT","w") as f:
    f.write(f"{num_groups} {max_group_size}")
