test_cases = int(input())
myTables = []
for _ in range(test_cases):
    height, width = list(map(int, input().split()))

    table_plates = [[0] * width for i in range(height)]

    for i in range(height):
        for j in range(width):
            if (i - 1 < 0) and (j - 1 < 0):
                table_plates[i][j] = 1
                continue

            if i == 0:
                if (table_plates[i][j - 1] != 1):
                    table_plates[i][j] = 1
                    continue

            if (i == height - 1):
                if (j + 1 <= width - 1):
                    if (table_plates[i][j - 1] != 1 and
                        table_plates[i - 1][j] != 1 and
                        table_plates[i - 1][j + 1] != 1 and
                        table_plates[i - 1][j - 1] != 1 ):
                        table_plates[i][j] = 1
                        continue
                elif (table_plates[i][j - 1] != 1 and
                    table_plates[i - 1][j] != 1 and
                    table_plates[i - 1][j - 1] != 1 ):
                    table_plates[i][j] = 1
                    continue

            if j == 0:
                if (table_plates[i - 1][j] != 1):
                    table_plates[i][j] = 1
                    continue

            if (j == width - 1):
                if (table_plates[i - 1][j] != 1 and
                    table_plates[i][j - 1] != 1 and
                    table_plates[i - 1][j - 1] != 1 ):
                    table_plates[i][j] = 1
                    continue

    for row in table_plates:
        for element in row:
            print(element, end="")
        print()