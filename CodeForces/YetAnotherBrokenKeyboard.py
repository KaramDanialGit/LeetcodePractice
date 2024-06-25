def solve():
    len_s, len_available = list(map(int, input().split()))
    s = input()
    available = list(map(str, input().split()))
    sum = 0
    num_arr = []
    dp = [0] * (len_s)

    for i in range(len_s):
        if s[i] in available:
            num_arr.append(1)
        else:
            num_arr.append(0)

    dp[0] = num_arr[0]
    sum += dp[0]

    for i in range(1, len(num_arr)):
        if (num_arr[i] == 1):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
        sum += dp[i]

    print(sum)

print(solve())