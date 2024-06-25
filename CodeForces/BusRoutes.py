test_cases = int(input())

for i in range(test_cases):
    number_of_buses, D = list(map(int, input().split()))
    buses = list(map(int, input().split()))

    for j in range(number_of_buses-1, -1, -1):
        divided = D // buses[j]
        latest_day = divided * buses[j]
        D = latest_day

    print("Case #%s: %s" % (i + 1, D))