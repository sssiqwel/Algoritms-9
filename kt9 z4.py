sizes = [1, 3, 2, 4]
n = len(sizes)

if n == 1:
    print(0)
else:
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + sizes[i]

    cost = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            total = prefix[right + 1] - prefix[left]
            best = 10 ** 30
            for mid in range(left, right):
                candidate = cost[left][mid] + cost[mid + 1][right] + total
                if candidate < best:
                    best = candidate
            cost[left][right] = best
    print(cost[0][n - 1])
