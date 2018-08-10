# LeeCode链接：https://leetcode.com/problems/coin-change-2/description/
#
# 你有不同面额的硬币和总金额。编写一个函数来计算构成该总金额的组合数。你可以假设你有有无限数量的每种硬币。
#
# Note: 可以有如下假设
#
# 0 <= amount <= 5000
#
# 1 <= coin <= 5000
#
# 硬币的面值少于 500
#
# 答案肯定可以被存储在32位整型变量int中

# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5 = 5
# 5 = 2 + 2 + 1
# 5 = 2 + 1 + 1 + 1
# 5 = 1 + 1 + 1 + 1 + 1

# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1


def main():
    amount = int(input())
    coins = list(map(int, input().split()))
    # dp[x]表示总金额为x时硬币的组合数
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    # 注意：不可以将里外层循环互换，否则就出现重复计算，
    # 比如：如果有硬币{1, 2}，且aoumut = 3，那么使用2, 1 和1, 2
    # 应该算为一种情况
    # 使用前i种硬币凑成指定面值
    for i in range(len(coins)):
        # 目标面值，从1到amount
        for j in range(1, amount + 1):
        # for j in range(coins[i], amount + 1):
            if j >= coins[i]:
                dp[j] += dp[j - coins[i]]

    return dp[amount]


print(main())
