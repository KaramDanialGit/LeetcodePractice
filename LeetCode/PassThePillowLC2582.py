# You can also simulate the solution but math is clearly faster

def passThePillow(self, n: int, time: int) -> int:
    full_rounds = time // (n - 1)
    extra_time = time % (n - 1)

    if full_rounds % 2 == 0:
        return extra_time + 1
    else:
        return n - extra_time