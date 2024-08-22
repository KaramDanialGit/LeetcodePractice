
def findComplement(num: int) -> int:
    numStr = str(bin(num))[2:]

    for i in range(len(numStr)):
        num ^= (1 << i)

    return num