stops = int(input())
min_capacity = 0
difference = 0
for i in range(stops):
    a, b = list(map(int, input().split()))
    difference += b-a
    if difference > min_capacity:
        min_capacity = difference

print(min_capacity)