n = int(input())

memo = [0 for _ in range(n + 1)]

memo[0] = 1
memo[1] = 1

for i in range(2, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]
    memo[i] %= 15746
print(memo[n])