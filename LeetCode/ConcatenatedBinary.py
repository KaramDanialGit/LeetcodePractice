def concatenatedBinary(n: int) -> int:
    str_cat = ""

    for i in range(1, n + 1):
        binary_string = str(bin(i))

        for j in range(len(binary_string)):
            if binary_string[j] == 'b':
                str_cat += binary_string[j + 1:]
                break
    return int(str_cat, 2) % (10 ** 9 + 7)