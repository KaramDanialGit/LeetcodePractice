
def canChange(start: str, target: str) -> bool:
    sQueue = []
    tQueue = []

    for i in range(len(start)):
        if start[i] == "L" or start[i] == "R":
            sQueue.append((start[i], i))
        if target[i] == "L" or target[i] == "R":
            tQueue.append((target[i], i))

    if len(sQueue) != len(tQueue):
        return False

    while sQueue and tQueue:
        sChar, sIndex = sQueue.pop(0)
        tChar, tIndex = tQueue.pop(0)

        if (
            sChar != tChar
            or (sChar == "L" and sIndex < tIndex)
            or (sChar == "R" and sIndex > tIndex)
        ):
            return False

    return True