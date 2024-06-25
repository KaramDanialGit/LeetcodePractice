"""
Given N towns, an array representing the number of people living in those town, and two arrays x[n],
y[n] representing x-y coordinates of the towns. We have to give location for holding a fair which minimizes the
distance at which people must travel to reach the fair. Cost for people living in ith town is |x[i]-X|+|y[i]-Y|. X,
Y being the location of the fair.
"""

def find_a_fair_location(num_towns, town_population, town_coordinates):
    total_distance = 0
    result = [float('inf'), 0, 0]
    num_rows = 0
    num_cols = 0

    for i in range(num_towns):
        for j in range(i, num_towns):
            num_rows = max(num_rows, abs(town_coordinates[i][0] - town_coordinates[j][0]))
            num_cols = max(num_cols, abs(town_coordinates[i][1] - town_coordinates[j][1]))

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(num_towns):
                total_distance = town_population[k] * (abs(i - town_coordinates[k][0]) + abs(j - town_coordinates[k][1]))
            if total_distance < result[0]:
                result = [total_distance, i, j]
    print(result)

# Find the farthest distance between two villages
# Create a matrix using the difference of those distances
# Iterate through the constructed matrix while testing the distance each populous must walk to reach that index

num_towns = 3
town_population = [100, 200, 160]
town_coordinates = [[69, 32], [100, 432], [523, 15]]

find_a_fair_location(num_towns, town_population, town_coordinates)