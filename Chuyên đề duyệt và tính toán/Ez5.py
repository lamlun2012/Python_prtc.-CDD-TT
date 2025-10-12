n = int(open("SEQUENCE.INP").readline())
a = []
for line in open("SEQUENCE.INP").read().splitlines()[1:]:
    x, y = map(int, line.split())
    a.insert(x-1, y)   # chèn y vào trước vị trí x
open("SEQUENCE.OUT","w").write(" ".join(map(str, a)))
