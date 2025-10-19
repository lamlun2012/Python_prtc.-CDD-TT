with open ("MINSEG.INP", "r") as fi
    n = int(fi.readline().strip())
    a = list(map(int, fi.readline().strip().split()))
t = None
for i in range(n-1):
    if a[i+1] < a[i]:
        t = -1
    else:
        diff = a[i+1] - a[i]
        if diff > 0:
            if t is None or diff < t:
                t = diff
if t is None:
    t = 0

with open ("MINSEG.OUT", "w") as fo:
    fo.write(str(t))
