# RESOURCE: https://leetcode.com/discuss/interview-question/1461537/Databricks-OA

def difference_pairs(a, b):
    results = []
    min_len = min(len(a), len(b))

    for i in range(min_len):
        for j in range(i, min_len):
            if a[i] - b[j] == a[j] - b[i]:
                results.append([i,j])
    return results

print(difference_pairs([2,2],[2,2]))