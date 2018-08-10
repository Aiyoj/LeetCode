# https://www.lintcode.com/problem/partition-equal-subset-sum/description
# 描述
# 给一 只含有正整数 的 非空 数组, 找到这个数组是否可以划分为 两个 元素和相等的子集。
# 所有数组元素不超过100.
# 数组大小不超过200.
# 样例
# 给一数组 [1, 5, 11, 5] , 返回 true ,
# 两个子集:[1, 5, 5], [11]
# 给一数组 [1, 2, 3, 9] , 返回 false


def main():
    arr = list(map(int, input().split()))
    su = sum(arr)
    if su % 2 == 1:
        return False
    su //= 2

    dp = [[False for _ in range(su+1)] for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = True

    for j in range(1, su + 1):
        if arr[0] == j:
            dp[0][j] = True
        else:
            dp[0][j] = False

        for i in range(len(arr)):
            if arr[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - arr[i]]

    return dp[len(arr) - 1][su]

print(main())
