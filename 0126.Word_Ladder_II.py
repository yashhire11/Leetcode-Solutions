class Solution:
    def __init__(self):
        self.graph = {}
        self.trace = {}

    def distanceOne(self, s1, s2):
        diffs = 0
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diffs = diffs+1
            if diffs > 1:
                return False
        return True

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []


        for word in wordList:
            self.graph[word] = []

        # The commented way below is actually too slow. As we approach 5000 nodes, our number of comparisons
        # are (5000 choose 2)*|s| where |s| is the length of the strings. Instead, we will need to check every possible
        # lowercase substitution of a given string. This results in a runtime of 26*|S|*N. For small S and large N,
        # this is clearly better, the alternative all possible combinations check is better.

        for word in wordList:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(0, len(word)):
                    word2 = word[:i]+c+word[i+1:]
                    if word2 in self.graph and word != word2:
                        self.graph[word].append(word2)
                        self.graph[word2].append(word)

        # Unique each node set
        for key in self.graph:
            self.graph[key] = list(set(self.graph[key]))

        # for i in range(0,len(wordList)):
        #     for j in range(i+1, len(wordList)):
        #         if sum(c1 != c2 for c1, c2 in zip(wordList[i], wordList[j])) == 1:
        #             self.graph[wordList[i]].append(wordList[j])
        #             self.graph[wordList[j]].append(wordList[i])



        startNode = beginWord
        self.graph[startNode] = []
        for node in self.graph:
            if node == startNode:
                continue
            if self.distanceOne(node, startNode):
                self.graph[startNode].append(node)

        level = self.BFS(startNode, endWord, [startNode])
        paths = self.backwards(level, endWord)
        return paths

    def BFS(self, start, endWord, visited):
        currList = [start]
        ended = False

        i = 1
        while currList and not ended:
            self.trace[i] = {}
            nextList = []
            for node in currList:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        if neighbor not in self.trace[i]:
                            self.trace[i][neighbor] = [node]
                        else:
                            self.trace[i][neighbor].append(node)
                        if neighbor not in nextList:
                            nextList.append(neighbor)
                        if neighbor == endWord:
                            ended = True
            [visited.append(x) for x in nextList]
            currList = nextList
            i = i+1
        retval = i-1
        return retval

    def backwards(self, level, endWord):
        if endWord not in self.trace[level]:
            return []

        currSet = self.trace[level][endWord]
        paths = [[x] for x in currSet]

        while level >= 2:
            nextPaths = []
            for path in paths:
                currNode = path[-1]
                for ele in self.trace[level-1][currNode]:
                    newpath = path.copy()
                    newpath.append(ele)
                    nextPaths.append(newpath)
            paths = nextPaths
            level = level - 1

        [x.reverse() for x in paths]
        [x.append(endWord) for x in paths]
        return paths

Sol = Solution()
print(Sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

