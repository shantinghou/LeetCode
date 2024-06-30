class RoseTree:
    def __init__(self):
        self.end = False
        self.dic = [None]*26
        
class WordDictionary:

    def __init__(self):
        self.words = RoseTree()

    def addWord(self, word: str) -> None:
        cur = self.words
        for c in word:
            i = ord(c) - ord('a')
            if cur.dic[i] == None:
                cur.dic[i] = RoseTree()
            cur = cur.dic[i]
        cur.end = True
        
    def search(self, word: str) -> bool:

        def find(word, cur):
            if len(word) == 0:
                return cur.end == True
            c = word[0]
            if c == '.': 
                for dic in cur.dic:
                    if dic != None and find(word[1:], dic):
                        return True
            else: 
                i = ord(c) - ord('a')
                if cur.dic[i] == None:
                    return False
                else:
                    return find(word[1:], cur.dic[i])
            
        return find(word, self.words)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)