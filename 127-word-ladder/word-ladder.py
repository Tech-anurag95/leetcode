class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        visited={beginWord}
        words=set(wordList)
        choices="abcdefghijklmnopqrstuvwxyz"
        queue=deque([(beginWord,1)])
        while queue:
            word,number=queue.popleft()
            if word==endWord:
                return number
            for i in range(len(word)):
               for choice in choices:
                    news=word[:i]+choice+word[i+1:]
                    if news in words and news not in visited:
                        visited.add(news)
                        queue.append((news,number+1))
        return 0
                




        
        



        