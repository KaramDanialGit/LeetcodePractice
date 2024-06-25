def solve():
    num_juices = int(input())
    inf = 10**10
    f = [[inf] * 8 for i in range(num_juices + 1)]
    f[0][0] = 0
    result = inf

    for i in range(num_juices):
        tmp = list(map(str, input().split()))
        cost = tmp[0]
        vitamins = tmp[1]
        mask = 0
        for pos in range(0, 3):
            c = chr(ord('C') - pos)
            have = 0

            for x in vitamins:
                if (x == c):
                    have = 1

            if have:
                mask += 1 << pos

        for string_mask in range(0, 8):
            f[i + 1][string_mask] = min(f[i + 1][string_mask], f[i][string_mask])
            f[i + 1][string_mask | mask] = min(f[i + 1][string_mask | mask], f[i][string_mask] + int(cost))

    result = f[num_juices][7]
    if result == inf: return -1
    return result

print(solve())