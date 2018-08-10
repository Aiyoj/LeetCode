# 链接：https://www.nowcoder.com/questionTerminal/3e901cac7b074621b3b6178eee8b1eaf
# 来源：牛客网
#
# 给出一个整数n，将n分解为至少两个整数之和，使得这些整数的乘积最大化，输出能够获得的最大的乘积。
# 例如：
# 2=1+1，输出1；
# 10=3+3+4，输出36。
#
# 输入描述:
#
# 输入为1个整数
#
#
# 输出描述:
#
# 输出为1个整数
# 示例1
# 输入
#
# 10
# 输出
#
# 36


def main():
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1

    for i in range(2, n + 1):
        for j in range(2, i):
            dp[i] = max(dp[i], j * max(dp[i - j], i - j))
    return dp[n]

print(main())
