"""
Given a list of similar names and a second list of each name and their frequency add them all under one name and report them as a list

Name    Freq
Jim     10
Jimmy	5
Paul	1
Carl	3
Carle	5
Caryl	9
John	2
Jonny	14
Jon     40

Name    Synonym
Jim     Jimmy
Jimmy   Jim
Carl	Carle
Carle	Carl
Caryl	Carle
John	Jon
Jonny	John
Jon     John

output: Jim (15), Paul (1), Carl (17), John (56)
"""


from collections import defaultdict

def similarNameFreq(freqNames, synonyms):
    result = {}
    graph = defaultdict(set)
    visited = set()

    for name, syn in synonyms:
        graph[name].add(syn)
        graph[syn].add(name)

    def dfs(name, visited, tmp):
        if name in visited:
            return

        tmp.add(name)
        visited.add(name)

        dfs(name, visited, tmp)

    for name in freqNames.keys():
        tmp = set()
        total = 0

        for n in graph[name]:
            if n not in visited:
                dfs(n, visited, tmp)

            for i in graph[n]:
                if i not in visited:
                    dfs(i, visited, tmp)

        if tmp:
            for word in tmp:
                total += freqNames[word]

            result[tuple(tmp)] = total;

    output = ""
    for group, total in result.items():
        output += group[0] + " " + "(" + str(total) + ")"
        if group != list(result.keys())[-1]:
            output += ", "

    return output

synonyms = [
    ["Jim",   "Jimmy"],
    ["Jimmy", "Jim"],
    ["Carl",  "Carle"],
    ["Carle", "Carl"],
    ["Caryl", "Carle"],
    ["John",  "Jon"],
    ["Jonny", "John"],
    ["Jon",   "John"],
    ["Paul",   "Paul"],
]

freqNames = {
    "Jim":    10,
    "Jimmy":  5,
    "Paul":   1,
    "Carl":   3,
    "Carle":  5,
    "Caryl":  9,
    "John":   2,
    "Jonny":  14,
    "Jon":    40
}

test1 = similarNameFreq(freqNames, synonyms)
print(test1)