import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        pq = []
        if a > 0:
            pq.append([-a, "a"])
        if b > 0:
            pq.append([-b, "b"])
        if c > 0:
            pq.append([-c, "c"])
        heapq.heapify(pq)
        freq = [0, 0, 0]

        for i in range(a + b + c):
            if not pq:
                return result

            currentFreq, currentChar = heapq.heappop(pq)
            currentFreq = -1 * currentFreq
            freqIdx = ord(currentChar) - ord('a')

            if freq[freqIdx] == 2:
                if not pq:
                    return result
                else:
                    for i, frequency in enumerate(freq):
                        if frequency == 2:
                            freq[i] = 0

                    nextFreq, nextChar = heapq.heappop(pq)
                    nextFreq = -1 * nextFreq
                    result += nextChar
                    freq[ord(nextChar) - ord('a')] += 1
                    nextFreq -= 1
                    heapq.heappush(pq, [-currentFreq, currentChar])
                    if nextFreq > 0:
                        heapq.heappush(pq, [-nextFreq, nextChar])
            else:
                result += currentChar
                for i, frequency in enumerate(freq):
                    if frequency == 2:
                        freq[i] = 0
                freq[freqIdx] += 1
                currentFreq -= 1
                if currentFreq > 0:
                    heapq.heappush(pq, [-currentFreq, currentChar])

        return result