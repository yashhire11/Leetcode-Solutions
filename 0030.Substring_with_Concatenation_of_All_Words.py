class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return[]
        K = len(words[0])
        N = len(s)
        W = len(words)
        ans = []

        def increment(word, number, counter):
            count[word] += number
            if count[word] == 0:
                del count[word]

        for start in range(K):
            current = start
            if current + W * K > N:
                continue

            count = collections.Counter()
            for word in words:
                count[word] += 1

            for _ in range(W):
                increment(s[current:current+K], -1, count)
                current += K

            if len(count) == 0:
                ans.append(current - (W * K))

            while current + K <= N:
                increment(s[current:current+K], -1, count)
                increment(s[current-(W*K):current-(W-1)*K], +1, count)
                current += K
                if len(count) == 0:
                    ans.append(current - (W * K))
        return ans



"""
"wordgoodgoodgoodbestword"
["word","good","best","word"]
N = 4
s = 0,4,8,12,16
s = 1,5,9,13,17
s = 2,6,10,14 ..
s = 3 ...
"""
