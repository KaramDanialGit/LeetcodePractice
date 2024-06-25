test_cases = int(input())

for _ in range(test_cases):
    input()
    n, k = list(map(int, input().split()))
    ac_position = list(map(int, input().split()))
    ac_temperature = list(map(int, input().split()))

    result_list = [float('inf')] * (n + 2)
    my_map = {}

    for i in range(k):
        my_map[ac_position[i]] = ac_temperature[i]

    for i in range(n, 0, -1):
        if i in my_map:
            if (i + 1) < n:
                result_list[i] = min(my_map[i], result_list[i + 1] + 1, result_list[i])
            else:
                result_list[i] = min(my_map[i], result_list[i])
        else:
            if (i + 1) <= n:
                result_list[i] = min(result_list[i + 1] + 1, result_list[i])

    for i in range(n + 2):
        if i in my_map:
            if (i - 1) > 0:
                result_list[i] = min(my_map[i], result_list[i - 1] + 1, result_list[i])
            else:
                result_list[i] = min(my_map[i], result_list[i])
        else:
            if (i - 1) > 0:
                result_list[i] = min(result_list[i - 1] + 1, result_list[i])

    result = " ".join(map(str, result_list[1:-1]))
    print(result)