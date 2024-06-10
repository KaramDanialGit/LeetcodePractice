# RESOURCE: https://leetcode.com/discuss/interview-question/1543771/Databricks-or-OA-or-Longest-Palindrome-with-Pairs
import collections

def longest_palindrome(string_list):
    if not string_list or len(string_list) == 0:
        return False

    str_dict = collections.defaultdict(int)
    ans = 0

    for str in string_list:
        if str[0] == str[1]:
            ans += 2
            continue
        str_dict[str] += 1
    for str in string_list:
        if str_dict[str] == 0:
            continue
        str_tmp = str[1] + str[0]

        if str_dict[str_tmp] > 0:
            str_dict[str] -= 1
            str_dict[str_tmp] -= 1
            ans += 4
    print(ans)
    return ans

test_case = ["gh", "bc", "hg", "bb"]
longest_palindrome(test_case)
