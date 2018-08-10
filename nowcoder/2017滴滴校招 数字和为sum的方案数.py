# 给定一个有n个正整数的数组A和一个整数sum,求选择数组A中部分数字和为sum的方案数。
# 当两种选取方案有一个数字的下标不一样,我们就认为是不同的组成方案。

# 输入描述:  输入为两行: 第一行为两个正整数n(1 ≤ n ≤ 1000)，sum(1 ≤ sum ≤ 1000)，
# 第二行为n个正整数A[i](32位整数)，以空格隔开。

# 输出描述:  输出所求的方案数

# 输入例子:
# 5 15
# 5 5 10 2 3

# 输出例子:
# 4


def main1():
    N, Sum = list(map(int, input().split()))
    Arr = list(map(int, input().split()))
    dp = [[0 for j in range(Sum + 1)] for i in range(len(Arr) + 1)]
    for i in range(Sum + 1):
        dp[0][i] = 0
    dp[0][0] = 1

    for i in range(1, len(Arr) + 1):
        for j in range(Sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= Arr[i - 1]:
                dp[i][j] += dp[i - 1][j - Arr[i - 1]]

    return dp[len(Arr)][Sum]


def main2():
    N, Sum = list(map(int, input().split()))
    Arr = list(map(int, input().split()))
    dp = [0 for _ in range(Sum + 1)]
    dp[0] = 1
    for i in range(len(Arr)):
        for j in range(Sum, Arr[i] - 1, -1):
            dp[j] += dp[j - Arr[i]]

    return dp[Sum]


print(main1())
# print(main2())
