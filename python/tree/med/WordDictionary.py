class wordnode:
    def __init__(self):
        self.children = {}
        self.endword = False
        
        
class WordDictionary:
    def __init__(self):
        self.root = wordnode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = wordnode()
            cur = cur.children[i]
        cur.endword = True
        # 和Trie相同。
        # 遍历word，如果不在root的child里，新建一个node。
        # 如果在的话。指针下移。
        # 将end写为True。


    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endword
        return dfs(0, self.root)
    # search不同在.匹配。
    # 通过recurse来解决。
    # function help()多一个参数来作index标记。
    # 遍历index到word尾部。结束时返回cur.endword，判断是否为完整的词。
    # 如果有「.」遍历root的children， 递归「.」的下一位在child里。
    # 如果找到-->True，反之亦然。
    # 如果没「.」，和Trie的search相同。
    
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)