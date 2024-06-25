tests = int(input())

for k in range(tests):
    # much faster way to just get the remainder
    num_buildings = input()
    heights = list(map(int, input().split(" ")))
    tot_heights = 0

    for i in range(len(heights)):
        tot_heights += heights[i]

    mod = tot_heights % len(heights)
    if mod == 0:
        print(mod)
    else:
        print(1)
