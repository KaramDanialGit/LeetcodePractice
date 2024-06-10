def dp_solve(num_string : str):
    num_string = '0' + num_string
    size = len(num_string)

    dp = [0] * (size + 1)
    dp[0] = 1
    for i in range(size):
        if num_string[i - 1] == '0':
            dp[i] += dp[i - 1]
        else:
            tmp = num_string[i - 1 : i + 1]
            tmp_int = int(tmp)
            if tmp_int <= 25:
                dp[i] += dp[i - 2]
            dp[i] += dp[i - 1]
    return dp[i]

num_string = input()
print(dp_solve(num_string))