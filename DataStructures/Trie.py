class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.word_end = False


def insert_key(root, key):
    current = root

    for char in key:
        index = ord(char) - ord('a')

        if current.child[index] is None:
            newNode = TrieNode()
            current.child[char] = newNode

        current = current.child[char]

    current.word_end = True


def search_key(root, key):
    current = root

    for char in key:
        index = ord(char) - ord('a')

        if current.child[index] is None:
            return False

        current = current.child[char]

    return current.word_end


# Create an example Trie
root = TrieNode()
arr = ["and", "ant", "do", "geek", "dad", "ball"]
for s in arr:
    insert_key(root, s)

# One by one search strings
search_keys = ["do", "gee", "bat"]
for s in search_keys:
    print(f"Key : {s}")
    if search_key(root, s):
        print("Present")
    else:
        print("Not Present")