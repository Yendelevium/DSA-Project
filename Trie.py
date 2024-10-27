class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocorrect(self, word):
        def dfs(node, word, index, path, results, max_edits, edits):
            if edits > max_edits:
                return
            if index == len(word):
                if node.is_end_of_word:
                    results.append((path, edits))
                return
            if word[index] in node.children:
                dfs(node.children[word[index]], word, index + 1, path + word[index], results, max_edits, edits)
            for char, child_node in node.children.items():
                if char != word[index]:
                    dfs(child_node, word, index + 1, path + char, results, max_edits, edits + 1)
                dfs(child_node, word, index, path + char, results, max_edits, edits + 1)

        results = []
        dfs(self.root, word, 0, "", results, max_edits=1, edits=0)
        results.sort(key=lambda x: x[1])
        return [result[0] for result in results]

    def autocomplete(self, prefix):
        def dfs(node, prefix, results):
            if node.is_end_of_word:
                results.append(prefix)
            for char, child_node in node.children.items():
                dfs(child_node, prefix + char, results)

        results = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return results
            node = node.children[char]
        dfs(node, prefix, results)
        return results

    def substring_match(self, substring):
        def dfs(node, path, results):
            if node.is_end_of_word and substring in path:
                results.append(path)
            for char, child_node in node.children.items():
                dfs(child_node, path + char, results)

        results = []
        dfs(self.root, "", results)
        return results