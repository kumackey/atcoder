N = int(input())
Xs = list(map(int, input().split()))

min = 2 ** 100

for p in range(1, 100):
    cand = 0
    for xi in Xs:
        cand += (xi - p) ** 2
    if cand < min:
        min = cand

print(min)
