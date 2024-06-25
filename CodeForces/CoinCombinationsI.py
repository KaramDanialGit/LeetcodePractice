import collections
# TOP DOWN
number_coins, desired_sum = list(map(int, input().split()))
coins = list(map(int, input().split()))

dp = {}

def TopDown(desired_sum, subtract):
    num_ways = 0

    if (desired_sum == 0):
        return 1
    if (desired_sum < 0):
        return 0
    if desired_sum in dp:
        return dp[desired_sum]

    for i in range(len(subtract)):
        num_ways += TopDown(desired_sum - subtract[i], subtract)

    dp[desired_sum] = num_ways

    return num_ways

print(TopDown(desired_sum, coins))