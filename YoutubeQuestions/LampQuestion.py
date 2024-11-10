"""
Given an array lamp light ranges [start, end] on a long horizontal street, determine which chair on the street under those lamps
has the most lamps illuminating it simultaneously.
"""
import heapq

def mostLuminatedChair(light_ranges, chair_pos):
    event_heaps = []
    cur_lights = 0
    result = []

    for idx_start, idx_end in light_ranges:
        heapq.heappush(event_heaps, [idx_start, 1])
        heapq.heappush(event_heaps, [idx_end, -1])

    for chair_idx in chair_pos:
        heapq.heappush(event_heaps, [chair_idx, 0])

    while event_heaps:
        event = heapq.heappop(event_heaps)
        cur_lights += event[1]

        if event[1] == 0:
            result.append(cur_lights)

    print(result)
    return max(result)

lamp_lights = [[-20,-3], [-10,-1], [-5,14], [11,15]]
chair_positions = [-17, -10, -4, 4, 12, 16]
mostLuminatedChair(lamp_lights, chair_positions)