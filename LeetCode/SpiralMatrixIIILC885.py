from copy import deepcopy
from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    rBound, lBound = cStart + 1, cStart - 1
    uBound, dBound = rStart - 1, rStart + 1
    current = [deepcopy(rStart), deepcopy(cStart)]
    vibes = []

    while len(vibes) < rows * cols:
        # Add shit
        while current[1] < rBound:
            if 0 <= current[1] < cols and 0 <= current[0] < rows:
                vibes.append(deepcopy(current))
            current[1] += 1

        rBound += 1

        while current[0] < dBound:
            if 0 <= current[1] < cols and 0 <= current[0] < rows:
                vibes.append(deepcopy(current))
            current[0] += 1

        dBound += 1

        while current[1] > lBound:
            if 0 <= current[1] < cols and 0 <= current[0] < rows:
                vibes.append(deepcopy(current))
            current[1] -= 1

        lBound -= 1

        while current[0] > uBound:
            if 0 <= current[1] < cols and 0 <= current[0] < rows:
                vibes.append(deepcopy(current))
            current[0] -= 1

        uBound -= 1

    return vibes

