import collections


def solution(members, messages):
    # Return result in an array of strings "[user id = mentions count]"
    # Sort array by mention count in descending order or lexicographically ascending

    result = []
    my_map = {}

    for member in members:
        my_map[member] = 0

    for message in messages:
        words = message.split(" ")
        visited = []

        for word in words:
            word_len = len(word)

            if "@" in word:
                if word[1:word_len] == "all":
                    for member in members:
                        if member not in visited:
                            my_map[member] += 1
                    break
                if word[1:word_len] in members and word[1:word_len] not in visited:
                    my_map[word[1:word_len]] += 1
                    visited.append(word[1:word_len])

    d_asc_key = collections.OrderedDict(sorted(my_map.items(), key=lambda item: item[0]))
    d_descending = collections.OrderedDict(sorted(d_asc_key.items(), key=lambda item: item[1], reverse=True))

    tmp = list(d_descending.items())

    for item in tmp:
        result.append(item[0] + "=" + str(item[1]))
    return result
