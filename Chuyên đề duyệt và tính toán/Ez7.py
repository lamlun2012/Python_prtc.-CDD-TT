with open("PROMAX.INP","r") as fi:
    n = int(fi.readline().strip())
    nums = list(map(int, fi.readline().strip().split()))
t1 = max(nums)
nums.remove(t1)
t2 = max(nums)
nums.remove(t2)
t3 = max(nums)
max_prod = t1 * t2 * t3
with open("PROMAX.OUT","w") as fo:
    fo.write(str(max_prod))
