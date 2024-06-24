# RESOURCE: https://leetcode.com/discuss/interview-question/851513/roblox-new-grad-2021-oa-hackerrank

def CommonPrefixLenght(word):
    n = len(word)
    max_length = 0

    for i in range(len(word)):
        prefix = word[0:i]
        suffix = word[i:n]
        min_len = min(len(prefix), len(suffix))

        if prefix == "":
            max_length += len(suffix)
        else:
            for j in range(min_len):
                if prefix[j] != suffix[j]:
                    break
                max_length += min_len

    print(max_length)

input_str = input()
CommonPrefixLenght(input_str)