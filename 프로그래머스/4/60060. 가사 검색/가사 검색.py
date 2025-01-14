class TrieNode:
    def __init__(self):
        self.children = {}
        self.length_count = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.length_count = {}
    
    def insert_length_count(self, length):
        length_count = self.length_count
        self.length_count[length] = self.length_count.get(length, 0) + 1
        
    def insert(self, word):
        node = self.root  
        word_length = len(word)
        
        for i in range(word_length):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
            length = word_length-i-1
            length_count = node.length_count
            length_count[length] = length_count.get(length, 0) + 1
            
        node.isEnd = True
        
    def count_by_length(self, word):
        return self.length_count.get(word, 0)
    
    def count_starts_with(self, prefix, length):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.length_count.get(length, 0)

    
def solution(words, queries):
    trie = Trie()
    reverse_trie = Trie()
    
    for word in words:
        trie.insert(word)
        reverse_trie.insert(word[::-1])
        trie.insert_length_count(len(word))
    
    answer = []
    for query in queries:
        word_len = len(query)
        if query[0] == query[-1] == "?":
            answer.append(trie.count_by_length(word_len))
        elif query[-1] == "?":
            query = query.rstrip("?")
            answer.append(trie.count_starts_with(query, word_len-len(query)))
        else:
            query = query.lstrip("?")
            answer.append(reverse_trie.count_starts_with(query[::-1], word_len-len(query)))
    return answer