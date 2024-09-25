"""
Given a set of starting and ending points for a set of intervals, return the number of overlaps each interval experiences
"""

def overlaps(intervals):
    length = len(intervals)
    result = []

    for i in range(length):
        intersections = 0
        start, end = intervals[i]

        for j in range(length):
            if i != j:
                if (
                    (start == intervals[j][0]) or (end == intervals[j][1]) or (start >= intervals[j][0] and end <= intervals[j][1]) or
                    (start <= intervals[j][0] and end >= intervals[j][1]) or (start <= intervals[j][1] and end >= intervals[j][0])
                ):
                    intersections += 1
        result.append(intersections)

    return result


test = [[4,7], [1,6], [1,1], [4,5], [3,4]]
print(overlaps(test))