class PrefixTree:
    
    def __init__(self):
        self.head = Node()    

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                new = Node()
                curr.children[c] = new
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Node:
    def __init__(self):
        self.children = {}
        self.end = False