
def compressedString(word: str) -> str:
    ptr1 = ptr2 = 0
    n = len(word)
    comp = ""

    while ptr2 < n:
        cur_counter = 0

        while ptr2 < n and word[ptr2] == word[ptr1] and (ptr2 - ptr1 + 1) <= 9:
            cur_counter += 1
            ptr2 += 1

        comp += str(cur_counter) + word[ptr1]
        ptr1 = ptr2

    return comp