number_of_rooms = int(input())
viable_rooms = 0
for i in range(number_of_rooms):
    residents, max_quantity = list(map(int, input().split()))
    if max_quantity - residents >= 2:
        viable_rooms += 1

print(viable_rooms)