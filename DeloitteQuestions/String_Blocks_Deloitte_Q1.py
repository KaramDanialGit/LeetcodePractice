# RESOURCE: https://leetcode.com/discuss/interview-question/1725338/Codility-or-OA-or-Deloitte-Hashedin

"""
You are given a string S consisting of letters 'a' and/or 'b'. A block is a consecutive fragment of S composed of the
same letters and surrounded by different letters or string endings. For example, S = "abbabbaaa" has five blocks: "a",
"bb", "a", "bb" and "aaa".
"""


def letters_to_add(string):
    current, future = 0, 0
    letter_groups = []
    max_string_len = 0
    answer = 0

    while future < len(string):
        if string[current] == string[future]:
            future += 1
        else:
            letter_groups.append(string[current: future])
            max_string_len = max(max_string_len, future - current)
            current = future

    max_string_len = max(max_string_len, future - current)
    letter_groups.append(string[current: future])

    for i in range(len(letter_groups)):
        answer += max_string_len - len(letter_groups[i])

    return answer


print(letters_to_add("abbabbaaa"))
