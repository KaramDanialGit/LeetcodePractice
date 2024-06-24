# RESOURCE: https://leetcode.com/discuss/interview-question/854052/Roblox-Intern-OA-2020

def fair(arrival,duration):
    all_intervals = []
    current_time = 0
    max_appointments = 0

    for i in range(len(arrival)):
        all_intervals.append([arrival[i],duration[i]])

    for i in range(len(all_intervals) - 1):
        if all_intervals[i][0] + all_intervals[i][1] <= all_intervals[i + 1][0]:
            max_appointments += 1

    print(max_appointments)

arrivals = list(map(int, input().split(',')))
durations = list(map(int, input().split(',')))
fair(arrivals,durations)