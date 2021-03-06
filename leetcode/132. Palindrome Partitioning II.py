# https://leetcode.com/problems/palindrome-partitioning-ii/description/

# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


def main():
    MAX = 1 << 30
    s = input()
    length = len(s)
    dp = [-1 for _ in range(length + 1)]
    p = [[False for _ in range(length)] for _ in range(length)]

    for i in range(length - 1, -1, -1):
        dp[i] = MAX
        for j in range(i, length, 1):
            if (s[i] == s[j]) and ((j - i < 2) or p[i + 1][j - 1] is True):
                p[i][j] = True
                dp[i] = min(dp[i], dp[j + 1] + 1)

    return dp[0]


if __name__ == '__main__':
    result = main()
    print(result)
