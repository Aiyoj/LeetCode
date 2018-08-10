# LeeCode链接：https://leetcode.com/problems/coin-change/description/
#
# 你有不同面额的硬币和总金额。写一个函数来计算你所需要的最少的硬币数。如果这笔钱不能由硬币的任何组合构成，则返回-1。
#
# Example 1:
#
# coins = [1, 2, 5], amount = 11
#
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
#
# coins = [2], amount = 3
#
# return -1.
#
# Note:
# 你可以假设每种硬币都有无数个


def main():
    MAX = 1 << 30
    amount = int(input())
    coins = list(map(int, input().split()))
    # dp[x] 表示总面值为x所需的最少硬币数
    # 每一个元素都初始为MAX，如果最后无解则dp[amount] == MAX
    dp = [MAX for _ in range(amount + 1)]
    # 总金额为0时需要0个硬币
    dp[0] = 0

    # 注意：可以将里外层循坏互换，不影响结果
    # 求出总金额从1到amount所需的最少硬币数
    for i in range(1, amount + 1):
        # 本轮循环只使用第j种硬币，但是dp[]中保存的信息是使用前j - 1种硬币对应金额所需的最少硬币数
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    return -1 if dp[amount] == MAX else dp[amount]


print(main())
