from math import gcd

def fractionAddition(expression: str) -> str:
    queue = [""]

    for char in expression:
        if char == '+':
            queue.append("")
            continue
        elif char == '/':
            queue.append("")
        elif char == '-' and queue[-1] != "":
            queue.append("-")
        else:
            queue[-1] += char
    print(queue)

    while len(queue) > 3:
        firstNum = int(queue.pop(0))
        secondNum = int(queue.pop(0))

        if not queue:
            return str(firstNum) + "/" + str(secondNum)

        thirdNum = int(queue.pop(0))
        fourthNum = int(queue.pop(0))

        numerator = firstNum * fourthNum + thirdNum * secondNum
        denominator = secondNum * fourthNum
        GCD = gcd(abs(numerator), denominator)
        numerator = numerator // GCD
        denominator = denominator // GCD

        queue.append(str(numerator))
        queue.append(str(denominator))

    return str(queue[0]) + "/" + str(queue[1])