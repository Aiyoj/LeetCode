# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?


def main():
    n = int(input())
    rating_value = list(map(int, input().split(' ')))
    cnt = [1 for _ in range(n)]
    for i in range(1, n):
        if rating_value[i] > rating_value[i - 1]:
            cnt[i] = cnt[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if rating_value[i] > rating_value[i + 1] and cnt[i] < cnt[i + 1]:
            cnt[i] = cnt[i + 1] + 1
    return sum(cnt)


if __name__ == '__main__':
    res = main()
    print(res)
