from collections import defaultdict

def countOfAtoms(self, formula: str) -> str:
    n = len(formula)
    myMap = defaultdict(int)
    stack = [""]
    recentElement = ""
    i = 0

    while i < n:
        if formula[i] == '(':
            stack.append("")
            i += 1
        elif formula[i] == ')':
            multiple = 1
            tmp = stack[-1]

            if i + 1 < n and formula[i + 1].isnumeric():
                multiple = int(formula[i + 1])
                i += 2
            else:
                i += 1

            stack.pop()
            stack[-1] += tmp * multiple
        elif i + 1 < n and formula[i + 1].islower():
            stack[-1] += formula[i : i + 2]
            recentElement = formula[i : i + 2]
            i += 2
        elif formula[i].isnumeric():
            stack[-1] += recentElement * (int(formula[i]) - 1)
            i += 1
        else:
            stack[-1] += formula[i]
            recentElement = formula[i]
            i += 1

    result = "".join(stack)
    i = 0
    n = len(result)

    while i < n:
        if i < n - 1 and result[i + 1].islower():
            tmp = result[i] + result[i + 1]
            myMap[tmp] += 1
            i += 2
        else:
            myMap[result[i]] += 1
            i += 1

    result = ""
    keys = sorted(myMap)
    print(keys)

    for key in keys:
        myMap[key] += 1

    for key in keys:
        if myMap[key] - 1 > 1:
            result += key + str(myMap[key] - 1)
        else:
            result += key

    return result
            
