import sys
input = sys.stdin.readline

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.order = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.similar_words_order = (10, 10)
        self.similarity = 0
    
    def insert(self, word, order):
        node = self.root
        similar_node = self.root
        cur_similarity = 0
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                node.children[char].order = order
            else:
                cur_similarity += 1
                similar_node = node.children[char]
                
            node = node.children[char]
        node.is_end = True
        
        if (cur_similarity == self.similarity and self.similar_words_order[0] > similar_node.order) or cur_similarity > self.similarity:
            self.similarity = cur_similarity
            self.similar_words_order = (similar_node.order, order)
        
N = int(input())
words = [input().rstrip() for _ in range(N)]

trie = Trie()
for i in range(N):
    trie.insert(words[i], i)

print(*(words[i] for i in trie.similar_words_order), sep="\n")