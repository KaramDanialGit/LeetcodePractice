'''
You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a
from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from
a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Example

For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
solution(a, b, k) = 2.
'''

def find_tiny_pairs(a, b, k):
    size = len(a)
    str_num = ""
    answer = 0

    for i in range(size):
        str_num += str(a[i])
        str_num += str(b[size - i - 1])
        if int(str_num) < k:
            answer += 1
        str_num = ""
    print(answer)

a = [1, 2, 3]
b = [1, 2, 3]
k = 31
find_tiny_pairs(a, b, k)