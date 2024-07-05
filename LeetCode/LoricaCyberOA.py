# LoricaCyber OA Questions

# QUESTION 1: longest k unique substring
# test case: 2aaabc answer: "aaab"

def SearchingChallenge(strParam):
  result = ""
  ChallengeToken = "8pyong46ae"
  N = len(strParam)
  k = int(strParam[0])
  window = []
  
  for i in range(1, N):
    window.append(strParam[i])
    mySet = set(window)

    while len(mySet) > k:
      window.pop(0)
      mySet.pop()

    if len(window) > len(result):
      result = "".join(window)

  final = ChallengeToken + ":" + result
  return final[::-1]


print(SearchingChallenge(input()))


# QUESTION 2: 5-ELEMENT LRU CACHE
def ArrayChallenge(strArr):
  cache = []
  # Used a set for faster look ups
  lookup = set()

  for char in strArr:
    if char not in lookup:
      cache.append(char)
      lookup.add(char)

      if len(cache) > 5:
        val = cache[0]
        cache.pop(0)
        lookup.remove(val)
    else:
      N = len(cache)
      i = cache.index(char)
      tmp = cache[i]

      for i in range(i, N-1):
        cache[i] = cache[i + 1]
      cache[N - 1] = tmp

  return "-".join(cache)[::-1] + ":" + "8pyong46ae"[::-1]

 
print(ArrayChallenge(input()))