m, p, n = map(int, input("m p n: ").split())
for i in range(1, n+1):
    print(i + 1, int(m))
    m = m * (1 + p/100)