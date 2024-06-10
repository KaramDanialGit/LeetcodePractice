# RESOURCE: https://leetcode.com/discuss/interview-question/1460091/Databricks-or-Quora-or-Amazon-OA-memory-allocator
import collections

def malloc(memory,queries):
    atomic_counter = 1
    length_map = []

    for query in queries:
        if query[0] == 0:
            result = [alloc(memory,query[1]), query[1]]
            length_map.append(result)
            if result[0] != -1:
                atomic_counter += 1
        if query[0] == 1:
            for arr in length_map:
                if query[1] in arr:
                    erase(memory, arr[0], arr[1])
                else:
                    print(-1)
    print(memory)

def alloc(memory,x):
    zero_count = 0

    for i in range(len(memory)):
        if memory[i] == 0:
            zero_count += 1

            if zero_count == x:
                for j in range(x,-1,-1):
                    memory[j] = 1
                return i - x

        if memory[i] == 1:
            zero_count = 0
    return -1

def erase(memory,index,length):

    for i in range(index,length + 1):
        memory[i] = 0
    return length

mem = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
query_list = [[0, 2], [0, 1], [0, 1], [1, 2], [1, 4], [0, 4]]
print(malloc(mem,query_list))
