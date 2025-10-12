with open("LUYTHUA.INP", "r") as fi:
    n = int(fi.readline().strip())
    p = [int(fi.readline().strip()) for _ in range(n)]
total =0
for p_ in p:
    last_digit = p_ % 10
    other_digits = p_ // 10
    k = other_digits ** last_digit
    total += k
with open("LUYTHUA.OUT", "w") as fo:
    fo.write(str(total))