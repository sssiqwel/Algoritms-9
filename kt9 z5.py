table = [
    [1, -5, 3],
    [-2, 4, -1],
]
k = 1
n = len(table)
m = len(table[0])
NEG = -10 ** 30

best = [[[NEG] * (k + 1) for _ in range(m)] for _ in range(n)]
start = table[0][0]
best[0][0][0] = start
if k > 0 and start < 0:
    best[0][0][1] = 0

for i in range(n):
    for j in range(m):
        for used in range(k + 1):
            current = best[i][j][used]
            if current <= NEG // 2:
                continue
            for ni, nj in ((i + 1, j), (i, j + 1)):
                if ni >= n or nj >= m:
                    continue
                value = table[ni][nj]
                candidate = current + value
                if candidate > best[ni][nj][used]:
                    best[ni][nj][used] = candidate
                if value < 0 and used + 1 <= k and current > best[ni][nj][used + 1]:
                    best[ni][nj][used + 1] = current

print(max(best[n - 1][m - 1]))
