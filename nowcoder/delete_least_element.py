# 问题描述

# 给定有 n 个数的 A 序列：A1,A2,A3…An 。对于这个序列，我们想得到一个子序列 Ap1,Ap2⋯Api⋯Apm(1≤p1< p2<⋯pi<⋯< pm≤n)，
# 满足 Ap1≥Ap2≥⋯≥Api≤⋯≤Apm 。从 A 序列最少删除多少元素，可以得到我们想要的子序列。

# 输入格式
# 第一行输入一个整数 n，代表 A 序列中数字的个数。第二个输入 n 个整数，代表A1,A2 ,A3 …An。(1≤n≤1000，1≤Ai≤10000)

# 输出格式
# 输出需要删除的元素个数，占一行。

# 样例输入
# 7
# 3 2 4 1 2 5 3

# 样例输出
# 2

# 首先从前往后找出每一个位上的最长非递增子序列，然后从后往前找出每一位上的最长非递增子序列，最后把前后位上的结果相加-1，
# 因为要找出删除最少的元素数，所以n-res即可，这个题还有个点是不一定非得找先减后增的序列，也可以是单减或者单增序列


def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    res = 0

    dp1 = [1 for _ in range(n)]
    dp2 = [1 for _ in range(n)]
    for i in range(n):
        dp1[i] = 1
        for j in range(i):
            if A[j] >= A[i]:
                dp1[i] = max(dp1[j] + 1, dp1[i])

    for i in range(n - 1, -1, -1):
        dp2[i] = 1
        for j in range(n - 1, i, -1):
            if A[i] <= A[j]:
                dp2[i] = max(dp2[j] + 1, dp2[i])

    for i in range(n):
        res = max(dp1[i] + dp2[i] - 1, res)

    return n - res


if __name__ == '__main__':
    result = main()
    print(result)
