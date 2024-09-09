"""
Input: S = [1, 2, 6, 5, 3], E = [5, 5, 7, 6, 8]
Output: 3
Explanation:
There are five guests attending the party.
The 1st guest will arrive at time 1. We need one chair at time 1.
The 2nd guest will arrive at time 2. There are now two guests at the party, so we need two chairs at time 2.
The 5th guest will arrive at time 3. There are now three guests at the party, so we need three chairs at time 3.
The 4th guest will arrive at time 5 and, at the same moment, the 1st and 2nd guests will leave the party.
There are now two (the 4th and 5th) guests at the party, so we need two chairs at time 5.
The 3rd guest will arrive at time 6, and the 4th guest will leave the party at the same time.
There are now two (the 3rd and 5th) guests at the party, so we need two chairs at time 6.
So we need at least 3 chairs.
"""

def maxChairs(enters, exits):
    limit1 = max(enters)
    limit2 = max(exits)
    chairs = [0] * (max(limit1, limit2) + 1)
    result = 0

    for en, ex in zip(enters, exits):
        chairs[en] += 1
        chairs[ex] -= 1

    for i in range(1, len(chairs)):
        chairs[i] += chairs[i - 1]

        if chairs[i] > result:
            result = chairs[i]
    print(chairs)
    return result


enterTime = [7, 2]
exitTime = [10, 4]

print(maxChairs(enterTime, exitTime))