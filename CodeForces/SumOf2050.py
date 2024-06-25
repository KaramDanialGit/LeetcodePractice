import math

test_cases = int(input())

for _ in range(test_cases):
    number = int(input())
    exponent = 0

    if number < 2050:
        print("-1")
        continue

    while 2050 * (10 ** exponent) <= number:
        exponent += 1

    exponent -= 1
    tmp_number = 2050 * (10 ** exponent)
    counter = 0
    printed = False
    while number > 0:
        while number >= tmp_number:
            number -= tmp_number
            counter += 1
        exponent -= 1
        tmp_number = 2050 * (10 ** exponent)
        if number < 2050 and number > 0:
            print("-1")
            printed = True
            break
    if printed == False:
        print(counter)