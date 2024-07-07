def numWaterBottles(numBottles: int, numExchange: int) -> int:
    result = numBottles
    remaining = numBottles

    while remaining >= numExchange:
        result += floor(remaining / numExchange)
        remaining = floor(remaining / numExchange) + remaining % numExchange

    return result