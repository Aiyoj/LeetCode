# https://www.lintcode.com/problem/backpack-vi/description

# 描述
# 给出一个都是正整数的数组 nums，其中没有重复的数。从中找出所有的和为 target 的组合个数。
# 一个数可以在组合中出现多次。
# 数的顺序不同则会被认为是不同的组合。

# 样例
# 给出 nums = [1, 2, 4], target = 4
# 可能的所有组合有：
#
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# [4]
# 返回 6


def main():
    target = int(input())
    nums = list(map(int, input().split()))
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for j in range(1, target + 1):
        for i in range(len(nums)):
            if j >= nums[i]:
                dp[j] += dp[j - nums[i]]
    return dp[target]

print(main())
