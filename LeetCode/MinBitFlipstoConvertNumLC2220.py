def minBitFlips(start: int, goal: int) -> int:
    result = str(bin(start ^ goal))
    return result.count("1")