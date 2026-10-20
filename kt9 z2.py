grid = [
    "...",
    "#..",
    "...",
]
MOD = 1_000_000_007
n = len(grid)
m = len(grid[0])

ways = [[0] * m for _ in range(n)]
if grid[0][0] != "#":
    ways[0][0] = 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            ways[i][j] = 0
            continue
        if i:
            ways[i][j] = (ways[i][j] + ways[i - 1][j]) % MOD
        if j:
            ways[i][j] = (ways[i][j] + ways[i][j - 1]) % MOD

print(ways[-1][-1])
