# 给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
# 输出需要删除的字符个数。

# 输入描述:
# 输入数据有多组，每组包含一个字符串s，且保证: 1 <= s.length <= 1000.

# 输出描述:
# 对于每组数据，输出一个整数，代表最少需要删除的字符个数。

# 输入例子1:
# abcda
# google

# 输出例子1:
# 2
# 2


def main():
    s = input()
    rs = list(reversed(s))
    s = list(s)

    dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(s) + 1):
            if s[i - 1] == rs[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # elif dp[i][j - 1] > dp[i - 1][j]:
            #     dp[i][j] = dp[i][j - 1]
            # else:
            #     dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return len(s) - dp[len(s)][len(s)]


if __name__ == '__main__':
    print(main())
