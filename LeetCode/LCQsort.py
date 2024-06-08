def SimpleSort(array: List[int]) -> List[int]:
    mini = float('-inf')
    while len(result) != len(testArr):
        for i in range(0, len(testArr)):
            if testArr[i] < mini and testArr[i] not in result:
                mini = testArr[i]
                testArr[i] = None
                result.append(mini)
                print(result)
    return array

testArr = [1,13,6,5,10]
print(SimpleSort(testArr))