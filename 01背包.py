

def main():
    N, M = int(input()), int(input())
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))

    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if weight[i] <= j:
                dp[i][j] = max(dp[i - 1][j - weight[i]] + value[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[N][M])



o = [0, 1, 1, 1]
v = o.pop()
print(o)


ss = '666666'
ss = list(ss)
ss[0], ss[1] = ss[1], ss[0]
print(''.join(ss))