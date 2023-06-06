# Give a list of documents and give a list of keywords, write two function:
# getOr - return the list of documents containing at least one keyword
# getAnd - return the list of documents containing all the keywords
import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def searchLCP(self, word: str):
        node = self.root
        prefix = ""
        for curr in word:
            if curr in node.children and not node.isEnd:
                prefix += curr
                node = node.children[curr]
            else:
                return prefix
        return prefix

    def insert(self, word: str) -> None:
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root
        # Search character by character in trie
        for c in word:
            # if character path does not exist, return False
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd


    def startsWith(self, prefix: str) -> bool:
        # Same as search, except there is no isEnd condition at final return
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

def longestCommonPrefix(strs: List[str], q: str) -> str:
    # Trie O(S) build and O(m) search, m = len(q), S(S) for trie
    if not strs: return ""
    if len(strs) == 1: return strs[0]
    trie = Trie()
    for i in range(1, len(strs)):
        trie.insert(strs[i])

    return trie.searchLCP(q)

def getAnd(docs, keywords):
    res = set()
    terms = set()
    tokens = []    # 2-D list, each item is a list of tokens from a doc
    inverted_index = {}
    # docs[i] would be matched with tokens[i]
    for i in range(len(docs)):
        tokens.append(docs[i].lower().split())

    # collect all terms
    for lst in tokens:
        terms = terms.union(set(lst))

    # create inverted index
    for term in terms:
        documents = []
        for i in range(len(docs)):
            if term in tokens[i]:
                documents.append(i)
        inverted_index[term] = documents

    # search
    for word in keywords:
        if word in inverted_index:
            res = res.union(set(inverted_index[word]))
    return list(res)

def getOr(docs, keywords, num):
    words = random.sample(keywords, num)
    return getAnd(docs, words)

# Define the documents
document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"
document3 = "I have a beautiful house by the beach and near the lighthouse"
document4 = "She is a great employee working on a significant project"

d = []
d.append(document1)
d.append(document2)
d.append(document3)
d.append(document4)
k = ["the", "quick", "fix", "I", "sample", "r"]
k2 = ["the"]
print(getOr(d, k, 3))
print(getAnd(d, k))
print(getAnd(d, [longestCommonPrefix(k2, "there")]))