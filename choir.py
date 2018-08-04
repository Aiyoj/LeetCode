# 题目描述

# 有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，
# 要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

# 输入描述:
# 每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，表示学生的个数，接下来的一行，
# 包含 n 个整数，按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。
# 接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。

# 输出描述:
# 输出一行表示最大的乘积。

# 示例1

# 输入
# 3
# 7 4 7
# 2 50

# 输出
# 49


def main():
    N = int(input())
    ability = list(map(int, input().split()))
    K, D = list(map(int, input().split()))
    dp1 = [[0 for _ in range(N)] for _ in range(K)]
    dp2 = [[0 for _ in range(N)] for _ in range(K)]
    res = 0

    for i in range(N):
        dp1[0][i] = ability[i]
        dp2[0][i] = ability[i]

    for i in range(1, N):
        for k in range(1, K):
            for j in range(i - 1, max(0, i - D) - 1, -1):
                dp1[k][i] = max(dp1[k][i], max(dp1[k - 1][j] * ability[i], dp2[k - 1][j] * ability[i]))
                dp2[k][i] = min(dp2[k][i], min(dp1[k - 1][j] * ability[i], dp2[k - 1][j] * ability[i]))
        res = max(res, dp1[K - 1][i])

    return res


if __name__ == '__main__':
    result = main()
    print(result)
