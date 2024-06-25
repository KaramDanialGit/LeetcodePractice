'''
Given two arrays of integers a and b of the same length, find the number of pairs (i, j) such that i ≤ j and a[i] - b[j] = a[j] - b[i].
'''

def Question_1(a, b):
    num_swapping_sums = 0

    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] - b[j] == a[j] - b[i]:
                num_swapping_sums += 1
    print(num_swapping_sums)

arr_1 = [2, -2, 5, 3]
arr_2 = [1, 5, -1, 1]
Question_1(arr_1, arr_2)

'''
You are given an array of positive integers arr. You'd like to know how many triangles can be formed with side lengths equal to adjacent elements from arr.
Construct an array of integers of length arr.length - 2, where the ith element is equal to 1 if it's possible to form a triangle with side lengths arr[i], arr[i + 1], and arr[i + 2], otherwise 0.
Return the resulting array of integers.

Note: A triangle can be formed with side lengths a, b, and c if a + b > c, a + c > b, and b + c > a.
'''

def Question_2(array):
    size = len(array)
    result = []
    if size < 3:
        return [0]

    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    for i in range(size - 2):
        if is_valid_triangle(array[i], array[i + 1], array[i + 2]):
            result.append(1)
        else:
            result.append(0)
    print(result)

Question_2([2, 10, 2, 10, 2])

'''
You found an old push-button phone in your room, but unfortunately some of the buttons are broken and can't be pushed 
anymore. To test the phone, you decided to try typing a message to your friend. Your task is to find which words of this
message will be possible to type using the broken keypad. You are given an array of integers digits representing the set
of phone buttons which are still working. You are also given an array of strings words containing the words you'd like 
to type in your message. Return an array of booleans, where the ith element is true if it is possible to type the ith
word, and false otherwise. Here is how the push-button phone looks like:
'''

def phone_2_words(digits, words):
    digits_map = { 2:"abc", 3:"def", 4:"ghi",
                   5:"jkl", 6:"mno", 7:"pqrs",
                   8:"tuv", 9:"wxyz", 0:""}
    result = []
    possible_chars = ""
    valid_word = True

    for digit in digits:
        possible_chars += digits_map[digit]

    for word in words:
        for char in word:
            if char not in possible_chars:
                valid_word = False
        if valid_word:
            result.append(True)
        else:
            result.append(False)
        valid_word = True
    print(result)

digits = [2, 3]
words = ["abc", "gdef"]
phone_2_words(digits, words)