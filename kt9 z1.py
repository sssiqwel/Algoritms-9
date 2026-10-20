s = "ababbbabbababa"
n = len(s)

palindrome = [[False] * n for _ in range(n)]
for i in range(n):
    palindrome[i][i] = True
for i in range(n - 1):
    palindrome[i][i + 1] = s[i] == s[i + 1]
for length in range(3, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        palindrome[left][right] = s[left] == s[right] and palindrome[left + 1][right - 1]

parts = [0] * n
for right in range(n):
    if palindrome[0][right]:
        parts[right] = 1
        continue
    best = right + 1
    for left in range(1, right + 1):
        if palindrome[left][right]:
            best = min(best, parts[left - 1] + 1)
    parts[right] = best

print(parts[-1])
