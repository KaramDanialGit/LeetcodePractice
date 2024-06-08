
def fill_shape(n) -> int:
    width = n
    res = 1
    if width % 2 != 0:
        return 0

    for i in range(0, width, 2):
        res *= 2
    return res

shape_width = int(input())
print(fill_shape(shape_width))