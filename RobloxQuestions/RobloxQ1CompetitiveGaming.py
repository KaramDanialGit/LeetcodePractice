# RESOURCE: https://leetcode.com/discuss/interview-question/850397/Roblox-Hackerrank-2021

def CompetitiveGaming(n,k,scores):
    scores.sort(reverse=True)
    placements = []
    seen = []
    placement = 1

    for i in range(len(scores)):
        if scores[i] in seen:
            placements.append(placements[-1])
            placement += 1
        else:
            seen.append(scores[i])
            placements.append(placement)
            placement += 1
        if placement > k:
            break

    print(placements)

n = 4
k = 3
scores = [100,100,100,10]
CompetitiveGaming(n,k,scores)