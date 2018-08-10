# https://lintcode.com/problem/k-sum/description

# Description
# Given n distinct positive integers, integer k (k <= n) and a number target.
#
# Find k numbers where sum is target. Calculate how many solutions there are?

# Example
# Given [1,2,3,4], k = 2, target = 5.
#
# There are 2 solutions: [1,4] and [2,3].
#
# Return 2.

# state:
#     f[i][j][t]前 i 个数中取 j 个数出来组成和为 t 的组合数目
# function:
#     f[i][j][t] = f[i - 1][j][t] + f[i - 1][j - 1][t - a[i - 1]] (不包括第i 个数的时候组成t的情况 + 包括第i个数的时候组成t的情况)
# initialize:
#     f[i][0][0] = 1
# result:
#     f[n][k][target]
#
# 时间复杂度：O(n * k * target)


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    target = int(input())

    dp = [[[0 for k in range(target + 1)] for j in range(k + 1)] for i in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        dp[i][0][0] = 1

    for i in range(1, len(arr) + 1):
        for j in range(1, k + 1):
            for l in range(target + 1):
                dp[i][j][l] = dp[i - 1][j][l]
                if l >= arr[i - 1]:
                    dp[i][j][l] += dp[i - 1][j - 1][l - arr[i - 1]]

    return dp[len(arr)][k][target]


print(main())
